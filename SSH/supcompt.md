# 在超算构建SSH隧道
啊，我也不知道该起什么标题，暂时就以这个标题来命名吧，因为我已经濒临崩溃了（笑对人生💆）。 
（其实后文还有超算的应用tips，后加的）
## 遇到了困难先发一波牢骚
最近需要使用大量计算资源，因此老师让我去超算上跑任务。本来是热泪盈眶的 _wrklick aufgeregt_ ，但折腾了几天发现超算没法连网，一个没法安装包的python等于没有，因此现在要找办法让超算能
用上网下载安装各种东西。  
说实话，幸好这几天还干了点别的活。要是啥也没干，这个也没折腾好，我真的会自闭的。  
## 应用场景
超算无法联网，但我需要安装python包、下载各种软件等，必须使用网络，因此需要构建一个从本地到超算的ssh隧道，开一个代理，满足我的联网需求。  
挺复杂的。如果我搞定了之后，这个文档我要收费反正。一块钱一个字。  
## 系统配置
### 超算
广州天河超算中心  
```bash
[nibs_nhuang_1@lon21:~]$ lsb_release -a
LSB Version:	:core-4.1-amd64:core-4.1-noarch
Distributor ID:	RedHatEnterpriseServer
Description:	Red Hat Enterprise Linux Server release 7.3 (Maipo)
Release:	7.3
Codename:	Maipo
```
### 本地机器
```bash
[zenglj@x024 ~]$ lsb_release -a
LSB Version:	:core-4.1-amd64:core-4.1-noarch
Distributor ID:	Rocky
Description:	Rocky Linux release 8.7 (Green Obsidian)
Release:	8.7
Codename:	GreenObsidian
```
相当于centos 7.
## 理论知识
需要了解的：squid, ssh 隧道，sysctl restart squid  
port 3128  
tepip  
### squid
其实就是一个代理服务器。功能丰富的Web代理缓存服务器软件，可为流行的网络协议（包括HTTP, HTTPS和FTP）提供代理和缓存服务。  
![image](https://user-images.githubusercontent.com/52747634/215239580-fa39c33b-d35b-4e18-9693-352f8beecd69.png)  
它接收来自客户端的请求并将它们传递到指定的后端服务器。后端服务器响应时，会将内容的副本存储在缓存中，然后将其传递给客户端。将来对相同内容的请求将从缓存中得到处理，从而将内容更快地传递到客户端。因此，它可以优化客户端和服务器之间的数据流以提高性能，并缓存常用内容以减少网络流量并节省带宽。
Squid可用于做服务器的统一出口，把squid作为能够出[公网](https://www.zhihu.com/question/337578873)的设备，然后为所有需要出公网的服务器进行代理设置，从而带动内网服务器能够上网。  

### 操作步骤
1. x024上安装squid
x024作为代理服务器
```bash
# RHEL7 系统的安装光盘中自带了Squid的RPM格式的软件包。
yum -y install squid
systemctl restart squid
```
2. 保证x024能ssh连到超算上
_Notice_:要保持Node52网页VPN正常连通
3. 打通ssh 隧道
```bash
ssh  -tR 31128:localhost:3128  -p2222 nibs@node52  ssh -p5566  -R 31128:localhost:31128  nibs_nhuang_1@172.16.22.11 -i nibs_nhuang_1.id
```
这个命令运行结果不稳定，要多试几次。
4. 在`.bashrc`中添加代理协议和端口
```bash
# ~/.bashrc
export http_proxy=127.0.0.1:31128
export https_proxy=127.0.0.1:31128
```
_Notice_:如果某些应用的代理不支持`http_proxy, https_proxy`，可以在网页上用`vscode proxy`类似关键词搜索其代理协议。
### 补充知识
等我先能运行任务再说把，tmd.
























































