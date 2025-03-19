#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : cfitsio
Version  : 4.6.0
Release  : 17
URL      : https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/cfitsio-4.6.0.tar.gz
Source0  : https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/cfitsio-4.6.0.tar.gz
Summary  : FITS File Subroutine Library
Group    : Development/Tools
License  : ISC
Requires: cfitsio-bin = %{version}-%{release}
Requires: cfitsio-lib = %{version}-%{release}
Requires: cfitsio-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : curl-dev
BuildRequires : file
BuildRequires : gfortran
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
===============================================================================
===============================================================================
= with CFITSIO up until version 3.35 in 2013.  These instruction may still work
= with more recent versions of CFITSIO, however, users are strongly urged to
===============================================================================
===============================================================================

%package bin
Summary: bin components for the cfitsio package.
Group: Binaries
Requires: cfitsio-license = %{version}-%{release}

%description bin
bin components for the cfitsio package.


%package dev
Summary: dev components for the cfitsio package.
Group: Development
Requires: cfitsio-lib = %{version}-%{release}
Requires: cfitsio-bin = %{version}-%{release}
Provides: cfitsio-devel = %{version}-%{release}
Requires: cfitsio = %{version}-%{release}

%description dev
dev components for the cfitsio package.


%package lib
Summary: lib components for the cfitsio package.
Group: Libraries
Requires: cfitsio-license = %{version}-%{release}

%description lib
lib components for the cfitsio package.


%package license
Summary: license components for the cfitsio package.
Group: Default

%description license
license components for the cfitsio package.


%prep
%setup -q -n cfitsio-4.6.0
cd %{_builddir}/cfitsio-4.6.0
pushd ..
cp -a cfitsio-4.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742398492
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742398492
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cfitsio
cp %{_builddir}/cfitsio-%{version}/licenses/License.txt %{buildroot}/usr/share/package-licenses/cfitsio/c287787ea3432b806844ccb7571d6b8e3cd4a7ef || :
cp %{_builddir}/cfitsio-%{version}/licenses/License.txt %{buildroot}/usr/share/package-licenses/cfitsio/c287787ea3432b806844ccb7571d6b8e3cd4a7ef || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/cookbook
/V3/usr/bin/fitscopy
/V3/usr/bin/fitsverify
/V3/usr/bin/fpack
/V3/usr/bin/funpack
/V3/usr/bin/imcopy
/V3/usr/bin/smem
/V3/usr/bin/speed
/usr/bin/cookbook
/usr/bin/fitscopy
/usr/bin/fitsverify
/usr/bin/fpack
/usr/bin/funpack
/usr/bin/imcopy
/usr/bin/smem
/usr/bin/speed

%files dev
%defattr(-,root,root,-)
/usr/include/cfortran.h
/usr/include/drvrsmem.h
/usr/include/f77_wrap.h
/usr/include/fitsio.h
/usr/include/fitsio2.h
/usr/include/longnam.h
/usr/include/region.h
/usr/lib64/libcfitsio.so
/usr/lib64/pkgconfig/cfitsio.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libcfitsio.so.10.0.0
/usr/lib64/libcfitsio.so.10
/usr/lib64/libcfitsio.so.10.0.0
/usr/lib64/libcfitsio.so.10.4.6.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cfitsio/c287787ea3432b806844ccb7571d6b8e3cd4a7ef
