## Build Me Like This:
## PATH=/opt/freeware/bin:$PATH rpm -ba pup-openssl-1.0.0k-1.32.puppet.local.spec

%define _prefix /opt/puppet
%define openssldir /opt/puppet
%define openssldir64 /opt/puppet
%define _defaultdocdir %{_prefix}/doc
%define libsslver 1.0.0
%define _libdir64 lib64
%define tarballname openssl

Name:		pup-openssl
Version:	1.0.0k
Release:	1.32.puppet.local
License: 	OpenSSL License 
URL: 		http://www.openssl.org/
Prefix:		%{_prefix}
Source:		openssl-%{version}.tar.gz
Patch0:         %{tarballname}-%{version}-Configure.patch
BuildRoot:	%{_tmppath}/%{tarballname}-%{version}-%{release}-root
Provides:	pup-openssl-local
Requires:	pup-zlib-local
#Requires:	libgcc
#BuildRequires:  make gcc perl pup-zlib-local
BuildRequires:  make perl pup-zlib-local


Summary: Secure Sockets Layer and cryptography libraries and tools
Group: System Environment/Libraries

%description
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, fully featured, and Open Source toolkit implementing the
Secure Sockets Layer (SSL v2/v3) and Transport Layer Security (TLS v1)
protocols as well as a full-strength general purpose cryptography library.
The project is managed by a worldwide community of volunteers that use the
Internet to communicate, plan, and develop the OpenSSL tookit and its related
documentation.

OpenSSL is based on the excellent SSLeay library developed from Eric A. Young
and Tim J. Hudson.  OpenSSL is licensed under the OpenSSL License, included in
this package.

This package contains the base OpenSSL cryptography and SSL/TLS libraries and
tools.

You should also install a pseudo-random number generator such as EGD or prngd
if you do not have a /dev/urandom and /dev/random.

%prep
%setup -n %{tarballname}-%{version}

%build
perl util/perlpath.pl /usr/bin/perl

export CFLAGS="-DSYSV -D_AIX -D_AIX32 -D_AIX41 -D_AIX43 -D_AIX51 -D_AIX52 -D_AIX53 -D_AIX61 -D_ALL_SOURCE -DFUNCPROTO=15 -O -I/opt/puppet/include"

export LDFLAGS="-L/opt/puppet/lib -Wl,-blibpath:/usr/lib:/lib -Wl,-bmaxdata:0x80000000"

#export OBJECT_MODE=64
#export CC="gcc -maix64"
#export AR=/usr/bin/ar
#ARFLAGS="-X64"
#export CPATH="/opt/puppet/include/"
#
#./Configure \
#    no-idea no-mdc2 no-rc5 \
#    no-symlinks -DSSL_ALLOW_ADH \
#    threads \
#    no-shared \
#    zlib-dynamic \
#    --prefix=%{_prefix} \
#    --openssldir=%{openssldir64} \
#    aix64-gcc

#gmake -j4 depend
#gmake -j4 build_libs

#mkdir -p %{_libdir64}
#if [ -f "/opt/freeware/bin/cp" ]; then
#  /opt/freeware/bin/cp -P libcrypto*  %{_libdir64}/
#  /opt/freeware/bin/cp -P libssl* %{_libdir64}/
#else 
#  /usr/bin/cp -h libcrypto*  %{_libdir64}/
#  /usr/bin/cp -h libssl* %{_libdir64}/
#fi


#gmake clean-shared
#gmake clean

# now build the 32-bit version
export CFLAGS="-DSYSV -D_AIX -D_AIX32 -D_AIX41 -D_AIX43 -D_AIX51 -D_AIX52 -D_AIX53 -D_AIX61 -D_ALL_SOURCE -DFUNCPROTO=15 -O -I/opt/puppet/include"

export LDFLAGS="-L/opt/puppet/lib -Wl,-blibpath:/opt/puppet/lib:/opt/puppet/lib:/usr/lib:/lib -Wl,-bmaxdata:0x80000000"

export CPATH="/opt/puppet/include/"
export OBJECT_MODE=32
ARFLAGS="-X32"
export CC="cc"

./Configure \
    no-idea no-mdc2 no-rc5 \
    no-symlinks -DSSL_ALLOW_ADH \
    threads \
    no-shared \
    zlib-dynamic \
    --prefix=%{_prefix} \
    --openssldir=%{openssldir} \
    --with-zlib-include=/opt/puppet/include \
    --with-zlib-lib=/opt/puppet/lib \
    aix-cc

gmake depend
gmake build_libs


%install
rm -rf $RPM_BUILD_ROOT
make MANDIR=%{_prefix}/man INSTALL_PREFIX="$RPM_BUILD_ROOT" install

#cp -r ${RPM_BUILD_DIR}/%{tarballname}-%{version}/%{_libdir64}/ ${RPM_BUILD_ROOT}/%{_prefix}/%{_libdir64}/


#%clean
#[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}


%files
%defattr(-,root,system,-)
/%{_prefix}/bin/*
/%{_prefix}/include/*
/%{_prefix}/misc/*
/%{_prefix}/private/
/%{_prefix}/certs/
/%{_prefix}/lib/*
/%{_prefix}/man/*
/%{_prefix}/openssl.cnf
#/%{_prefix}/%{_libdir64}/*

%post
# Create a symlink for libcc_s.a based on libgcc rpm contents
#LIBGCC_LIB=$(/usr/bin/find /opt/freeware/lib/ -name "libgcc_s.a"| /usr/bin/env egrep -v "64|pthread" | tail -1 )
#cd /opt/puppet/pup-openssl/lib
#/usr/bin/ln -sf $LIBGCC_LIB

%changelog
* Mon Aug 28 2013 by Toni Schmidbauer <toni@stderr.at> 1.0.0k-1.puppet.local
- update to version 1.0.0k
* Mon Dec 05 2011 by Nick Bausch <nick.bausch@gmail.com> 1.0.0e-1.puppet.local
- First ssl-puppet-local build for AIX
* Fri Jan 06 2011 by Nick Bausch <nick.bausch@gmail.com> 1.0.0e-2.puppet.local
- Adding tail -1 to %post routine to handle case where multiple versions or symlinks of libgcc_s.a available in /opt/freware just choose one.  Admin can change if needed.
