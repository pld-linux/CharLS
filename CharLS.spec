# NOTE: for >= 2.0.0 (C++14 based) see DEVEL branch
Summary:	An optimized implementation of the JPEG-LS standard
Summary(pl.UTF-8):	Zoptymalizowana implementacja standardu JPEG-LS
Name:		CharLS
Version:	1.1.0
Release:	3
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/team-charls/charls/releases
Source0:	https://github.com/team-charls/charls/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ea02f65abd33aa46830dedec8f4c52f5
URL:		https://github.com/team-charls/charls
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
%setup -q -n charls-%{version}

%build
%cmake . \
	-DBUILD_TESTING=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# the most important header file is missing from make install...
test ! -f $RPM_BUILD_ROOT%{_includedir}/CharLS/interface.h
cp -p src/interface.h $RPM_BUILD_ROOT%{_includedir}/CharLS

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md src/License.txt
%attr(755,root,root) %{_libdir}/libCharLS.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libCharLS.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libCharLS.so
%{_includedir}/CharLS
