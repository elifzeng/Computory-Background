# Reading papers or using google service outside NIBS

## Install `Terminal` and `Wingy` on ipad.
  
  (no need to log in)

### In Terminal

  `Keychain` --> `'+' on the top right` --> `Paste Key`
  Fill the table with private key of users who can log in huanglab.org.cn
  ```
  Name:
  zenglj@host
  Private:
  private key of your host in lab. i.e./home/.ssh/id_rsa # see Notice1 below
  ```
  Notice1: click `Keychain` --> `'+' on the top right` --> `Import Key`, you can see that 'Support file types:text, txt, pem,...`
  So you should translate id_rsa to id_rsa.pem

  **Translate File Type to pem**
  
  [link](http://www.guohuawei.com/archives/gen-pem-key-for-ssh-login.html)
  (On host terminal)
  ```
  $openssl rsa -in ~/.ssh/id_rsa -outform pem > id_rsa.pem
  $chmod 700 id_rsa.pem
  ```
  Then `Paste Key`:
  ```
  Name :
  id_rsa.pem
  Private:
  The content of id_rsa.pem
  ```
  `Host` --> `+` --> `New Host` 
  ```
  Alias    hn
  Hostname     www.huanglab.org.cn #or input IP address
  Port     22
  Username     zenglj
  Key     zenglj@x026 # the key just creat before
  ```
  `Port Forwarding` --> `+` -->
  --> `Local`:
  ```
  Host     zenglj@www.huanglab.org.cn:22
  Port From     9347 # 随便指定的
  Destination     localhost
  Port To     2222
  Bind Address: 127.0.0.1
  ```
  --> `Remote`:
  ```
  Host     zenglj@www.huanglab.org.cn:22
  Port From     9347 # 随便指定的
  Destination     localhost
  Port To     2222
  Bind Address: 127.0.0.1
  ```
  -->`Dynamic`:
  ```
  Host     zenglj@www.huanglab.org.cn:22
  Port     9347
  ```
  Open the terminal in `Host` and input (when connected to huanglab.org.cn)
  ```
  ssh -ND 2222 x026
  ```
  run the item in `Port Forwarding` simultaneously
  
### On Wingy

  click `+` and choose `Socks5`
  ```
  server     127.0.0.1
  Port     9347
  Proxy Mode      Auto
  ```
  choose the proxy just added
  
  complete
  
## The next time you open ipad
  Activete connecting in wingy
  Open terminal in `Host` of `Termius`:
  `$ ssh username@host`
  
  
  
