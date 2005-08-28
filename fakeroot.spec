Summary:	Gives a fake root environment
Summary(pl):	Umo¿liwia uzyskanie ,,podrobionego'' ¶rodowiska roota
Summary(pt_BR):	Cria um falso ambiente de root
Name:		fakeroot
Version:	1.4.3
Release:	1
License:	GPL (see COPYING)
Group:		Development/Tools
Source0:	ftp://ftp.debian.org/debian/pool/main/f/fakeroot/%{name}_%{version}.tar.gz
# Source0-md5:	bf9cd1d9b98adcf1a94741fc2db0442e
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
Requires:	util-linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{_prefix}/%{_lib}/libfakeroot

%description
fakeroot runs a command in an environment were it appears to have root
privileges for file manipulation. This is useful for allowing users to
create archives (tar, ar, .deb etc.) with files in them with root
permissions/ownership. Without fakeroot one would have to have root
privileges to create the constituent files of the archives with the
correct permissions and ownership, and then pack them up, or one would
have to construct the archives directly, without using the archiver.

fakeroot works by replacing the file manipulation library functions
(chmod(), stat() etc.) by ones that simulate the effect the real
library functions would have had, had the user really been root. These
wrapper functions are in a shared library libfakeroot.so*, which is
loaded through the LD_PRELOAD mechanism of the dynamic loader.

%description -l pl
Program fakeroot uruchamia polecenia w ¶rodowisku, gdzie wydaje im
siê, ¿e maj± uprawnienia roota przy operacjach na plikach. Jest to
przydatne, aby umo¿liwiæ u¿ytkownikom na tworzenie archiwów (tar, ar,
deb) z plikami maj±cymi bêd±cymi w³asno¶ci± roota. Bez fakeroota do
tworzenia takich plików z w³a¶ciwymi uprawnieniami potrzebne by³yby
uprawnienia roota lub bezpo¶rednie tworzenie archiwów bez u¿ycia
normalnego archiwizera.

fakeroot dzia³a poprzez podmianê funkcji bibliotecznych operuj±cych na
plikach (chmod(), stat() itp.) na takie, które symuluj± efekt
prawdziwych funkcji gdyby by³y uruchamiane z uprawnieniami roota. Te
specjalne funkcje znajduj± siê w bibliotece dzielonej libfakeroot.so*
³adowanej poprzez mechanizm LD_PRELOAD.

%description -l pt_BR
Este pacote permite a construção de pacotes por usuários sem
privilégios de root. Isso e' feito utilizando libfakeroot.so com
LD_PRELOAD, que prove implementacoes de getuid, chown, chmod, mknod,
stat e outros, criando um falso ambiente de root.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/libfakeroot.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING DEBUG README.fake debian/changelog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}
%attr(755,root,root) %{_libdir}/libfakeroot.so.*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(sv) %{_mandir}/sv/man1/*
