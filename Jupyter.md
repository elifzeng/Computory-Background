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
```bash
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
