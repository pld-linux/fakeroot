Summary:	Gives a fake root environment
Summary(pl):	Umo¿liwia uzyskanie ,,podrobionego'' ¶rodowiska roota
Summary(pt_BR):	Cria um falso ambiente de root
Name:		fakeroot
Version:	0.4.5
Release:	6
%define		debver 2.3
License:	GPL (see COPYING)
Group:		Development/Tools
Source0:	ftp://ftp.debian.org/debian/pool/main/f/fakeroot/%{name}_%{version}-%{debver}.tar.gz
Patch0:		%{name}-ac_fix.patch
Patch1:		%{name}-amfix.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
Requires:	util-linux
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

%description -l pt_BR
Este pacote permite a construção de pacotes por usuários sem
privilégios de root. Isso e' feito utilizando libfakeroot.so com
LD_PRELOAD, que prove implementacoes de getuid, chown, chmod, mknod,
stat e outros, criando um falso ambiente de root.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f --foreign
%configure
%{__make}

gzip -9nf DEBUG AUTHORS COPYING README.fake BUGS debian/changelog

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz debian/*.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/libfakeroot
%attr(755,root,root) %{_libdir}/libfakeroot/lib*so.*
%{_mandir}/man*/*
