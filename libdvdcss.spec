#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library to decrypt CSS-encoded DVD
Summary(pl.UTF-8):   Biblioteka do dekodowania DVD zakodowanych CSS
Name:		libdvdcss
Version:	1.2.9
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.videolan.org/pub/videolan/libdvdcss/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bec67a57436a7f80c5aeb3c3abccbd9e
URL:		http://www.videolan.org/libdvdcss/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	tetex-makeindex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdcss is a simple library designed for accessing DVDs like a block
device without having to bother about the decryption.

%description -l pl.UTF-8
Biblioteka dostarczająca prosty interfejs pozwalający na dostęp do
zakodowanych płyt DVD.

%package devel
Summary:	libdvdcss library headers
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libdvdcss
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdvdcss into applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja pozwalająca na dodawanie obsługi
CSS w swoich programach.

%package static
Summary:	libdvdcss static libraries
Summary(pl.UTF-8):   Statyczne biblioteki libdvdcss
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static libdvdcss libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libdvdcss.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/*.h $RPM_BUILD_ROOT%{_includedir}/dvdcss

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/dvdcss

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
