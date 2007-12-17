%define module	AppConfig-Std
%define name	perl-%{module}
%define version 1.07
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Subclass of AppConfig that provides standard options
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/AppConfig/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
BuildArch:	noarch
BuildRequires:	perl-devel perl-AppConfig

%description
AppConfig::Std is a Perl module that provides a set of standard configuration
variables and command-line switches. It is implemented as a subclass of
AppConfig; AppConfig provides a general mechanism for handling global
configuration variables.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog README
%{perl_vendorlib}/AppConfig/*
%{_mandir}/*/*



