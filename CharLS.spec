Summary:	An optimized implementation of the JPEG-LS standard
Summary(pl.UTF-8):	Zoptymalizowana implementacja standardu JPEG-LS
Name:		CharLS
Version:	1.0
Release:	2
License:	BSD
Group:		Libraries
# to download, open this URL in fully JS-capable browser (elinks doesn't suffice)
# and manually accept BSD(!) license
#Source0Download: http://charls.codeplex.com/releases/view/55406
Source0:	%{name}-source-%{version}.zip
# Source0-md5:	4694f02fbe2c4e1897ff2188d6e3cefc
Patch0:		%{name}-add_cmake_install_target.patch
Patch1:		%{name}-add_sharedlib_soname.patch
Patch2:		%{name}-fix_tests.patch
URL:		http://charls.codeplex.com/
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An optimized implementation of the JPEG-LS standard for loss less and
near loss less image compression. JPEG-LS is a low-complexity standard
that matches JPEG 2000 compression ratios. In terms of speed, CharLS
outperforms open source and commercial JPEG LS implementations.

%description -l pl.UTF-8
Zoptymalizowana implementacja standardu JPEG-LS bezstratnej i prawie
bezstratnej kompresji obrazu. JPEG-LS to mało skomplikowany standard
osiągający współczynniki kompresji standardu JPEG 2000. Pod względem
szybkości CharLS jest wydajniejszy niż inne implementacje JPEG LS o
otwartych źródłach, a także komercyjne.

%package devel
Summary:	Header files for CharLS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CharLS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for CharLS library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CharLS.

%prep
%setup -q -c

%undos CMakeLists.txt defaulttraits.h

%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake . \
	-Dcharls_BUILD_SHARED_LIBS=ON \
	-DBUILD_TESTING=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc License.txt
%attr(755,root,root) %{_libdir}/libCharLS.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libCharLS.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCharLS.so
%{_includedir}/CharLS
