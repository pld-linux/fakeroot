Summary:	Gives a fake root environment
Name:		fakeroot
Version:	0.4.4
Release:	1
%define		debver 9
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	ftp://ftp.debian.org/debian/pool/main/f/fakeroot/%{name}_%{version}-%{debver}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is intended to enable something like: fakeroot rpm
--rebuild i.e. to remove the need to become root for a package
build. This is done by setting LD_PRELOAD to a "libfakeroot.so.0.0",
that provides wrappers around chown, chmod, mknod, stat, etc.

If you don't understand any of this, you do not need this!

%prep
%setup -q -n %{name}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf DEBUG

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/libfakeroot
%attr(755,root,root) %{_libdir}/libfakeroot/lib*so.*
%{_mandir}/man*/*
