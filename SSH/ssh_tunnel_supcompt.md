# 在超算构建SSH隧道
啊，我也不知道该起什么标题，暂时就以这个标题来命名吧，因为我已经濒临崩溃了（笑对人生💆）。  
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





























































