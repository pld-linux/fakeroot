Summary:	Gives a fake root environment
Summary(pl):	Umo¿liwia uzyskanie ,,podrobione'' ¶rodowisko roota
Name:		fakeroot
Version:	0.4.4
Release:	2
%define		debver 9
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	ftp://ftp.debian.org/debian/pool/main/f/fakeroot/%{name}_%{version}-%{debver}.tar.gz
BuildRequires:	libtool
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is intended to enable something like: fakeroot rpm
--rebuild i.e. to remove the need to become root for a package
build. This is done by setting LD_PRELOAD to a "libfakeroot.so.0.0",
that provides wrappers around chown, chmod, mknod, stat, etc.

If you don't understand any of this, you do not need this!

%description -l pl
Pakiet w zamierzeniu pozwala na wykonanie operacji takich jak:
fakeroot rpm --rebuild by usun±æ potrzebê operowania z u¿ytkownika
root w celu zbudowania pakietu. Fakeroot wykorzystuje LD_PRELOAD,
któr± to zmienn± ustawia na "libfakeroot.so.0.0" - bibliotekê, która
dostarcza w³asne chown, chmod, mknod, stat itp.

Je¶li nie rozumiesz niczego z powy¿szych informacji to nie
potrzebujesz tego pakietu!

%prep
%setup -q -n %{name}

%build
rm missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
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
