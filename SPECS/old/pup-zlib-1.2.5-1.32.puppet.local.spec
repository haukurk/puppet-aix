%define install_prefix /opt/puppet/pup-zlib
%define _defaultdocdir %{install_prefix}/doc
%define tarballname zlib
 
Summary:	The zlib compression and decompression library
Name:		pup-zlib
Version:	1.2.5
Release:	1.32.puppet.local
Group:		System Environment/Libraries
Source:		zlib-%{version}.tar.bz2
Patch0:		%{tarballname}-%{version}-aix.patch
URL:		http://www.gzip.org/zlib/
License:	zlib
Provides: 	pup-zlib-local
BuildRoot:	%{_tmppath}/%{tarballname}-%{version}-%{release}-root
BuildRequires:  make gcc


%description
Zlib is a general-purpose, patent-free, lossless data compression
library which is used by many different programs.

The library is available as 32-bit and 64-bit.

If you are compiling a 64-bit program, you have to compile and link your
application with "cc -q64" or "gcc -maix64".


%prep
%setup -n %{tarballname}-%{version}
%patch0

%build

export CFLAGS="-DSYSV -D_AIX -D_AIX32 -D_AIX41 -D_AIX43 -D_AIX51 -D_AIX52 -D_AIX53 -D_AIX61 -D_ALL_SOURCE -DFUNCPROTO=15 -O"

export OBJECT_MODE=32
export CC="gcc"
ARFLAGS="-X32"


./configure \
    --prefix=%{install_prefix} \
    --shared
gmake

%install
rm -rf $RPM_BUILD_ROOT
make install prefix="$RPM_BUILD_ROOT/%{install_prefix}" 

%clean
[ "${RPM_BUILD_ROOT}" != "/" ] && rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,system,-)
/%{install_prefix}/lib/*
/%{install_prefix}/include/*
/%{install_prefix}/man/*

%changelog
* Tue Dec 06 2011 Nick Bausch <nick.bausch@gmail.com> -  1.2.5-1.puppet-local
- First zlib-puppet-local build for AIX
