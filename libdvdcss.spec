Summary:	Library to decrypt CSS-encoded DVD
Summary(pl):	Biblioteka do odkodowania DVD-Video
Name:		libdvdcss
Version:	1.1.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://www.videolan.org/pub/videolan/libdvdcss/1.1.0/%{name}-%{version}.tar.gz
URL:		http://www.videolan.org/libdvdcss/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdcss is a simple library designed for accessing DVDs like a block
device without having to bother about the decryption.

%description -l pl
Biblioteka dostarczaj±ca prosty interfejs do dostêpu do kodowanych
p³yt DVD.

%package devel
Summary:	%{name} library headers
Summary(pl):	Pliki nag³ówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdvdcss into applications.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja pozwalaj±ca na dodawanie obs³ugi
CSS w swoich programach.

%package static
Summary:	libdevdread static libraries
Summary(pl):	Statyczne biblioteki do obs³ugi formatu DVD-Video
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This is package with static libdvdcss libraries.

%description static -l pl
Statyczne biblioteki libdvdcss.

%prep
%setup -q

%build
aclocal
autoconf
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install src/*.h $RPM_BUILD_ROOT/%{_includedir}/dvdcss
gzip -9nf README AUTHORS ChangeLog

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/dvdcss

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
