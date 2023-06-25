```bash
export PYTHONPATH=$PYTHONPATH:/home/zenglj/git/fullspace/examples/grepPDB
./a.py
# 之后在grepPDB下运行`.py`就不用输入`python`了。如第二行直接输入`.py`文件路径即可。
```

有时不知道某个class里有哪些方法，可用`ipython Tab`或者`dir(object)`查看可用方法。
```python
import fpdb
# 报错 : ModuleNotFoundError: No module named 'fpdb'
```
此时在terminal中运行, ` export PYTHONPATH=$PYTHONPATH:/home/zenglj/git/fullspace/examples/grepPDB/fpdb`，即可。




# Something I wrote before
[link](https://github.com/elifzeng/extract-fragment/blob/master/README.md)  
There are things about   
**f-string (python格式化字符)**   
some packages including   
**from rdkit import Chem**  
**import re** Regular Expression 一种文本解析工具，用于提供各种正则表达式的匹配操作  
**import sys** sys means system 系统相关的信息模块（有很多函数）  
**from io import StringIO** 在`内存`中读写str  
**import argparse12** [see_also](https://www.jianshu.com/p/fef2d215b91d) 解析bash命令行的包  
**import gzip** 解压缩和压缩文件，读写压缩文件  
**from multiprocessing.dummy import Pool** 提供线程池  
**import os** os means operation system (现在多用pathlib替代了)可用于处理文件和目录这些我们日常手动需要做的操作，且可以跨平台  
**from pathlib import Path** 在指定目录下创建字典等，pathlib 本身也很强大  
**import numpy as np** Numpy是Python中科学计算的核心库。它提供了一个高性能的多维数组对象，以及用于处理这些数组的工具。  

## sys.argv  

在terminal中输入

```bash
$python a.py ./tmp/*  b c d
```

./tmp/中有50个文件，此时python中调用  

```python
import sys
sys.argv[2]
```

显示的是./tmp/*中第二个文件，而不是b，也就是说，现在sys.argv长度为1+50+3=54...令人难过(注意，此次第0个输入参数为a.py)  
此时若想迭代./tmp/中的文件，可使用`for i in $(ls ./tmp/*); do python a.py $i a b c; done`  

python是动态类型的语言，对象与引用分离。
```python
a = 1
```
`a` 为引用，`1` 为对象。利用上述赋值语句，将引用`a`指向对象`1`。   

## sys.path
返回包检索路径
```python
>>> print(sys.path)
['', '/pubhome/lzeng/anaconda3/envs/py37/lib/python37.zip', '/pubhome/lzeng/anaconda3/envs/py37/lib/python3.7', '/pubhome/lzeng/anaconda3/envs/py37/lib/python3.7/lib-dynload', '/pubhome/lzeng/.local/lib/python3.7/site-packages', '/pubhome/lzeng/anaconda3/envs/py37/lib/python3.7/site-packages']
```
