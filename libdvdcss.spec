Summary:	Library to decrypt CSS-encoded DVD
Summary(pl):	Biblioteka do odkodowania DVD-Video
Name:		libdvdcss
Version:	0.0.3.ogle2
Release:	2
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://www.dtek.chalmers.se/groups/dvd/%{name}-%{version}.tar.gz
URL:		http://www.videolan.org/libdvdcss/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdvdcss is a simple library designed for accessing DVDs like a block
device without having to bother about the decryption.

%description -l pl
Biblioteka dostarczaj±ca prosty interfejs do dostÍpu do kodowanych
p≥yt DVD.

%package devel
Summary:	%{name} library headers
Summary(pl):	Pliki nag≥Ûwkowe biblioteki %{name}
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This is the libraries, include files and other resources you can use
to incorporate libdvdcss into applications.

%description devel -l pl
Pliki nag≥Ûwkowe oraz dokumentacja pozwalaj±ca na dodawanie obs≥ugi
CSS w swoich programach.

%package static
Summary:	libdevdread static libraries
Summary(pl):	Statyczne biblioteki do obs≥ugi formatu DVD-Video
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
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
%configure \
	--disable-sdl \
	--disable-gtk \
	--disable-x11 \
	--disable-xvideo

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS TODO ChangeLog

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
%{_includedir}/videolan/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
