#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (incomplete dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Command to Read a subunit file or stream and put the data in a SQL DB
Summary(pl.UTF-8):	Polecenie do odczytu plików lub strumieni subunit i umieszczania danych w SQL DB
Name:		python-subunit2sql
Version:	1.10.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/subunit2sql/
Source0:	https://files.pythonhosted.org/packages/source/s/subunit2sql/subunit2sql-%{version}.tar.gz
# Source0-md5:	59133f07a86b1f805e5d9c53f750c456
URL:		https://pypi.org/project/subunit2sql/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-pbr >= 3.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyMySQL
BuildRequires:	python-alembic >= 0.8.10
BuildRequires:	python-dateutil >= 2.4.2
BuildRequires:	python-fixtures >= 0.3.14
BuildRequires:	python-mock >= 1.0
BuildRequires:	python-oslo.concurrency >= 3.5.0
BuildRequires:	python-oslo.config >= 4.0.0
BuildRequires:	python-oslo.db >= 4.24.0
BuildRequires:	python-psycopg2
BuildRequires:	python-six >= 1.9.0
BuildRequires:	python-sqlalchemy >= 1.1.9
BuildRequires:	python-stevedore >= 1.20.0
BuildRequires:	python-stestr >= 1.0.0
BuildRequires:	python-subunit >= 0.0.18
BuildRequires:	python-testresources >= 0.2.4
BuildRequires:	python-testscenarios >= 0.4
BuildRequires:	python-testtools >= 0.9.34
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyMySQL
BuildRequires:	python3-alembic >= 0.8.10
BuildRequires:	python3-dateutil >= 2.4.2
BuildRequires:	python3-fixtures >= 0.3.14
BuildRequires:	python3-oslo.concurrency >= 3.5.0
BuildRequires:	python3-oslo.config >= 4.0.0
BuildRequires:	python3-oslo.db >= 4.24.0
BuildRequires:	python3-psycopg2
BuildRequires:	python3-six >= 1.9.0
BuildRequires:	python3-sqlalchemy >= 1.1.9
BuildRequires:	python3-stevedore >= 1.20.0
BuildRequires:	python3-stestr >= 1.0.0
BuildRequires:	python3-subunit >= 0.0.18
BuildRequires:	python3-testresources >= 0.2.4
BuildRequires:	python3-testscenarios >= 0.4
BuildRequires:	python3-testtools >= 0.9.34
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python-openstackdocstheme >= 1.11.0
BuildRequires:	python-reno >= 0.1.1
BuildRequires:	sphinx-pdg-2 >= 1.6.2
%endif
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
subunit2SQL is a tool for storing test results data in a SQL database.
Like it's name implies it was originally designed around converting
subunit streams to data in a SQL database and the packaged utilities
assume a subunit stream as the input format. However, the data model
used for the DB does not preclude using any test result format.
Additionally the analysis tooling built on top of a database is data
format agnostic.

%description -l pl.UTF-8
subunit2SQL to narzędzie do zapisu danych wyników testów w bazie
danych SQL. Zgodnie z nazwą pierwotnie zostało zaprojektowane do
konwersji strumieni subunit na dane w bazie SQL, a załączone narzędzia
oczekują strumienia subunit jako formatu wejściowego. Jednak model
danych używany dla bazy nie wyklucza stosowania dowolnego formatu
wyników testów, a narzędzia analityczne zbudowane w oparciu o bazę
danych są niezależne od formatu.

%package -n python3-subunit2sql
Summary:	Command to Read a subunit file or stream and put the data in a SQL DB
Summary(pl.UTF-8):	Polecenie do odczytu plików lub strumieni subunit i umieszczania danych w SQL DB
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-subunit2sql
subunit2SQL is a tool for storing test results data in a SQL database.
Like it's name implies it was originally designed around converting
subunit streams to data in a SQL database and the packaged utilities
assume a subunit stream as the input format. However, the data model
used for the DB does not preclude using any test result format.
Additionally the analysis tooling built on top of a database is data
format agnostic.

%description -n python3-subunit2sql -l pl.UTF-8
subunit2SQL to narzędzie do zapisu danych wyników testów w bazie
danych SQL. Zgodnie z nazwą pierwotnie zostało zaprojektowane do
konwersji strumieni subunit na dane w bazie SQL, a załączone narzędzia
oczekują strumienia subunit jako formatu wejściowego. Jednak model
danych używany dla bazy nie wyklucza stosowania dowolnego formatu
wyników testów, a narzędzia analityczne zbudowane w oparciu o bazę
danych są niezależne od formatu.

%package apidocs
Summary:	API documentation for Python subunit2sql module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona subunit2sql
Group:		Documentation

%description apidocs
API documentation for Python subunit2sql module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona subunit2sql.

%prep
%setup -q -n subunit2sql-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
stestr run
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
stestr run
%endif
%endif

%if %{with doc}
sphinx-build-2 -b html doc/source doc/build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__mv} $RPM_BUILD_ROOT%{_bindir}/sql2subunit{,-2}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/subunit2sql{,-2}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/subunit2sql-db-manage{,-2}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/subunit2sql-graph{,-2}
%endif

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/sql2subunit{,-3}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/subunit2sql{,-3}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/subunit2sql-db-manage{,-3}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/subunit2sql-graph{,-3}
ln -sf sql2subunit-3 $RPM_BUILD_ROOT%{_bindir}/sql2subunit
ln -sf subunit2sql-3 $RPM_BUILD_ROOT%{_bindir}/subunit2sql
ln -sf subunit2sql-db-manage-3 $RPM_BUILD_ROOT%{_bindir}/subunit2sql-db-manage
ln -sf subunit2sql-graph-3 $RPM_BUILD_ROOT%{_bindir}/subunit2sql-graph
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst RELEASENOTES.rst TODO.rst
%attr(755,root,root) %{_bindir}/sql2subunit-2
%attr(755,root,root) %{_bindir}/subunit2sql-2
%attr(755,root,root) %{_bindir}/subunit2sql-db-manage-2
%attr(755,root,root) %{_bindir}/subunit2sql-graph-2
%{py_sitescriptdir}/subunit2sql
%{py_sitescriptdir}/subunit2sql-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-subunit2sql
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst RELEASENOTES.rst TODO.rst
%attr(755,root,root) %{_bindir}/sql2subunit
%attr(755,root,root) %{_bindir}/sql2subunit-3
%attr(755,root,root) %{_bindir}/subunit2sql
%attr(755,root,root) %{_bindir}/subunit2sql-3
%attr(755,root,root) %{_bindir}/subunit2sql-db-manage
%attr(755,root,root) %{_bindir}/subunit2sql-db-manage-3
%attr(755,root,root) %{_bindir}/subunit2sql-graph
%attr(755,root,root) %{_bindir}/subunit2sql-graph-3
%{py3_sitescriptdir}/subunit2sql
%{py3_sitescriptdir}/subunit2sql-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_images,_static,cli,contributor,reference,user,*.html,*.js}
%endif
