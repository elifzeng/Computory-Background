### python调用系统命令popen、system
[ref](https://www.cnblogs.com/MrLJC/p/3811106.html)  
python调用shell有两种方法：`os.system()`或`os.popen()`，前者返回值是脚本的**退出状态码**，后者返回值是脚本执行过程中的**输出内容**。所以一般认为
popen更加强大。
#### os.system(cmd):
该方法在调用完shell脚本后，返回一个16位的二进制数，低位为杀死所调用脚本的信号号码，高位为脚本的退出状态码，即脚本中“exit 1”的代码执行后，os.system函数返回值的
高位数则是1，如果低位数是0的情况下，则函数的返回值是0×100,换算为10进制得到256。

#### os.popen(cmd):
这种调用方式是通过管道的方式来实现，函数返回一个file-like的对象(所以可以用read()来读取)，里面的内容是脚本输出的内容（可简单理解为echo输出的内容）。  
实例如下：
```python
1 import numpy
2 import os
3 t=os.popen('ls')
4 print(t.read())
7 popen.close()
5 t=os.system('ls')
6 print(t)
```
输出如下：  

![image](https://user-images.githubusercontent.com/52747634/92049712-bf29a200-edbd-11ea-8d25-6130cf9050fd.png)
![image](https://user-images.githubusercontent.com/52747634/92053331-3c561680-edc0-11ea-82fe-af82ec4d1562.png)

> 注意这里有一个小彩蛋。python file read() 函数为按字节（字符）读取文件。当第二次调用read()时返回内容为空。这是因为调用read()的操作内容是：
读取整个文件并将读取光标留在文件的末尾（没有更多内容可读）。如果想一次读取一定数量的行就用readline(), readlines()或者使用行迭代 for line in handle:。

> 此外ia，也可以用seek(0)将读取光标返回文件的开头。如果文件不大，还可以将read()输出保存到变量中，并在findall表达式中使用它。实例如下：

```bash
>>> a = open('file.txt')
>>> a.read()
#output
>>> a.seek(0)
>>> a.read()
#same output
```
[ref](https://segmentfault.com/q/1010000017024076)  
[这里](http://c.biancheng.net/view/2545.html)有另一篇讲解和使用read()的文章。  

**多说一句**  
原文中还提到了官方建议用`subprocess`的`Popen`替换os.popen()，具体的以后再研究吧（挖坑警告）。
