# Jupyter
JupyterLab is the next-generation web-based user interface for Project Jupyter. [There](https://jupyterlab.readthedocs.io/en/stable/) is the official document.  
I've tried `Jupyterlab` on windows10 and here are some notes about it.
## Installation
I've tried to install `Jupyterlab` by two ways: 
1. cmd console with python 3.8 installed: `pip install Jupyterlab`
2. Anoconda
And I find `Anoconda` is more convenient. The steps are just installing Anoconda and open Jupyterlab.
## Change the opening folder of Jupyter
Jupyter 默认起始文件夹为`C:\Users\Administor`, 而且好像没法跳转到其他文件夹。[更改](https://zhuanlan.zhihu.com/p/43786555)默认起始文件夹方法如下：
#### 1. Find the path of jupyter_notebook_config.py  
Open `CMD.exe Prompt` from Anoconda and input
```cmd
>>>jupyter-lab --generate-config
Writing default config to:C:\Users\UserName\.jupyter\jupyter_notebook_config.py
```
And the second line tells us the path we are looking for.  
#### 2. Change the openning fold path  
Open `jupyter_notebook_config.py` and find this line: `#c.NotebookApp.notebook_dir = ''`  
Then remove the `#` and change it to `c.NotebookApp.notebook_dir = 'E:\Jupyter`  
_The folder you added should have existed._  
done!

## Usage
`Shift + Enter`

## Change python kernel
_我真的服了，有两个要用的模块nglview和mdtraj，前者不能在vscode上用，后者不能在python 3.7里用，为了解决前面那个问题，我搞了Jupyter,对于后面那个问题，Jupyter默认python内核为3.7，所以我打算在Jupyter里再装一个python3.6的内核，然后再安装各个包再撸脚本，啊，又学到新知识真是令人开心呢。。。_
_我靠我成功了，我太开心了_  
Reference [1](https://stackoverflow.com/questions/43759610/how-to-add-python-3-6-kernel-alongside-3-5-on-jupyter) and [2](https://blog.stefanproell.at/2016/12/16/switching-kernels-using-python-2-7-and-python-3-5-in-jupyter-notebooks/)  
Open `CMD.exe Prompt` from Anoconda and input
'''cmd
conda install ipykernel
conda create -n Python3.6 python=3.6 # 创建一个内核为python3.6的，名字叫Python3.6的环境
conda activate Python3.6 # 启用该环境，此时可以看到，命令提示符最左侧变为(Python3.6)
python -m pip install --upgrade ipykernel # '-m' means 'module', 'python -m pip' tells python to run with the pip module as the main module since 'python pip' isn't understood, because pip isn't a command line argument that python understands (i.e., pip is a module).
python -m ipykernel install --name Python3.6 # 新建了一个名字为Python3.6，内核为python3.6的内核
'''
然后打开`Jupyterlab`，在菜单栏`Kernel`下拉菜单中选择`change kernel`，然后选择刚刚建的`Python3.6`，就行了。  
![image](https://user-images.githubusercontent.com/52747634/77303321-bc665380-6d2d-11ea-8e7e-a6d4770b17db.png)



