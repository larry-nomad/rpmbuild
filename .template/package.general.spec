%define debug_package %{nil}
%global __os_install_post %{nil}

%define pkg_name nload
%define pkg_version 0.7.4
%define pkg_release 1

Name:		q-%{pkg_name}
Version:	%{pkg_version}
Release:	%{pkg_release}%{?dist}
Summary:	
Packager:	zhen.pei

Group:		Qunar/
License:	Unknown
URL:		
Source0:	%{pkg_name}-%{pkg_version}.tar.gz
BuildArch:	%{_arch}

BuildRequires:	
Requires:	
AutoReqProv:	no

%description


%prep
%setup -q -n %{pkg_name}-%{pkg_version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files

# bin
%defattr(0755,root,root,0755)

# others
%defattr(0644,root,root,0755)

# config
%defattr(0644,root,root,0755)
%config(noreplace)

# doc
%defattr(0644,root,root,0755)
%doc



%changelog

