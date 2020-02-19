# Something about git
```bash
$ git clone git@github.com:hnlab/fullspace.git
# 报错
Warning: Permanently added the RSA host key for IP address '192.30.253.113' to the list of known hosts.
Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
```
此时需要将这台电脑的公钥加到github上  
![image](https://user-images.githubusercontent.com/52747634/71792098-547b6780-3072-11ea-8fc5-7c11a9ce6e02.png)
# 基本概念
Git包括：【工作区】—git add—【暂存区】—git commit—【本地库】
# Git 命令行操作
`Git`专属命令一般都为`git [options]`形式。
## 本地库初始化
```bash
$ git init 
```
初始化一个空的Git仓库（这是在gitbash下的操作，在github直接创建仓库就可以了），该命令在本地创建了一个`./.git`目录，其下存放的是本地库相关的子目录和文件，不可随意删除和修改。
## 设置签名
（一般设置系统用户级别的就行了）
```bash
git config user.name elif_pro # 项目级别/仓库级别，仅在当前本地库范围内（当前操作系统某文件夹下）有效（优先）
git config user.email Elifzzz_pro@xxx.com 
git config --global user.name elif_glb # 系统用户级别，登录当前操作系统的用户范围
git config --global user.email Elifzzz_glb@xxx.com 
```
以上仓库级别签名信息保存在`./.git/config`，系统用户级别签名保存在`~/.gitconfig`下：  
![image](https://user-images.githubusercontent.com/52747634/74800932-0499ec80-5310-11ea-8a21-7e565260c45c.png)  
签名是用于**标识开发人员的身份**。形式：用户名：elif, Email：Elifzzz@xxx.com。  
注意：这里设置的签名和登录远程库（代码托管中心）的账号、密码没有任何关系。
## 基本操作
以下命令及更多更改命令都可以通过`git status`获得提示。
```bash
$ git status # 查看工作区、暂存区状态
$ git add [filename] # 将工作区的“新建/修改”添加到暂存区
$ git commit -m 'message' [filename]# 将缓存区的文件提交到本地库，并附带注释
```
