%define _prefix /opt/puppet/pup-puppet
%define _defaultdocdir %{_prefix}/doc
%define _rubybin /opt/puppet/pup-puppet/bin/ruby
%define tarballname facter

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(%{_rubybin} -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}


Summary: Ruby module for collecting simple facts about a host operating system
Name: pup-facter
Version: 1.6.3
Release: 1.puppet.local
License: Apache 2.0
Group: System Environment/Base
URL: http://www.puppetlabs.com/puppet/related-projects/%{tarballname}/
Source: %{tarballname}-%{version}rc1.tar.gz
BuildRoot: %{_tmppath}/%{tarballname}-%{version}-%{release}-root
BuildArch: noarch

Requires: pup-ruby-local >= 1.8.1
Provides: pup-facter-local = 1.6.3
BuildRequires: pup-ruby-local >= 1.8.1 python readline gdbm 

%description
Ruby module for collecting simple facts about a host Operating
system. Some of the facts are preconfigured, such as the hostname and the
operating system. Additional facts can be added through simple Ruby scripts

%prep
%setup -n %{tarballname}-%{version}


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
* Mon Dec 19 2011 Nick Bausch <nick.bausch@gmail.com> - 1.6.3-1.puppet.local
- First facter-puppet-local build for AIX
* Mon Oct 31 2011 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.3-0.1rc1
- 1.6.3 rc1
