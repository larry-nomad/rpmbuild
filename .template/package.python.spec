%define debug_package %{nil}
%global __os_install_post %{nil}

%define pkg_name pyasn1
%define pkg_version 0.1.4
%define pkg_unmangled_version %{version}
%define pkg_release 1

Name:		q-python27-%{pkg_name}
Version:	%{pkg_version}
Release:	%{pkg_release}%{?dist}
Summary:	
Packager:	zhen.pei

Group:		Qunar/Language
License:	
URL:		
Source0:	%{pkg_name}-%{pkg_version}.tar.gz
BuildArch:	noarch

Requires:	q-python27
Requires:	q-python27-setuptools
AutoReqProv:	no

%description


%prep
%setup -q -n %{pkg_name}-%{pkg_version}


%build
q-python27 setup.py build

%install
q-python27 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES


%clean
rm -rf $RPM_BUILD_ROOT

%files

# bin
%defattr(0755,root,root,0755)

# others
%defattr(0644,root,root,0755)
/home/q/python27/lib/python2.7/site-packages/*

# config
%defattr(0644,root,root,0755)
%config(noreplace)

# doc
%defattr(0644,root,root,0755)



%changelog

