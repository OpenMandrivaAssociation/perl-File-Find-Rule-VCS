%define realname   File-Find-Rule-VCS
%define version    1.04
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Exclude files/directories for Version Control Systems
Source:     http://www.cpan.org/modules/by-module/File/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
Many tools need to be equally useful both on ordinary files, and on code
that has been checked out from revision control systems.

*File::Find::Rule::VCS* provides quick and convenient methods to exclude
the version control directories of several major Version Control Systems
(currently CVS, subversion, and Bazaar).

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*
