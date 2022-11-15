#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cfitsio
Version  : 4.2.0
Release  : 10
URL      : https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/cfitsio-4.2.0.tar.gz
Source0  : https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/cfitsio-4.2.0.tar.gz
Summary  : FITS File Subroutine Library
Group    : Development/Tools
License  : ISC
Requires: cfitsio-lib = %{version}-%{release}
Requires: cfitsio-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : curl-dev
BuildRequires : pkgconfig(zlib)

%description
CFITSIO Interface Library
CFITSIO is a library of ANSI C routines for reading and writing FITS
format data files.  A set of Fortran-callable wrapper routines are also
gives a brief summary of how to build and test CFITSIO, but the CFITSIO
User's Guide, found in the files cfitsio.doc (plain text), cfitsio.tex
(LaTeX source file), cfitsio.ps, or cfitsio.pdf should be
referenced for the latest and most complete information.

%package dev
Summary: dev components for the cfitsio package.
Group: Development
Requires: cfitsio-lib = %{version}-%{release}
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
%setup -q -n cfitsio-4.2.0
cd %{_builddir}/cfitsio-4.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1668546369
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1668546369
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cfitsio
cp %{_builddir}/cfitsio-%{version}/License.txt %{buildroot}/usr/share/package-licenses/cfitsio/c287787ea3432b806844ccb7571d6b8e3cd4a7ef || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/drvrsmem.h
/usr/include/fitsio.h
/usr/include/fitsio2.h
/usr/include/longnam.h
/usr/lib64/libcfitsio.so
/usr/lib64/pkgconfig/cfitsio.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcfitsio.so.10
/usr/lib64/libcfitsio.so.10.4.2.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cfitsio/c287787ea3432b806844ccb7571d6b8e3cd4a7ef
