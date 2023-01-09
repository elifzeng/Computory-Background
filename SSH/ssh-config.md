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
_Most errors can be solved by this method_  
**second method**
get the commit id like `2d23c42a936db1c7b3b06f918cde29561cc47cd6`, and mannually run `https://vscode.cdn.azure.cn/stable/ccbaa2d27e38e5afa3e5c21c1c7bef4657064247/vscode-server-linux-x64.tar.gz` on local device. Then scp the `vscode-server-linux-x64.tar.gz` to `k**:/pubhome/lzeng/.vscode-server/bin/ccbaa2d27e38e5afa3e5c21c1c7bef4657064247/`
### Still break when using vscode remote explore
In setting, select `Remote.SSH:Lockfiles In Tmp`  

![image](https://user-images.githubusercontent.com/52747634/175850287-d25c6769-e7c1-4a22-910f-3d28bb3f62c0.png)

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
# About VSCode Extension Remote Explorer
今天使用新机子同步VSCode设置时发现，remote explorer无法正常使用并提示我安装[Docker](https://www.cnblogs.com/qcloud1001/p/9273549.html)。由于过程有点复杂，在此记录一下。  
以下是安装docker的步骤，但**其实很可能只是因为远程没有安装remote explorer**，可以先尝试install一下。  

1. [在终端安装docker](https://www.how2shout.com/linux/what-do-we-need-to-install-docker-on-rhel-8/)。
2. 在VSCode Extension中搜索安装 Docker  
![image](https://user-images.githubusercontent.com/52747634/211251009-f10d5906-8567-437b-910c-c667cccd2994.png)

3. 刚安装完上面的插件时可能会出现以下报错：
```bash
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/build?buildargs=%7B%7D&cachefrom=%5B%5D&cgroupparent=&cpuperiod=0&cpuquota=0&cpusetcpus=&cpusetmems=&cpushares=0&dockerfile=Dockerfile&labels=%7B%7D&memory=0&memswap=0&networkmode=default&pull=1&rm=1&shmsize=0&t=controlwharehouse%3Alatest&target=&ulimits=null&version=1": dial unix /var/run/docker.sock: connect: permission denied
```
解决办法：[Run the Docker daemon as a non-root user (Rootless mode)](https://docs.docker.com/engine/security/rootless/)  

