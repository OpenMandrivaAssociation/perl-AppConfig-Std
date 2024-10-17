%define upstream_name	 AppConfig-Std
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Summary:	Subclass of AppConfig that provides standard options
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/N/NE/NEILB/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(AppConfig)
BuildRequires:	perl(Pod::Usage)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(warnings)

BuildArch:	noarch

%description
AppConfig::Std is a Perl module that provides a set of standard configuration
variables and command-line switches. It is implemented as a subclass of
AppConfig; AppConfig provides a general mechanism for handling global
configuration variables.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/AppConfig/*
%{_mandir}/*/*


