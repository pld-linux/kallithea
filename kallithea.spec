# TODO:
# - everything
# - relax python deps?
#
# Conditional build:
%bcond_without	doc		# don't build doc
%bcond_without	tests	# do not perform "make test"

Summary:	Source code management system for Git and Mercurial
Name:		kallithea
Version:	0.3
Release:	0.1
License:	GPL v3
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/K/Kallithea/Kallithea-%{version}.tar.gz
# Source0-md5:	bd65fcc49585a6debf0a9cdca5189a5e
Patch0:		%{name}-build.patch
URL:		https://kallithea-scm.org/
BuildRequires:	docutils
BuildRequires:	python-Beaker = 1.6.4
BuildRequires:	python-Mako <= 1.0.0
BuildRequires:	python-Mako >= 0.9.0
BuildRequires:	python-Paste
BuildRequires:	python-PasteDeploy
BuildRequires:	python-PasteScript
BuildRequires:	python-Pylons <= 1.0.2
BuildRequires:	python-Pylons >= 1.0.0
BuildRequires:	python-Routes = 1.13
BuildRequires:	python-Routes >= 1.13
BuildRequires:	python-SQLAlchemy = 0.7.10
BuildRequires:	python-URLObject = 2.3.4
BuildRequires:	python-WebHelpers = 1.3
BuildRequires:	python-WebOb
BuildRequires:	python-babel <= 1.3
BuildRequires:	python-babel >= 0.9.6
BuildRequires:	python-bcrypt >= 1.1.1
BuildRequires:	python-celery < 2.3
BuildRequires:	python-celery >= 2.2.5
BuildRequires:	python-dateutil <2.0.0
BuildRequires:	python-dateutil >= 1.5.0
BuildRequires:	python-devel
BuildRequires:	python-docutils >= 0.8.1
BuildRequires:	python-dulwich <= 0.9.9
BuildRequires:	python-dulwich >= 0.9.9
BuildRequires:	python-formencode <=1.2.6
BuildRequires:	python-formencode >= 1.2.4
BuildRequires:	python-markdown = 2.2.1
BuildRequires:	python-mercurial < 3.6
BuildRequires:	python-mercurial >= 2.9
BuildRequires:	python-mock
BuildRequires:	python-pygments >= 1.5
BuildRequires:	python-setuptools
BuildRequires:	python-waitress = 0.8.8
BuildRequires:	python-webob <= 1.1.1
BuildRequires:	python-webob >= 1.0.8
BuildRequires:	python-webtest = 1.4.3
BuildRequires:	python-whoosh <= 2.5.7
BuildRequires:	python-whoosh >= 2.4.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Source code management system that supports two leading version
control systems, Mercurial and Git, and has a web interface that is
easy to use for users and admins.

%prep
%setup -q -n Kallithea-%{version}
%patch0 -p1

%build
%{__python} setup.py build %{?with_tests:test}

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py \
	build
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/*.py[co]
%attr(755,root,root) %{py_sitedir}/*.so
%{py_sitedir}/Kallithea-%{version}-py*.egg-info
