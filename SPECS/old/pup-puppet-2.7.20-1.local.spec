%define _prefix /opt/puppet/pup-puppet
%define _rubybin /opt/puppet/pup-puppet/bin/ruby
%define _defaultdocdir %{_prefix}/doc
%define tarballname puppet

%{!?ruby_sitelibdir: %global ruby_sitelibdir %(%{_rubybin} -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}
%global confdir conf/redhat

Name:           pup-puppet
Version:        2.7.20
Release:        1.local
Summary:        A network tool for managing many disparate systems
License:        ASL 2.0
URL:            http://puppetlabs.com
Source0:        %{tarballname}/%{tarballname}-2.7.20.tar.gz
Source1:        %{tarballname}/%{tarballname}-2.7.20.tar.gz.asc
Group:          System Environment/Base
BuildRoot:      %{_tmppath}/%{tarballname}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       pup-ruby-local
Requires:       pup-facter-local
Provides:       pup-puppet-local

%description
Puppet lets you centrally manage every important aspect of your system using a
cross-platform specification language that manages all the separate elements
normally aggregated in different files, like users, cron jobs, and hosts,
along with obviously discrete elements like packages, services, and files.

%prep
%setup -q -n %{tarballname}-2.7.20


%build

# Fix some rpmlint complaints
for f in mac_dscl.pp mac_dscl_revert.pp mac_pkgdmg.pp ; do
  echo "looking at examples/$f"
  cp examples/$f examples/$f.sed
  sed -e 1d examples/$f.sed > examples/$f
  chmod a-x examples/$f
done
#chmod +x ext/puppetstoredconfigclean.rb

find examples/ -type f -empty | xargs rm
find examples/ -type f | xargs chmod a-x

# puppet-queue.conf is more of an example, used for stompserver
mv conf/puppet-queue.conf examples/etc/puppet/

%install
rm -rf %{buildroot}
%{_rubybin} install.rb --destdir=%{buildroot} --quick

%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root, 0755)
%doc CHANGELOG LICENSE README.md examples
/etc/puppet
/opt/puppet/pup-puppet

%changelog
* Tue Jan 15 2013 Toni Schmidbauer <toni@stderr.at> - 2.7.20-1.local
- Version 2.6.20
* Mon Dec 19 2011 Nick Bausch <nick.bausch@gmail.com> - 2.7.6-1.local
- First puppet-local build for AIX
