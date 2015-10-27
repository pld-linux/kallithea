# TODO: everything
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
BuildRequires:	mercurial >= 2.9
BuildRequires:	python-Paste
BuildRequires:	python-PasteDeploy
BuildRequires:	python-PasteScript
BuildRequires:	python-Routes >= 1.13
BuildRequires:	python-WebOb
BuildRequires:	python-bcrypt >= 1.1.1
BuildRequires:	python-devel
BuildRequires:	python-dulwich
BuildRequires:	python-setuptools
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
