[link](https://www.cnblogs.com/qvduoduo/p/6148523.html)  
# APT
 高级包装工具（英语：Advanced Packaging Tools,简称：APT）是**Debian**及其衍生发行版（如：ubuntu）的软件包管理器。
 APT可以自动下载，配置，安装二进制或者源代码格式的软 件包，因此简化了 Unix系统上管理软件的过程。  
 ### apt-get
`apt-get` 是一个下载安装软件包的简单命令行接口。 最常用的命令是update(更新) 和install(安装)。    
 ### apt-file
 `apt-file`是一个软件包查找工具，可以查到软件包所含的文件和安装的位置。（ps：据说是解决依赖的利器）
 # YUM
 YUM（Yellowdog Updater Modified）是一款开源命令行及图形化软件包管理工具，面向基于**RPM**（红帽软件包管理器）的Linux系统。
  它让广大用户和系统管理员可以在系统上轻松地安装、更新、移除或搜索软件包。它由Seth Vidal开发和发布,
  采用了GPL（通用公共许可证），是一款开源工具。这意味着，谁都可以下载和访问代码，以修复软件错误，开发定制的软件包。
  YUM通过解决软件包的依赖项问题,使用众多的第三方软件库来自动安装软件包。  
 ```bash
 yum install firefox
 yum remove firefox
 yum deplist firefox # 查看依赖
 yum grouplist # 列出所有的可用群组软件包
 yum repolist # 列出启用的Yum软件库
 yum history # 查看Yum的历史记录
 yum search firefox # 搜索软件包
 ```
 # [DNF](https://www.linuxdashen.com/yum%e5%b7%b2%e6%ad%bb%ef%bc%8cdnf%e4%b8%87%e5%b2%81)
DNF新一代的RPM软件包管理器。他首先出现在 **Fedora 18** 这个发行版中。而最近，他取代了YUM，正式成为 Fedora 22 的包管理器。  
DNF包管理器克服了YUM包管理器的一些瓶颈，提升了包括用户体验，内存占用，依赖分析，运行速度等多方面的内容。  
DNF使用 RPM, libsolv 和 hawkey 库进行包管理操作。尽管它没有预装在 CentOS 和 RHEL 7 中，
但你可以在使用YUM的同时使用 DNF 。  
## dnf usage
```bash
# install dnf (RHEL/CentOS/Scientific Linux need this)
yum install epel-release # 安装DNF前必须先安装并启用epel-release依赖
yum install dnf # 使用epel-release依赖中的yum命令安装DNF包
dnf --version # 查看安装在系统走过的DNF包管理器版本
dnf repolist # 显示系统中可用的DNF软件库
# fedora 更新
sudo dnf install dnf-plugin-system-upfrade
sudo dnf system-upgrade download --releasever=24 --best --nogpgcheck --allowerasing
sudo dnf system-upgrade reboot
# some usage, similiar to yum
sudo dnf install firefox
sudo dnf remove firefox
sudo dnf update # 升级软件
sudo dnf update # 升级系统
sudo dnf clean packages # 清除RPM包缓存
```
see more in `man dnf`.
## why use dnf
1. 很好地解决了依赖问题，效率更高（依赖的包会自动安装，卸载时会将依赖包一起卸载）
2. 完全由python3 写成，系统中可以不必python2和3共存，而yum必须有python2。
3. 由于`fedora`软件仓库是连续维护的，dnf适合大版本升级。
