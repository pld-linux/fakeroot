%define name fakeroot
%define version 0.4.4
%define release 1mdk
%define debver 4.1

Summary: Gives a fake root environment
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{version}-%{debver}.tar.bz2
Copyright: GPL
Group: Development/Tools
BuildRoot: /tmp/%{name}-buildroot
Prefix: %{_prefix}

%description
This package is intended to enable something like:
  fakeroot rpm --rebuild
i.e. to remove the need to become root for a package build.
This is done by setting LD_PRELOAD to a "libfakeroot.so.0.0",
that provides wrappers around chown, chmod, mknod, stat,
etc.

If you don't understand any of this, you do not need this!

%prep
%setup

%build
%configure

make    CFLAGS="-g -O2 -Wall -W -pedantic"\
         CXXFLAGS="-g -O2 -Wall -W -pedantic"

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr
make CFLAGS="-g -O2 -Wall -W -pedantic"\
     CXXFLAGS="-g -O2 -Wall -W -pedantic"\
     prefix=$RPM_BUILD_ROOT/usr install
install -d -m 0755 $RPM_BUILD_ROOT/usr/bin/
install -m 0755 scripts/fakeroot $RPM_BUILD_ROOT/usr/bin/
install -d -m 0755 $RPM_BUILD_ROOT/usr/lib/libfakeroot
bzip2 -9f $RPM_BUILD_ROOT/usr/man/man*/*
strip $RPM_BUILD_ROOT/usr/bin/faked
strip $RPM_BUILD_ROOT/usr/lib/libfakeroot/libfakeroot.so.0.0.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
/usr/bin/*
/usr/lib/libfakeroot/*
%doc DEBUG
%doc /usr/man/man*/*

%changelog

* Mon Jan 17 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.4.4-1mdk

- firct mandrake version.

# end of file
