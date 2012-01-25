%define module Gtk2-StatusIcon
%define fmodule Gtk2/StatusIcon

Summary: Perl module interface to the EggSystemTray library
Name:    perl-%module
Version: 0.010
Release:	9
License: GPL or Artistic
Group:   Development/GNOME and GTK+
Source:  %module-%version.tar.bz2
URL: http://gtk2-perl.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtkspell-devel perl-ExtUtils-Depends perl-Gtk2 perl-Gnome2 >= 1.020-2mdk
BuildRequires: perl-Glib > 1.00 perl-ExtUtils-PkgConfig 
BuildRequires: gnomeui2-devel
Buildrequires: perl-devel
BuildRequires: glitz-devel
Requires: perl-Gnome2 >= 1.020-2mdk

Requires: gtk+2

%description
This module allows a Perl developer to embed an arbitrary widget in a
System Tray like the Gnome notification area.


%prep
%setup -q -n %module-%version
find -type d -name CVS | rm -rf 

%build
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Os -s"
perl Makefile.PL INSTALLDIRS=vendor
make OPTIMIZE="$RPM_OPT_FLAGS"
#%make test || :

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root)
%doc NEWS examples/*
%{_mandir}/*/*
%{perl_vendorarch}/%{fmodule}*
%{perl_vendorarch}/%fmodule.pm
%{perl_vendorarch}/auto/%fmodule

