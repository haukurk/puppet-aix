%define _prefix /opt/puppet
%define _defaultdocdir %{_prefix}/doc
%define _rubybin /opt/puppet/bin/ruby
%define tarballname facter

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(%{_rubybin} -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}


Summary: Ruby module for collecting simple facts about a host operating system
Name: pup-facter
Version: 1.7.0
Release: 1.puppet.local
License: Apache 2.0
Group: System Environment/Base
URL: http://www.puppetlabs.com/puppet/related-projects/%{tarballname}/
Source: %{tarballname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{tarballname}-%{version}-%{release}-root
BuildArch: noarch
Requires: pup-ruby-local >= 1.8.1
Provides: pup-facter-local = 1.7.0
BuildRequires: pup-ruby-local >= 1.8.1 python readline gdbm 
#Patch0: facter-1.6.18-hardwaremodel.patch
#Patch1: facter-1.6.18-operatingsystemrelease.patch

%description
Ruby module for collecting simple facts about a host Operating
system. Some of the facts are preconfigured, such as the hostname and the
operating system. Additional facts can be added through simple Ruby scripts

%prep
%setup -n %{tarballname}-%{version}
#%patch0
#%patch1

%build

%install
rm -rf %{buildroot}
%{_rubybin} install.rb --destdir=%{buildroot} --quick --no-rdoc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/facter
%{ruby_sitelibdir}/facter.rb
%{ruby_sitelibdir}/facter
%doc CHANGELOG INSTALL LICENSE README.md


%changelog
* Tue Apr 16 2013 Toni Schmidbauer <toni@stderr.at> - 1.7.0-1.puppet.local
- Update to factor 1.7.0
- removed 1.6.18 patches, but maybe the hardwaremodel fix is still required
* Tue Mar 14 2013 Toni Schmidbauer <toni@stderr.at> - 1.6.18-2.puppet.local
- patches
  - http://projects.theforeman.org/issues/1489
  - http://seriousbirder.com/blogs/foreman-aix-client-images-missing-on-console/
* Tue Mar 14 2013 Toni Schmidbauer <toni@stderr.at> - 1.6.18-1.puppet.local
- Update to factor 1.6.18
* Tue Jan 15 2013 Toni Schmidbauer <toni@stderr.at> - 1.6.17-1.puppet.local
- Update to factor 1.6.17
* Mon Dec 19 2011 Nick Bausch <nick.bausch@gmail.com> - 1.6.3-1.puppet.local
- First facter-puppet-local build for AIX
* Mon Oct 31 2011 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.3-0.1rc1
- 1.6.3 rc1
