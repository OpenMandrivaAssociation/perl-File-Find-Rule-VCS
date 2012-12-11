%define upstream_name    File-Find-Rule-VCS
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Exclude files/directories for Version Control Systems
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
Many tools need to be equally useful both on ordinary files, and on code
that has been checked out from revision control systems.

*File::Find::Rule::VCS* provides quick and convenient methods to exclude
the version control directories of several major Version Control Systems
(currently CVS, subversion, and Bazaar).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.80.0-2mdv2011.0
+ Revision: 656914
- rebuild for updated spec-helper

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 595969
- update to new version 1.08

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2011.0
+ Revision: 553127
- update to 1.07

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.0
+ Revision: 401664
- rebuild using %%perl_convert_version
- fixed license field

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2010.0
+ Revision: 393792
- update to new version 1.06

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2009.1
+ Revision: 292160
- update to new version 1.05

* Sat Aug 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.04-1mdv2009.0
+ Revision: 277660
- import perl-File-Find-Rule-VCS


