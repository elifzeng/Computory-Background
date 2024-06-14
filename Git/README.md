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
Git 代码状态包括： 
- 未被Git跟踪的状态为unstage状态
- 已被Git跟踪的状态为stage状态（stage：阶段），因此包括staging状态和staged状态
    - untrack files:指尚未被git所管理的文件; changed but not updated：是指文件被git管理，并且发生了改变，但改动还没被git管理；这两种状态，都可以看成是改动还没被git管理的状态，我们这里称unstage状态。
    - staging是commit和未管理之间的一个状态，也有别名叫index状态，也就是git已经管理了这些改动，但是还没完成提交。changes to be commited是指进入staged状态的文件。
    - .gitignore中的文件，不会出现在以上三个状态中
- 综上，add就是被Git跟踪了，commit就是本Git管理了。代码一旦修改，就会成为未被git库跟踪的状态。需要add、commit。
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
#### 创建远程库
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
#### 只克隆远程库的一个分支（本地什么都没有）
已有本地分支的情况见后  
```bash
git clone -b elifzeng/issue28 git@github.com:hnlab/CPFrags.git
```
注意，branch名称前面没有`origin/`.
#### 拉取
作为管理员，要将其他成员push到远程库的东西pull下来，而`pull`这一步包含了`fetch`&`merge`两个步骤。有时`pull`这个步骤会分为后两个步骤执行，这样可以在fetch到本地后先确认好文件内容，再与本地文件merge,比较保险。 
```bash
git fetch [alias] [branchname] #只是把远程内容下载到本地，但未修改本地库的文件
git merge [alias/branchname]# 合并文件
git pull [alias] [branchname]
```
#### 解决冲突
1. 果不是基于GitHub远程库的最新版所做的修改，不能推送，必须先拉取。
2. 拉取下来后，如果进入`冲突`状态，则按照“分支冲突解决”操作解决即可。
#### 跨团队协作
1. 在GitHub上将别的团队的库`fork`下来（点击页面右上角Fork按钮）
2. clone下来，本地修改，然后推送到远程
3. Pull requests（GitHub页面Wiki那一横栏的另一个按钮）-> New pull request 绿色按钮 -> Create pull request -> 在弹出来的页面中给对方发消息

接下来由管理员点击`Pull request`查看对方刚刚发送的信息，可以在该页面进行对话。通过`Commits`栏查看有哪些提交，`Files changed`栏查看有哪些修改（即审核代码）。如果没问题，则点击`Merge pull request`按钮合并代码。然后通过`pull`拉取到本地。
#### SSH登录
适用于只有一个账户的时候。
1. 进入家目录
2. 删除原`.ssh/`,并通过`ssh-keygen`重新生成。
```bash
ssh-keygen -t rsa -C [mail@ddress]
```
将其中生成的公钥内容复制到GitHub上本教程页首截图所示页面上。
3. 在本地通过`git remote add [alias] [ssh-address]`将远程库添加到本地。

## 进阶操作
### 在本地已有分支的基础上克隆远程分支
如果此时本地分支还有修改未commit，但又因为bug没改完等原因不想commit，可以先stash缓存，之后再回来继续修改。  
```bash 
git stash
```
然后就可以拉取远程分支了
```bash
# 查看远程分支
git branch -r
# 查看本地分支
git branch
# 在本地建立对应远程分支的本地分支，此时会自动跳转到新分支
# 比如 git checkout -b elifzeng/issue22 origin/elifzeng/issue22
# 注意，只有远程分支名是origin/xxx
git checkout -b 本地分支名 origin/远程分支名
# 拉取远程分支
git pull origin 远程分支名
# 遇到本地冲突，先删除本地分支，再重新拉取远程分支
git branch -D 本地分支名
```
### 将本地分支推送到远程分支上
```bash
git branch --set-upstream-to origin/远程分支名 本地分支名
```
### stash 缓存修改
ref: [git-stash用法小结](https://www.cnblogs.com/tocy/p/git-stash-reference.html)  
`git stash`（git储藏）可用于以下情形：
- 发现有一个类是多余的，想删掉它又担心以后需要查看它的代码，想保存它但又不想增加一个脏的提交。这时就可以考虑`git stash`。
- 使用git的时候，我们往往使用分支（branch）解决任务切换问题，例如，我们往往会建一个自己的分支去修改和调试代码, 如果别人或者自己发现原有的分支上有个不得不修改的bug，我们往往会把完成一半的代码`commit`交到本地仓库，然后切换分支去修改bug，改好之后再切换回来。这样的话往往log上会有大量不必要的记录。其实如果我们不想提交完成一半或者不完善的代码，但是却不得不去修改一个紧急Bug，那么使用git stash就可以将你当前未提交到本地（和服务器）的代码推入到Git的栈中，这时候你的工作区间和上一次提交的内容是完全一样的，所以你可以放心的修Bug，等到修完Bug，提交到服务器上后，再使用`git stash apply`将以前一半的工作应用回来。
- 经常有这样的事情发生，当你正在进行项目中某一部分的工作，里面的东西处于一个比较杂乱的状态，而你想转到其他分支上进行一些工作。问题是，你不想提交进行了一半的工作，否则以后你无法回到这个工作点。解决这个问题的办法就是`git stash`命令。储藏(stash)可以获取你工作目录的中间状态——也就是你修改过的被追踪的文件和暂存的变更——并将它保存到一个未完结变更的堆栈中，随时可以重新应用。  

`git stash`用法：  
**1. stash 当前修改**  
默认情况下，`git stash`会缓存下列文件：
- 添加到暂存区的修改（staged changes）
- Git跟踪的但并未添加到暂存区的修改（unstaged changes）

但不会缓存以下文件：
- 在工作目录中新的文件（untracked files）
- 被忽略的文件（ignored files）
`git stash`命令提供了参数用于缓存上面两种类型的文件。使用`-u`或者`--include-untracked`可以stash untracked文件。使用-a或者--all命令可以stash当前目录下的所有修改。
`git stash`会把所有未提交的修改（包括暂存的和非暂存的）都保存起来，用于后续恢复当前工作目录。  
比如下面的中间状态，通过git stash命令推送一个新的储藏，当前的工作目录就干净了。
```bash
$ git status
On branch master
Changes to be committed:

new file:   style.css

Changes not staged for commit:

modified:   index.html

$ git stash
Saved working directory and index state WIP on master: 5002d47 our new homepage
HEAD is now at 5002d47 our new homepage

$ git status
On branch master
nothing to commit, working tree clean
```
需要说明一点，stash是本地的，不会通过`git push`命令上传到git server上。
实际应用中推荐给每个stash加一个message，用于记录版本，使用`git stash save`取代`git stash`命令。示例如下：
```bash
$ git stash save "test-cmd-stash"
Saved working directory and index state On autoswitch: test-cmd-stash
HEAD 现在位于 296e8d4 remove unnecessary postion reset in onResume function
$ git stash list
stash@{0}: On autoswitch: test-cmd-stash
```
**2. 重新应用缓存的stash**  
使用`stash pop` 或`stash apply`：
```bash
 git status
On branch master
nothing to commit, working tree clean
# git stash pop 将缓存堆栈中的第一个stash删除，并将对应修改应用到当前的工作目录下。
$ git stash pop
On branch master
Changes to be committed:

    new file:   style.css

Changes not staged for commit:

    modified:   index.html

Dropped refs/stash@{0} (32b3aa1d185dfe6d57b3c3cc3b32cbf3e380cc6a)
# git stash apply 将缓存堆栈中的stash多次应用到工作目录中，但并不删除stash拷贝。
# 在使用git stash apply命令时可以通过名字指定使用哪个stash，默认使用最近的stash（即stash@{0}）。
$ git stash apply
On branch master
Changes to be committed:

    new file:   style.css

Changes not staged for commit:

    modified:   index.html
```
**3. 查看现有stash**  
```bash
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```
**4. remove existing stash**   
```bash
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
$ git stash drop stash@{0}
Dropped stash@{0} (364e91f3f268f0900bc3ee613f9f733e82aaed43)
```
查看指定stash的diff、从stash创建分支见ref: [git-stash用法小结](https://www.cnblogs.com/tocy/p/git-stash-reference.html)  

# 恢复被误删的文件！！
ref: https://juejin.cn/post/7174989433593626661
![image](https://github.com/elifzeng/Computory-Background/assets/52747634/ff2d5b74-2788-4c9b-93a8-0dab7499675a)  
 ![image](https://github.com/elifzeng/Computory-Background/assets/52747634/fe27c900-0469-4726-a4f3-24802972c4ac)  
 ![image](https://github.com/elifzeng/Computory-Background/assets/52747634/d333c04d-2d3e-420c-bc3b-2894dbd7fef7)  
 




