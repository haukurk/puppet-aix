%define install_prefix /opt/puppet
%define _defaultdocdir %{install_prefix}/doc
%define patchlevel 371
%define tarballname ruby

Summary:        An interpreter of object-oriented scripting language
Name:		pup-ruby
Version:        1.8.7
Release:        p%{patchlevel}.1.32.puppet.local
Group:          Development/Languages
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
Prefix:		%{install_prefiX}
Source:		%{tarballname}-%{version}-p371.tar.gz
BuildRoot:	%{_tmppath}/%{tarballname}-%{version}-%{release}-root
Requires:	pup-zlib-local
Requires:	pup-openssl-local
#Requires:	db4 >= 4.7.25-2
# BuildRequires:	libgcc make gcc

Provides: 	pup-ruby-local
Provides:       pup-ruby(abi) = 1.8
Provides:       pup-libruby = %{version}-%{release}
Obsoletes:      pup-libruby <= %{version}-%{release}
Provides:       pup-irb = %{version}-%{release}
Obsoletes:      pup-irb <= %{version}-%{release}
Provides:       pup-rdoc = %{version}-%{release}
Obsoletes:      pup-rdoc <= %{version}-%{release}


%description
ruby is the interpreted scripting language for quick and easy
object-oriented programming.  It has many features to process text
files and to do system management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep 


%setup -n %{tarballname}-%{version}-p%{patchlevel}


%build
export CFLAGS="-DSYSV -D_AIX -D_AIX32 -D_AIX41 -D_AIX43 -D_AIX51 -D_ALL_SOURCE -DFUNCPROTO=15 -O"

export LDFLAGS="-L/opt/puppet/lib -Wl,-blibpath:/opt/puppet/lib:/usr/lib:/lib -Wl,-bmaxdata:0x80000000"

export OBJECT_MODE=32
#export CC="gcc -maix32"
#export LD="gcc"
ARFLAGS="-X32"

./configure --prefix=%{install_prefix} --with-zlib-include=/opt/puppet/include --with-zlib-lib=/opt/puppet/lib --with-openssl-dir=/opt/puppet
gmake 

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,system,-)
/%{install_prefix}/bin/*
/%{install_prefix}/lib/*
/%{install_prefix}/share/*


%changelog
* Tue Jan 15 2013 by Toni Schmidbauer <toni@stderr.at> - 1.8.7-p371.1.puppet.local
- Version 1.8.7-p371
* Tue Dec 06 2011 by Nick Bausch <nick.bausch@gmail.com> - 1.8.7-p352.1.puppet.local
- First ruby-puppet-local build for AIX
