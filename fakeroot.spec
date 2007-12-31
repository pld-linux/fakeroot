Summary:	Gives a fake root environment
Summary(pl.UTF-8):	Umożliwia uzyskanie ,,podrobionego'' środowiska roota
Summary(pt_BR.UTF-8):	Cria um falso ambiente de root
Name:		fakeroot
Version:	1.8.10
Release:	1
License:	GPL (see COPYING)
Group:		Development/Tools
Source0:	ftp://ftp.debian.org/debian/pool/main/f/fakeroot/%{name}_%{version}.tar.gz
# Source0-md5:	5ca6dab46ac7e1617edd71f8bb2ed4be
#BuildRequires:	autoconf >= 2.59
#BuildRequires:	automake
#BuildRequires:	libtool >= 2.0
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

%description -l pl.UTF-8
Program fakeroot uruchamia polecenia w środowisku, gdzie wydaje im
się, że mają uprawnienia roota przy operacjach na plikach. Jest to
przydatne, aby umożliwić użytkownikom na tworzenie archiwów (tar, ar,
deb) z plikami mającymi będącymi własnością roota. Bez fakeroota do
tworzenia takich plików z właściwymi uprawnieniami potrzebne byłyby
uprawnienia roota lub bezpośrednie tworzenie archiwów bez użycia
normalnego archiwizera.

fakeroot działa poprzez podmianę funkcji bibliotecznych operujących na
plikach (chmod(), stat() itp.) na takie, które symulują efekt
prawdziwych funkcji gdyby były uruchamiane z uprawnieniami roota. Te
specjalne funkcje znajdują się w bibliotece dzielonej libfakeroot.so*
ładowanej poprzez mechanizm LD_PRELOAD.

%description -l pt_BR.UTF-8
Este pacote permite a construção de pacotes por usuários sem
privilégios de root. Isso e' feito utilizando libfakeroot.so com
LD_PRELOAD, que prove implementacoes de getuid, chown, chmod, mknod,
stat e outros, criando um falso ambiente de root.

%prep
%setup -q

%build
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
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
%doc AUTHORS BUGS COPYING DEBUG debian/changelog
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}
%attr(755,root,root) %{_libdir}/libfakeroot*.so
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(nl) %{_mandir}/nl/man1/*
%lang(sv) %{_mandir}/sv/man1/*
