Summary:    Open source MPEG-4 and MPEG-2 AAC decoder
Name:       faad2
Epoch:      1
Version:    2.7
Release:    8%{?dist}
License:    GPLv2+
URL:        http://www.audiocoding.com/faad2.html

Source:     http://downloads.sourceforge.net/sourceforge/faac/%{name}-%{version}.tar.bz2
# fix non-PIC objects in libmp4ff.a
Patch0:     %{name}-pic.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  id3lib-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel

%description
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

%package    libs
Summary:    Shared libraries of the FAAD 2 AAC decoder

%description libs
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

This package contains the shared library libfaad.

%package    devel
Summary:    Development libraries of the FAAD 2 AAC decoder
Requires:   %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

This package contains development files and documentation for libfaad.

%prep
%setup -q
%patch0 -p1 -b .pic
find . -name "*.c" -o -name "*.h" -exec chmod 644 {} \;

for f in AUTHORS COPYING ChangeLog NEWS README* TODO ; do
    tr -d '\r' <$f >$f.n && touch -r $f $f.n && mv -f $f.n $f
done

%build
autoreconf -vif
%configure \
    --disable-static \
    --without-xmms

make %{?_smp_mflags}

%install
%make_install
install -d -m755 %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_mandir}/{manm/faad.man,man1/faad.1}

rm %{buildroot}%{_libdir}/libfaad.la
rm %{buildroot}%{_includedir}/mp4ff{,int}.h
rm %{buildroot}%{_libdir}/libmp4ff.a

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/faad
%{_mandir}/man1/faad.1*

%files libs
%license COPYING
%doc AUTHORS ChangeLog NEWS README*
%{_libdir}/libfaad.so.*

%files devel
%doc TODO docs/Ahead?AAC?Decoder?library?documentation.pdf
%{_includedir}/*.h
%{_libdir}/libfaad.so

%changelog
* Fri Apr 22 2016 Simone Caronni <negativo17@gmail.com> - 1:2.7-8
- Clean up SPEC file.
- Use autotools to avoid RPATH generation.
- Move documents and license to libs subpackage.

* Thu Jun 11 2015 Simone Caronni <negativo17@gmail.com> - 1:2.7-7
- Remove xmms support.

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 1:2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
