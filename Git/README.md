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

```bash
$ git help [cmd] # 查看帮助文档
```

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
### 提交任务等
以下命令及更多更改命令都可以通过`git status`获得提示。
```bash
$ git status # 查看工作区、暂存区状态
$ git add [filename] # 将工作区的“新建/修改”添加到暂存区
$ git commit -m 'message' [filename]# 将缓存区的文件提交到本地库，并附带注释
```
### 实现版本前进和回退
版本的前进和回退，本质上是操作**HEAD**指针。
#### 查看历史日志
```bash
$ git log #查看完整版本历史日志
commit 4ecfcf8dca4e059e17054e52137883cd834ca814  (HEAD -> yolk, origin/yolk)
Author: elifzeng <elifzeng@163.com>
Date:   Fri Feb 14 13:44:54 2020 +0800

    grep pdb data and energy of representative pairs
```
在这里只列出了部分的commit，第一行第二部分内容为提交索引，由哈希函数算出。括号里的`HEAD`指针表示现在处于哪个分支和哪个版本。
```bash
$ git log --pretty=oneline #每个提交以一行显示
$ git log --oneline # 更简洁，哈希值只显示一部分，只能显示当前及以前的版本
$ git reflog # 显示回溯到某版本需要n步 HEAD@{n}【推荐】
```
#### 版本前进回退
推荐使用`基于索引值`操作。（此外还有基于`^`符号和基于`~`符号的操作）
```bash
$ git reset --hard fa9d29b # 此处的索引值为哈希值的一部分（通过git reglog获得）
```
*reset 命令的三个参数对比*（了解）
原本三区状态是一致的。使用`git reset --[options]`命令后对应区的状态会发生变化。
1. `--soft` 仅仅在本地库以移动HEAD指针，不会去动工作区(index file)和暂存区(working tree)。
2. `--mixed` 在本地库移动HEAD指针，且重置暂存区。
3. `--hard` 在本地库移动HEAD指针，重置暂存区，重置工作区。
#### 删除文件及找回
```bash
$ rm [filename] # 现在本地库删除(此时可以用git status查看状态)
$ git add [filename]
$ git commit -m 'lsdkjflsdj' [filename]
```
也就是说，git上添加了该文件被删除的记录。当**回退到以前的版本状态**时，该删除的文件还能被找回。而当删除文件提交到暂存区而**未提交到本地库**时，可通过`git reset`找回（参看`git status`提示）。  
#### 比较文件差异
```bash
$ git diff [filename] # 将工作区文件和暂存区进行比较
$ git diff [本地库中历史版本号] [filename] # 将工作区文件和本地库历史记录比较
$ git diff #不带文件名可比较多个文件
```
### 分支管理
在版本控制过程中，使用多条线同时推进多个任务。  
好处：
1. 同时并行推进多个功能开发，提高开发效率
2. 各个分支在开发过程中，如果某一个分支开发失败，不会对其他分支有任何影响。失败的分支删除重新开始即可。
```bash
$ git branch -v # 查看分支及分支状态
$ git branch [branchname] # 创建一个新的分支
$ git checkout [branchname] # 切换分支
$ git merge [branchname]#合并分支,先切换到要合并到的分支上(如要把branch合并到master上，就先切换到master分支)，再执行merge命令
```
解决合并分支**冲突**：
```txt
aaaaaaa
<<<<<<< HEAD
sdjfhaisdfi
=======
>>>>>>> master
isudhfksad
...
```
上面文段从`HEAD`行到`=======`行之间的，为当前分子内容，`=======`到`master`之间的，为另一分支内容。不需要哪一部分就直接在文档里删掉。**注**：merge后`git commit`后不能带文件名，否则会报错。
### 远程库
```bash
git remote -v # 查看已有远程库地址（就是clone时用的那个地址）
git remote add [alias] [repository address] # 将远程库地址添加到本地Git上，并取了个别名
git push [alias] [branch name ] # 推送到远程库
git clone [repository address] # 将别人的库克隆到本地
```
将别人的库克隆到本地时，会同时：
1. 完整地把远程库克隆到本地
2. 创建origin远程地址别名
3. 初始化本地库（`.git`文件）
添加成员：`log in github -> the repository you want to operate -> setting -> Manage access -> invite a collaborator -> Copy invite link -> send to the man you want to invite -> verify`
