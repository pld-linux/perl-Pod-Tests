#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Pod
%define		pnam	Tests
Summary:	Pod::Tests - Extracts embedded tests and code examples from POD
Summary(pl.UTF-8):	Pod::Tests - wydobywanie osadzonych testów i przykładowego kodu z POD
Name:		perl-Pod-Tests
Version:	1.20
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Pod/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5f1c6b7423f660869323396176619fd8
URL:		https://metacpan.org/release/Pod-Tests
BuildRequires:	perl-ExtUtils-MakeMaker
%if %{with tests}
BuildRequires:	perl-Test-Harness >= 1.22
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a specialized POD viewer to extract embedded tests and code
examples from POD. It doesn't do much more than that. pod2test does
the useful work.

%description -l pl.UTF-8
Ten pakiet jest specjalizowaną przeglądarką POD służącą do wyciągania
osadzonych testów i przykładowego kodu z dokumentacji w formacie POD.
Robi niewiele więcej. pod2test wykonuje przydatną czynność.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/pod2test
%{perl_vendorlib}/Pod/Tests.pm
%{_mandir}/man1/pod2test.1p*
%{_mandir}/man3/Pod::Tests.3pm*
