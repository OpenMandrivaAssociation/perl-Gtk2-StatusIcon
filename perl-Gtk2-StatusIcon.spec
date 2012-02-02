%define	module	Gtk2-StatusIcon
%define	fmodule	Gtk2/StatusIcon

Summary:	Perl module interface to the EggSystemTray library
Name:		perl-%{module}
Version:	0.010
Release:	9
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Source0:	%{module}-%{version}.tar.bz2
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtkspell-devel perl-ExtUtils-Depends perl-Gtk2 perl-Gnome2 >= 1.020-2mdk
BuildRequires:	perl-Glib > 1.00 perl-ExtUtils-PkgConfig 
BuildRequires:	gnomeui2-devel
Buildrequires:	perl-devel
BuildRequires:	glitz-devel
Requires:	perl-Gnome2 >= 1.020-2mdk


%description
This module allows a Perl developer to embed an arbitrary widget in a
System Tray like the Gnome notification area.


%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc NEWS examples/*
%{_mandir}/*/*
%{perl_vendorarch}/%{fmodule}*
%{perl_vendorarch}/%{fmodule}.pm
%{perl_vendorarch}/auto/%{fmodule}
