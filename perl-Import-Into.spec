#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Import
%define		pnam	Into
Summary:	Import::Into - import packages into other packages
Summary(pl.UTF-8):	Import::Into - import pakietów do innych pakietów
Name:		perl-Import-Into
Version:	1.002005
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/H/HA/HAARG/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	48bdc7988f5a7d4d06039ccc5c2459e9
URL:		http://search.cpan.org/dist/Import-Into/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Writing exporters is a pain. Some use Exporter, some use
Sub::Exporter, some use Moose::Exporter, some use Exporter::Declare
... and some things are pragmas.

Exporting on someone else's behalf is harder. The exporters don't
provide a consistent API for this, and pragmas need to have their
import method called directly, since they effect the current unit
of compilation.

Import::Into provides global methods to make this painless.

%description -l pl.UTF-8
Pisanie eksporterów boli. Niektórzy używają modułu Exporter, niektórzy
Sub::Exporter, niektórzy Moose::Exporter, niektórzy
Exporter::Declare... a niektóre elementy to pragma.

Eksportowanie w czyimś imieniu jest trudniejsze. Eksportery nie
udostępniają do tego spójnego API, a pragma muszą mieć metodę
importującą wywołaną bezpośrednio, ponieważ wpływają na bieżącą
jednostkę kompilacji.

Import::Into udostępnia globalne metody czyniące to bezbolesnym.

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
%{perl_vendorlib}/Import/Into.pm
%{_mandir}/man3/Import::Into.3pm*
