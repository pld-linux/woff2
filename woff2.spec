Summary:	Reference font compression library
Summary(pl.UTF-8):	Referencyjna biblioteka kompresji fontów
Name:		woff2
Version:	1.0.2
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/google/woff2/releases
Source0:	https://github.com/google/woff2/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	793c8844845351cb80730a74937e411b
URL:		https://github.com/google/woff2
BuildRequires:	cmake >= 2.8.6
BuildRequires:	libbrotli-devel >= 1.0.0
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Reference font compression library using brotli algorithm.

%description -l pl.UTF-8
Referencyjna biblioteka kompresji fontów, korzystająca z algorytmu
brotli.

%package devel
Summary:	Header files for woff2 libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek woff2
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbrotli-devel >= 1.0.0
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for woff2 libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek woff2.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libwoff2common.so.*.*.*
%attr(755,root,root) %{_libdir}/libwoff2dec.so.*.*.*
%attr(755,root,root) %{_libdir}/libwoff2enc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwoff2common.so
%attr(755,root,root) %{_libdir}/libwoff2dec.so
%attr(755,root,root) %{_libdir}/libwoff2enc.so
%{_includedir}/woff2
%{_pkgconfigdir}/libwoff2common.pc
%{_pkgconfigdir}/libwoff2dec.pc
%{_pkgconfigdir}/libwoff2enc.pc
