%define	module	Gtk2-StatusIcon
%define	fmodule	Gtk2/StatusIcon

Summary:	Perl module interface to the EggSystemTray library
Name:		perl-%{module}
Version:	0.010
Release:	10
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Source0:	%{module}-%{version}.tar.bz2
URL:		http://gtk2-perl.sf.net/
BuildRequires:	gtkspell-devel perl-ExtUtils-Depends perl-Gtk2 perl-Gnome2 >= 1.020-2mdk
BuildRequires:	perl-Glib > 1.00 perl-ExtUtils-PkgConfig 
BuildRequires:	pkgconfig(libgnomeui-2.0)
Buildrequires:	perl-devel
BuildRequires:	pkgconfig(glitz)
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
%{perl_vendorarch}/%{fmodule}.pm
%{perl_vendorarch}/%{fmodule}
%{perl_vendorarch}/auto/%{fmodule}


%changelog
* Thu Feb 02 2012 Per Ã˜yvind Karlsen <peroyvind@mandriva.org> 0.010-9
+ Revision: 770584
- use pkgconfig() deps
- fix files listed multiple times
- clean up spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.010-8mdv2011.0
+ Revision: 430464
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.010-7mdv2009.0
+ Revision: 257185
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.010-5mdv2008.1
+ Revision: 152115
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Jun 22 2007 Thierry Vignaud <tv@mandriva.org> 0.010-4mdv2008.0
+ Revision: 43101
- rebuild


* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.010-3mdk
- Add another buildRequires

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.010-2mdk
- Fix BuildRequires

* Tue Feb 08 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.010-1mdk
- initial release

