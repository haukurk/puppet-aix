%define _prefix /opt/puppet
%define _rubybin /opt/puppet/bin/ruby
%define _defaultdocdir %{_prefix}/doc
%define tarballname puppet

%{!?ruby_sitelibdir: %global ruby_sitelibdir %(%{_rubybin} -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%global confdir conf/redhat

Name:           pup-puppet
Version:        3.2.4
Release:        1.local
Summary:        A network tool for managing many disparate systems
License:        ASL 2.0
URL:            http://puppetlabs.com
Source0:        %{tarballname}/%{tarballname}-3.2.4.tar.gz
Group:          System Environment/Base
BuildRoot:      %{_tmppath}/%{tarballname}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       pup-ruby-local
Requires:       pup-facter-local
Provides:       pup-puppet-local
#Patch0:         puppet-3.1.0-groupname_by_id.patch
#Patch1:         puppet-3.1.0-list_all.patch


%description
Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts,
along with obviously discrete elements like packages, services, and files.

%prep
%setup -q -n %{tarballname}-3.2.4
#%patch0
#%patch1


%build

# Fix some rpmlint complaints
#for f in mac_pkgdmg.pp ; do
#  echo "looking at examples/$f"
#  cp examples/$f examples/$f.sed
#  sed -e 1d examples/$f.sed > examples/$f
#  chmod a-x examples/$f
#done
#chmod +x ext/puppetstoredconfigclean.rb

find examples/ -type f -empty | xargs rm
find examples/ -type f | xargs chmod a-x

# puppet-queue.conf is more of an example, used for stompserver
#mv conf/puppet-queue.conf examples/etc/puppet/

%install
rm -rf %{buildroot}
%{_rubybin} install.rb --destdir=%{buildroot} --quick

%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README.md examples
/etc/puppet
/opt/puppet

%changelog
* Tue Aug 28 2013 Toni Schmidbauer <toni@stderr.at> - 3.2.4-1.local
- Puppet version 3.2.4
* Tue Mar 13 2013 Toni Schmidbauer <toni@stderr.at> - 3.1.1-1.local
- Puppet version 3.1.1 + patches
* Tue Mar 11 2013 Toni Schmidbauer <toni@stderr.at> - 3.1.0-1.local
- Puppet version 3.1.0 + patches
* Tue Jan 15 2013 Toni Schmidbauer <toni@stderr.at> - 3.0.2-1.local
- Puppet version 3.0.2
* Mon Dec 19 2011 Nick Bausch <nick.bausch@gmail.com> - 2.7.6-1.local
- First puppet-local build for AIX
