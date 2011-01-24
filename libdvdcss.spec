#
# Conditional build:
%bcond_without	static_libs	# don't build static library
%bcond_without	apidocs		# documentation generated with doxygen
#
Summary:	Library to decrypt CSS-encoded DVD
Summary(pl.UTF-8):	Biblioteka do dekodowania DVD zakodowanych CSS
Name:		libdvdcss
Version:	1.2.10
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.videolan.org/pub/videolan/libdvdcss/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7b03a9571c3a85d801330c7772cd69c4
Patch0:		%{name}-doc.patch
URL:		http://www.videolan.org/libdvdcss/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
%if %{with apidocs}
BuildRequires:	doxygen
BuildRequires:	texlive-fonts-cmsuper
BuildRequires:	texlive-fonts-jknappen
BuildRequires:	texlive-latex
BuildRequires:	texlive-latex-extend
BuildRequires:	texlive-latex-psnfss
BuildRequires:	texlive-makeindex
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdcss is a simple library designed for accessing DVDs like a block
device without having to bother about the decryption.

%description -l pl.UTF-8
Biblioteka dostarczająca prosty interfejs pozwalający na dostęp do
zakodowanych płyt DVD.

%package devel
Summary:	libdvdcss library headers
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdvdcss
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
Summary(pl.UTF-8):	Statyczne biblioteki libdvdcss
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This is package with static libdvdcss libraries.

%description static -l pl.UTF-8
Statyczne biblioteki libdvdcss.

%package apidocs
Summary:	libdvdcss API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libdvdcss
Group:		Documentation

%description apidocs
libdvdcss API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libdvdcss.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_apidocs:--disable-doc} \
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
%attr(755,root,root) %{_libdir}/libdvdcss.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdvdcss.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdvdcss.so
%{_libdir}/libdvdcss.la
%{_includedir}/dvdcss
%{_pkgconfigdir}/libdvdcss.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libdvdcss.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%doc doc/html/*
%endif
