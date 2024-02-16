#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
Name     : qt6networkauth
Version  : 6.6.2
Release  : 12
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtnetworkauth-everywhere-src-6.6.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtnetworkauth-everywhere-src-6.6.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-3.0
Requires: qt6networkauth-lib = %{version}-%{release}
Requires: qt6networkauth-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
BuildRequires : qtbase-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package dev
Summary: dev components for the qt6networkauth package.
Group: Development
Requires: qt6networkauth-lib = %{version}-%{release}
Provides: qt6networkauth-devel = %{version}-%{release}
Requires: qt6networkauth = %{version}-%{release}

%description dev
dev components for the qt6networkauth package.


%package lib
Summary: lib components for the qt6networkauth package.
Group: Libraries
Requires: qt6networkauth-license = %{version}-%{release}

%description lib
lib components for the qt6networkauth package.


%package license
Summary: license components for the qt6networkauth package.
Group: Default

%description license
license components for the qt6networkauth package.


%prep
%setup -q -n qtnetworkauth-everywhere-src-6.6.2
cd %{_builddir}/qtnetworkauth-everywhere-src-6.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1708116854
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1708116854
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6networkauth
cp %{_builddir}/qtnetworkauth-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6networkauth/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtnetworkauth-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6networkauth/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtnetworkauth-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6networkauth/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6networkauth_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_networkauth.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_networkauth_private.pri
/usr/lib64/qt6/modules/NetworkAuth.json

%files dev
%defattr(-,root,root,-)
/usr/include/QtNetworkAuth/6.6.2/QtNetworkAuth/private/qabstractoauth2_p.h
/usr/include/QtNetworkAuth/6.6.2/QtNetworkAuth/private/qabstractoauth_p.h
/usr/include/QtNetworkAuth/6.6.2/QtNetworkAuth/private/qabstractoauthreplyhandler_p.h
/usr/include/QtNetworkAuth/6.6.2/QtNetworkAuth/private/qoauth1_p.h
/usr/include/QtNetworkAuth/6.6.2/QtNetworkAuth/private/qoauth1signature_p.h
/usr/include/QtNetworkAuth/6.6.2/QtNetworkAuth/private/qoauth2authorizationcodeflow_p.h
/usr/include/QtNetworkAuth/6.6.2/QtNetworkAuth/private/qoauthhttpserverreplyhandler_p.h
/usr/include/QtNetworkAuth/QAbstractOAuth
/usr/include/QtNetworkAuth/QAbstractOAuth2
/usr/include/QtNetworkAuth/QAbstractOAuthReplyHandler
/usr/include/QtNetworkAuth/QOAuth1
/usr/include/QtNetworkAuth/QOAuth1Signature
/usr/include/QtNetworkAuth/QOAuth2AuthorizationCodeFlow
/usr/include/QtNetworkAuth/QOAuthHttpServerReplyHandler
/usr/include/QtNetworkAuth/QOAuthOobReplyHandler
/usr/include/QtNetworkAuth/QtNetworkAuth
/usr/include/QtNetworkAuth/QtNetworkAuthDepends
/usr/include/QtNetworkAuth/QtNetworkAuthVersion
/usr/include/QtNetworkAuth/qabstractoauth.h
/usr/include/QtNetworkAuth/qabstractoauth2.h
/usr/include/QtNetworkAuth/qabstractoauthreplyhandler.h
/usr/include/QtNetworkAuth/qoauth1.h
/usr/include/QtNetworkAuth/qoauth1signature.h
/usr/include/QtNetworkAuth/qoauth2authorizationcodeflow.h
/usr/include/QtNetworkAuth/qoauthglobal.h
/usr/include/QtNetworkAuth/qoauthhttpserverreplyhandler.h
/usr/include/QtNetworkAuth/qoauthoobreplyhandler.h
/usr/include/QtNetworkAuth/qtnetworkauthversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtNetworkAuthTestsConfig.cmake
/usr/lib64/cmake/Qt6NetworkAuth/Qt6NetworkAuthAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6NetworkAuth/Qt6NetworkAuthConfig.cmake
/usr/lib64/cmake/Qt6NetworkAuth/Qt6NetworkAuthConfigVersion.cmake
/usr/lib64/cmake/Qt6NetworkAuth/Qt6NetworkAuthConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6NetworkAuth/Qt6NetworkAuthDependencies.cmake
/usr/lib64/cmake/Qt6NetworkAuth/Qt6NetworkAuthTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6NetworkAuth/Qt6NetworkAuthTargets.cmake
/usr/lib64/cmake/Qt6NetworkAuth/Qt6NetworkAuthVersionlessTargets.cmake
/usr/lib64/libQt6NetworkAuth.prl
/usr/lib64/libQt6NetworkAuth.so
/usr/lib64/pkgconfig/Qt6NetworkAuth.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6NetworkAuth.so.6.6.2
/usr/lib64/libQt6NetworkAuth.so.6
/usr/lib64/libQt6NetworkAuth.so.6.6.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6networkauth/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6networkauth/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6networkauth/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
