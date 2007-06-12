Summary:	Python binding for the ALSA library
Summary(pl.UTF-8):	Wiązanie Pythona do biblioteki ALSA
Name:		python-pyalsa
Version:	1.0.14
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	ftp://ftp.alsa-project.org/pub/pyalsa/pyalsa-%{version}.tar.bz2
# Source0-md5:	cc9460605d6af59dbb494ddd3235763f
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.14
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	alsa-lib >= 1.0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python binding for the ALSA library.

%description -l pl.UTF-8
Wiązanie Pythona do biblioteki ALSA.

%prep
%setup -q -n pyalsa-%{version}

%build
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build
	
%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitedir}/pyalsa
%attr(755,root,root) %{py_sitedir}/pyalsa/alsa*.so
%{py_sitedir}/pyalsa/__init__.py[co]
%{py_sitedir}/pyalsa-*.egg-info