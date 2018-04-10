#
# Conditional build:
%bcond_without	python2	# CPython 2.x binding
%bcond_without	python3	# CPython 3.x binding

Summary:	Python 2 binding for the ALSA library
Summary(pl.UTF-8):	Wiązanie Pythona 2 do biblioteki ALSA
Name:		python-pyalsa
Version:	1.1.6
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	ftp://ftp.alsa-project.org/pub/pyalsa/pyalsa-%{version}.tar.bz2
# Source0-md5:	6a275707288af52d1d9e1856d6efaadc
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.29
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	alsa-lib >= 1.0.29
Requires:	python-libs >= 1:2.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 binding for the ALSA library.

%description -l pl.UTF-8
Wiązanie Pythona 2 do biblioteki ALSA.

%package -n python3-pyalsa
Summary:	Python 3 binding for the ALSA library
Summary(pl.UTF-8):	Wiązanie Pythona 3 do biblioteki ALSA
Group:		Libraries/Python
Requires:	alsa-lib >= 1.0.29
Requires:	python3-libs >= 1:3.2

%description -n python3-pyalsa
Python 3 binding for the ALSA library.

%description -n python3-pyalsa -l pl.UTF-8
Wiązanie Pythona 3 do biblioteki ALSA.

%prep
%setup -q -n pyalsa-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/pyalsa
%attr(755,root,root) %{py_sitedir}/pyalsa/alsa*.so
%{py_sitedir}/pyalsa/__init__.py[co]
%{py_sitedir}/pyalsa-%{version}-*.egg-info
%endif

%if %{with python3}
%files -n python3-pyalsa
%defattr(644,root,root,755)
%dir %{py3_sitedir}/pyalsa
%attr(755,root,root) %{py3_sitedir}/pyalsa/alsa*.cpython-*.so
%{py3_sitedir}/pyalsa/__init__.py
%{py3_sitedir}/pyalsa/__pycache__
%{py3_sitedir}/pyalsa-%{version}-py*.egg-info
%endif
