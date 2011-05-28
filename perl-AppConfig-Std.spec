%define upstream_name	 AppConfig-Std
%define upstream_version 1.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Subclass of AppConfig that provides standard options
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/AppConfig/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires: perl-AppConfig
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
AppConfig::Std is a Perl module that provides a set of standard configuration
variables and command-line switches. It is implemented as a subclass of
AppConfig; AppConfig provides a general mechanism for handling global
configuration variables.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
