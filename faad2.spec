Summary:    Open source MPEG-4 and MPEG-2 AAC decoder
Name:       faad2
Epoch:      1
Version:    2.8.8
Release:    1%{?dist}
License:    GPLv2+
URL:        http://www.audiocoding.com/faad2.html

Source:     http://downloads.sourceforge.net/sourceforge/faac/%{name}-%{version}.tar.gz
# fix non-PIC objects in libmp4ff.a
Patch0:     %{name}-2.8.8-pic.patch

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
Requires:   %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
FAAD 2 is a LC, MAIN and LTP profile, MPEG2 and MPEG-4 AAC decoder, completely
written from scratch.

This package contains development files and documentation for libfaad.

%prep
%setup -q
%patch0 -p1 -b .pic

%build
autoreconf -vif
%configure \
    --disable-static \
    --with-drm \
    --with-mpeg4ip \
    --without-xmms

make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -name "*.la" -delete

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%{_bindir}/faad
%{_mandir}/man1/faad.1*

%files libs
%license COPYING
%doc AUTHORS ChangeLog README*
%{_libdir}/libfaad.so.*
%{_libdir}/libfaad_drm.so.*

%files devel
%doc TODO
%{_includedir}/*.h
%{_libdir}/libfaad.so
%{_libdir}/libfaad_drm.so

%changelog
* Tue Apr 10 2018 Simone Caronni <negativo17@gmail.com> - 1:2.8.8-1
- Update to 2.8.8.

* Fri Apr 22 2016 Simone Caronni <negativo17@gmail.com> - 1:2.7-8
- Clean up SPEC file.
- Use autotools to avoid RPATH generation.
- Move documents and license to libs subpackage.

* Thu Jun 11 2015 Simone Caronni <negativo17@gmail.com> - 1:2.7-7
- Remove xmms support.

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 1:2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
