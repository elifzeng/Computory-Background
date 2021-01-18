`~/.ssh/config`  
`chmod 600 config` (otherwise the error `Bad owner or permissions on /home/zenglj/.ssh/config` will be rose)

```bash
Host x25402
    HostName x254.hn.org
    User lzeng02
    IdentityFile /home/test/.ssh/id_rsa.pub

Host x254
    HostName x254.hn.org
    User lzeng02
    IdentityFile /home/test/.ssh/id_rsa.pub
```

Now you can ssh by `ssh x254` rather than `ssh lzeng@x254`

`generate ssh key`

1st, check if ssh-key already exist. If not, genetate a new ssh-key.  
```bash
ssh-keygen -t rsa
# Creates a new ssh key
Generating public/private rsa key pair.
Enter file in which to save the key (/your_home_path/.ssh/id_rsa):
Enter passphrase (empty for no passphrase): 
#
The last step can be skipped.
```
### Two stedrr exist when using vscode remote explore 
#### 1.Server installation process already in progress
[ref](https://github.com/microsoft/vscode-remote-release/issues/2507)  
*output*:
```bash
[09:52:13.523] stderr> ln: failed to create hard link ‘/home/zenglj/.vscode-server/bin/db40434f562994116e5b21c24015a2e40b2504e6/vscode-remote-lock.sma.78a4c91400152c0f27ba4d363eb56d2835f9903a': File exists
```
**solution**: del the dictionary `db40434f562994116e5b21c24015a2e40b2504e6`

#### 2.stucked in Downloading with wget
**solution**: del the dictionary `db40434f562994116e5b21c24015a2e40b2504e6` and reinstall or scp the dictionary from other place, like host `hn`.  

### Just for backup
```bash
Host hn
    User zenglj
    HostName www.huanglab.org.cn

Host x??? n??? k??? z55 xn xk
    ProxyCommand ssh -4 -q -W %h:%p hn

# For desktop machine
Host x021
    User zenglj
```
