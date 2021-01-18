```bash
wget https://ftp.gnu.org/gnu/wget/wget-1.21.1.tar.gz
$ ./configure --prefix=/usr      \
            --sysconfdir=/etc  \
            --with-ssl=openssl &&
make
#run as root
$ make install
# check
wget -V
```
[ref](http://www.linuxfromscratch.org/blfs//view/svn/basicnet/wget.html)
