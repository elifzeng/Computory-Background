# Uninstall and install Anaconda
_由于实验室集群为centos，此处以centos为例—_
[CentOS安装/卸载Anaconda（图文详解）](https://cloud.tencent.com/developer/article/2065512)  
## Uninstall
直接删除anaconda3文件夹，注意，如果要重装，注意保留版本信息和包信息。
```bash
rm -rfv ~/anaconda3
# 清理.bashrc中的anaconda路径
vim ~/.bashrc
# del PATH=/yourInstallPath/anaconda3/bin:$PATH
source ~/.bashrc
# 重启terminal
```
## Install
1. 在[官方](https://docs.anaconda.com/anaconda/packages/oldpkglists/)查看版本信息，找到需要的版本并下载。条件不允许时可在[清华源](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)下载。查看linux架构：`cat /proc/version`    
查看anaconda版本不是用`--version`（这查的是conda的版本），而是用[这种方法](https://blog.csdn.net/zhr199970910/article/details/109902946)：  
![image](https://user-images.githubusercontent.com/52747634/197928639-63cd0f83-6be5-4cf0-bb59-2951e44b1cc2.png)

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
# or 清华源
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2021.05-Linux-x86_64.sh
```
2. 安装Anaconda
```bash
bash Anaconda3-2021.05-Linux-x86_64.sh
# press ENTER fot "Please, press ENTER to continue"
# input yes for "Do you accept the license terms? [yes|no]"
# press ENTER or input specific location for "Anaconda3 will now be installed into this location:"
# input yes for "Do you wish the installer to initialize Anaconda3 by running conda init? [yes|no]"
```
安装conda后可能会重置环境变量`$PS1`:
```bash
$conda activate mummer4
(mummer4)
```
即不显示`[用户名@主机名 当前路径]$`。解决办法：
针对单一虚拟环境设置：
```bash
$conda activate mummer4
$conda env config vars set PS1='($CONDA_DEFAULT_ENV)[\u@\h \W]$'
$conda deactivate
$conda activate mummer4
(mummer4)[user1@login1 ~/temp]$pwd
```
参考:https://zhuanlan.zhihu.com/p/572716915  
针对全局虚拟环境设置：
```bash
conda config --set env_prompt "({default_env})[\u@\h \W]$"
```
3. 添加环境
```bash
source ~/.bashrc
```
完成base环境地添加。若未能添加成功，可以手动添加环境变量
```bash
export PATH=/yourInstallPath/anaconda3/bin:$PATH
source ~/.bashrc
```

# Create a virtual environment for your project
[see more](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)
```bash
$ conda create -n yourenvname python=X.Y.Z anaconda
```
and activate the environment
```bash
$ conda activate yourenvname
```
## Install additional Python packages to a virtual environment
```bash
$ conda install -n yourenvname [package]
```
## Deactivate a virtual environment
```bash
$ conda deactivate
```
## Delete a no longer needed virtual environment
```bash
$ conda env remove -n yourenvname
```
## List environment you created 
```bash
conda env list
```
## Auto activate virtual environment in Visual Studio Code
![image](https://user-images.githubusercontent.com/52747634/205565018-42a95c34-cf05-4d03-bc07-d386d9555d66.png)

# Install some package or version not in official library with [conda-forge](https://github.com/conda-forge/conda-forge.github.io)
what's [conda-forge](https://cloud.tencent.com/developer/article/1035806) ?
```bash
conda install [package] -c conda-forge 
```
## Check available package version 
```bash
conda search package
```
## Export conda or pip environment & install env with export file
### conda
```bash
# export
conda env export > environment.yaml
# install
conda env create -f environment.yaml
# update existed env with .yaml file
conda env update -n my_env --file ENV.yaml
```
### pip
```bash
# export
pip freeze >requirements.txt
# install
pip install -r requirements.txt
```

## Install miniconda
https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html#install-macos-silent
## 将一些环境变量和virtual environment绑定在一起
https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#macos-and-linux
## CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
```
# error output
[nibs_nhuang_1@lon26:bin]$ ./conda activate base

CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'. 
```
解决办法：
```bash
1  首先终端输入 source activate

2 然后终端输入 source deactivate

3 输入你要激活的虚拟环境指令 conda activate your_virtual_name
```
## environments I usuallly use
```bash
#since now htmd only support python <=3.8.0.a1
conda create -n python python=3.7
conda install -c acellera -c conda-forge htmd
htmd_register
conda install -c conda-forge ase -y
conda create -n chemtools
conda activate chemtools
conda create -n chemtools -c conda-forge rdkit ambertools
conda install --name chemtools pylint -y
/home/zenglj/opt/miniconda/envs/chemtools/bin/python /home/zenglj/.vscode-server/extensions/ms-python.python-2021.1.502429796/pythonFiles/pyvsc-run-isolated.py /home/zenglj/.vscode-server/extensions/ms-python.python-2021.1.502429796/pythonFiles/shell_exec.py conda install --name chemtools ipykernel -y /tmp/tmp-7649pNQu3yEeN5vE.log
/home/zenglj/opt/miniconda/envs/chemtools/bin/python
source activate /home/zenglj/opt/miniconda/envs/chemtools
conda create -n qm
conda install --name qm pylint -y
# the context of the two .sh file is shown below
cat /home/zenglj/opt/miniconda/envs/qm/etc/conda/activate.d/env_vars.sh
cat /home/zenglj/opt/miniconda/envs/qm/etc/conda/deactivate.d/env_vars.sh
conda create -n deepchem python=3.7 anaconda
conda activate deepchem
conda install -c rdkit rdkit

```
and the `.bashrc`  
```bash
(base) [zenglj@x021 ~]$ cat .bashrc
# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/zenglj/opt/miniconda/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/zenglj/opt/miniconda/etc/profile.d/conda.sh" ]; then
        . "/home/zenglj/opt/miniconda/etc/profile.d/conda.sh"
    else
        export PATH="/home/zenglj/opt/miniconda/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

# User specific environment
export PATH=/home/zenglj/Downloads/plop25:$PATH

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions

# #NMRCLUST
# export PATH='/home/zenglj/data/nmrclust':$PATH
# alias nmrclust='/home/zenglj/data/nmrclust/nmrclust'
```
```bash
(base) [zenglj@x021 OptProgram]$ cat /home/zenglj/opt/miniconda/envs/qm/etc/conda/activate.d/env_vars.sh
#!/bin/sh

# Quantum Chem

# Gaussian
export g16root=/home/zenglj/gaussian
export GAUSS_SCRDIR=/home/zenglj/gaussian/g16/scratch
source /home/zenglj/gaussian/g16/bsd/g16.profile

# fullspace
# export PYTHONPATH=$PYTHONPATH:/home/zenglj/git/fullspace/examples/grepPDB/fpdb

# Orca
export PATH=/home/zenglj/data/orca_4_1_2:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/zenglj/data/orca_4_1_2
export ORCA_PATH=/home/zenglj/data/orca_4_1_2
alias orca='/home/zenglj/data/orca_4_1_2'

# Vaspkit
export PATH=$HOME/opt/vaspkit.1.2.4/bin:$PATH
```
```bash
(base) [zenglj@x021 OptProgram]$ cat /home/zenglj/opt/miniconda/envs/qm/etc/conda/deactivate.d/env_vars.sh
#!/bin/sh

echo "It's hard to undo the changes which g16.profile makes on like \$PATH, \$LD_LIBRARY_PATH and so on."
echo "Please exit this shell and open a new one".
```
