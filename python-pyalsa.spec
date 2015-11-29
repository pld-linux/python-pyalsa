Summary:	Python binding for the ALSA library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki ALSA
Name:		python-pyalsa
Version:	1.0.29
Release:	2
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	ftp://ftp.alsa-project.org/pub/pyalsa/pyalsa-%{version}.tar.bz2
# Source0-md5:	98bea57c789f73fff54a6d1940b73ede
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.29
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-libs
Requires:	alsa-lib >= 1.0.29
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python binding for the ALSA library.

%description -l pl.UTF-8
Wiązanie Pythona do biblioteki ALSA.

%prep
%setup -q -n pyalsa-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/pyalsa
%attr(755,root,root) %{py_sitedir}/pyalsa/alsa*.so
%{py_sitedir}/pyalsa/__init__.py[co]
%{py_sitedir}/pyalsa-*.egg-info
