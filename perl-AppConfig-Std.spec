%define upstream_name	 AppConfig-Std
%define upstream_version 1.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Subclass of AppConfig that provides standard options
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/AppConfig/AppConfig-Std-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-AppConfig
BuildArch:	noarch

%description
AppConfig::Std is a Perl module that provides a set of standard configuration
variables and command-line switches. It is implemented as a subclass of
AppConfig; AppConfig provides a general mechanism for handling global
configuration variables.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/AppConfig/*
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.70.0-2mdv2011.0
+ Revision: 680473
- mass rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 406834
- rebuild using %%perl_convert_version

* Mon Sep 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.07-5mdv2009.0
+ Revision: 289343
- restore the spec file

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-4mdv2008.1
+ Revision: 136885
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 1.07-3mdv2007.0
+ Revision: 73279
- import perl-AppConfig-Std-1.07-3mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.07-3mdk
- Fix SPEC according to Perl Policy
	- Source URL
- use mkrel

* Mon Nov 01 2004 Michael Scherer <misc@mandrake.org> 1.07-2mdk
- BuildRequires

* Thu Sep 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.07-1mdk
- Initial MDK release.



