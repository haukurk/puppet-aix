# Puppet 3.2.4 agent on AIX.
Tested for AIX 5.3, AIX 6.1 and AIX 7.1.

# Dependencies
## db
I recommend the db4 package on perzl (http://www.perzl.org/aix/index.php?n=Main.Db4)
```
rpm -ivh http://www.oss4aix.org/download/RPMS/db4/db4-4.7.25-2.aix5.1.ppc.rpm
```

# Installing
```
rpm -ivh RPMS/ppc/pup-zlib-1.2.8-1.32.puppet.local.aix5.3.ppc.rpm
rpm -ivh RPMS/ppc/pup-openssl-1.0.0k-1.32.puppet.local.aix5.3.ppc.rpm
rpm -ivh RPMS/ppc/pup-ruby-2.0.0-p247.1.32.puppet.local.aix5.3.ppc.rpm
rpm -ivh RPMS/noarch/pup-facter-1.7.2-1.puppet.local.aix5.3.noarch.rpm
rpm -ivh RPMS/ppc/pup-puppet-3.2.4-1.local.aix5.3.ppc.rpm
```
Note that all binaries are installed to */opt/puppet*

# Post-install configuration
```
mkdir -p /var/run/puppet
mkdir -p /var/lib/puppet/ssl
mkdir -p /usr/libexec/mcollective/mcollective/agent/
PUPPETMASTER=puppet.samskip.is # <- change this to fit your environment
cat<< EOF> /etc/puppet/puppet.conf
[main]
   logdir = /var/log/puppet
   rundir = /var/run/puppet
   ssldir = /var/lib/puppet/ssl
   server = $PUPPETMASTER
   pluginsync = true

[agent]
   classfile = /var/lib/puppet/classes.txt
   localconfig = /var/lib/puppet/localconfig
EOF
```

# Init scripts
```
cp init.d/puppet.init /etc/rc.d/init.d/
mv /etc/rc.d/init.d/puppet.init /etc/rc.d/init.d/puppet
chmod +x /etc/rc.d/init.d/puppet
```
Set auto-startup.
```
ln -s /etc/rc.d/init.d/puppet /etc/rc.d/rc2.d/S99puppet
```

Start agent

```
/etc/rc.d/init.d/puppet start
```

Now you can sign the certificate for your new node, on your puppetmaster.