#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : myst-nb
Version  : 0.13.1
Release  : 2
URL      : https://files.pythonhosted.org/packages/bc/5e/e641325a33d07cef3a1a0428a163ac95c5dbc0424c597becac38f1445cd9/myst-nb-0.13.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/bc/5e/e641325a33d07cef3a1a0428a163ac95c5dbc0424c597becac38f1445cd9/myst-nb-0.13.1.tar.gz
Summary  : A Jupyter Notebook Sphinx reader built on top of the MyST markdown parser.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: myst-nb-license = %{version}-%{release}
Requires: myst-nb-python = %{version}-%{release}
Requires: myst-nb-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(alabaster)
BuildRequires : pypi(bokeh)
BuildRequires : pypi(coverage)
BuildRequires : pypi(docutils)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(ipython)
BuildRequires : pypi(ipywidgets)
BuildRequires : pypi(matplotlib)
BuildRequires : pypi(nbconvert)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pandas)
BuildRequires : pypi(plotly)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinx_copybutton)
BuildRequires : pypi(sympy)
BuildRequires : pypi(wheel)

%description
[![Github-CI][github-ci]][github-link]
        [![Coverage Status][codecov-badge]][codecov-link]
        [![Documentation Status][rtd-badge]][rtd-link]
        [![PyPI][pypi-badge]][pypi-link]
        [![Conda Version][conda-badge]][conda-link]
        
        A collection of tools for working with Jupyter Notebooks in Sphinx.
        
        The primary tool this package provides is a Sphinx parser for `ipynb` files.
        This allows you to directly convert Jupyter Notebooks into Sphinx documents.

%package license
Summary: license components for the myst-nb package.
Group: Default

%description license
license components for the myst-nb package.


%package python
Summary: python components for the myst-nb package.
Group: Default
Requires: myst-nb-python3 = %{version}-%{release}

%description python
python components for the myst-nb package.


%package python3
Summary: python3 components for the myst-nb package.
Group: Default
Requires: python3-core
Provides: pypi(myst_nb)
Requires: pypi(docutils)
Requires: pypi(importlib_metadata)
Requires: pypi(ipython)
Requires: pypi(ipywidgets)
Requires: pypi(jupyter_cache)
Requires: pypi(jupyter_sphinx)
Requires: pypi(myst_parser)
Requires: pypi(nbconvert)
Requires: pypi(nbformat)
Requires: pypi(pyyaml)
Requires: pypi(sphinx)
Requires: pypi(sphinx_togglebutton)

%description python3
python3 components for the myst-nb package.


%prep
%setup -q -n myst-nb-0.13.1
cd %{_builddir}/myst-nb-0.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637342824
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/myst-nb
cp %{_builddir}/myst-nb-0.13.1/LICENSE %{buildroot}/usr/share/package-licenses/myst-nb/f6901900cf039247901977f1db5534db7b54141b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/myst-nb/f6901900cf039247901977f1db5534db7b54141b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
