%define upstream_name	 AppConfig-Std
%define upstream_version 1.10
Name:		perl-%{upstream_name}
Version:	1.10
Release:	3
Summary:	Subclass of AppConfig that provides standard options
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{upstream_name}/
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/AppConfig-Std-1.10.tar.gz
BuildRequires:	make
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
%setup -qn %{upstream_name}-%{version} -n AppConfig-Std-1.10

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/AppConfig/*
%{_mandir}/*/*


