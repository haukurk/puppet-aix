
Name:           pup-puppet-conf
Version:        0.1
Release:        1.local
Summary:        Configuration File For Puppet
License:        GPL
URL:            http://localhost
Source0:        %{name}-%{version}.tar.gz
Group:          Local Puppet Configuration
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

%description
This is a default config file for puppet.  Modify to meet your needs.


%prep
%setup -q -n %{name}-%{version}


%build


%install
mkdir -p ${RPM_BUILD_ROOT}/etc/puppet
cp ${RPM_BUILD_DIR}/%{name}-%{version}/puppet.conf ${RPM_BUILD_ROOT}/etc/puppet

%files
%defattr(-, root, root, 0755)
/etc/puppet

%changelog
* Mon Dec 19 2011 Nick Bausch <nick.bausch@gmail.com> - 0.1-1.local
- First puppet-config build for AIX
