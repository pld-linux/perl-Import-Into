#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Import
%define		pnam	Into
%include	/usr/lib/rpm/macros.perl
Summary:	Import::Into - import packages into other packages
#Summary(pl.UTF-8):	
Name:		perl-Import-Into
Version:	1.002000
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/H/HA/HAARG/Import-Into-1.002000.tar.gz
# Source0-md5:	6c51779d26d665d9858a71117d52e8a5
URL:		http://search.cpan.org/dist/Import-Into/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Writing exporters is a pain. Some use Exporter, some use
Sub::Exporter, some use Moose::Exporter, some use Exporter::Declare
... and some things are pragmas.

Exporting on someone else's behalf is harder.  The exporters don't
provide a consistent API for this, and pragmas need to have their
import method called directly, since they effect the current unit
of compilation.

Import::Into provides global methods to make this painless.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Import
%{perl_vendorlib}/Import/*.pm
%{_mandir}/man3/*
