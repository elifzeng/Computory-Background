# Module argparse
[official tutorial](https://docs.python.org/zh-cn/3.7/library/argparse.html) and a [CDSN blog](https://blog.csdn.net/Sunshine_in_Moon/article/details/51332931)  

argparse --- 命令行选项、参数和子命令解析器  

**位置参数**(positional arguments)。之所以这样命名，是因为程序应该如何处理该参数值，完全取决于它在命令行出现的位置。更能体现这个概念的命令如 `cp`，它最基本的
用法是 `cp SRC DEST`。第一个位置参数指的是*你想要复制的*，第二个位置参数指的是你想要复制到的位置。  

**可选参数**(optional arguments)。现在假设我们想要改变这个程序的行为。例如命令行`ls -l`，我们不仅仅只是输出每个文件的文件名，还输出了更多信息。
在这个例子中，`-l`被称为可选参数。

```python
import argparse
parser = argparse.ArgumentParser(description=__doc__)
```
方法ArgumentParser(prog=None, usage=None,description=None, epilog=None, parents=[],formatter_class=argparse.HelpFormatter, prefix_chars='-',fromfile_prefix_chars=None, argument_default=None,conflict_handler='error', add_help=True)  

这些参数都有默认值，当调用parser.print_help()或者运行程序时由于参数不正确(此时python解释器其实也是调用了pring_help()方法)时，会打印这些描述信息，一般只需要传递description参数。这个方法相当于一个构造函数，初始化一个对象，里面使用最多的参数就是description，用于描述该程序，`__doc__`返回该文件名称，也可以是`parser = argparse.ArgumentParser(description="the usage of the program")`。 

*Notice*  help是自带可选参数。
```python
parser.add_argument("-c",
                    "--charge",
                    type=int,
                    default=0,
                    help="total charge of fragment.")
parser.add_argument("square", help="display a square of a given number",type=int)
parser.add_argument('--noHopt',
                    action="store_true",
                    help="Hs will not add/opt with PLOP.")
args = parser.parse_args()
```
The `parse_args()` method actually returns some data from the options specified.  
比如在上述例子中，`arg.square`会返回square选项对应的值（此处`square`是一个位置参数）。而`arg.charge`会返回charge选项对应的值或布尔值，
这取决于`add_argument`中设置的参数（此处`charge`是一个可选参数）  
**Notice**在终端运行时，输入选项(option)不讲究顺序。  

add_argument()中的参数详见[here](https://docs.python.org/zh-cn/3.7/library/argparse.html#the-add-argument-method)  
`help = ""` 添加帮助信息，在输入`python program_name -h` 时打印出来。  
 `type = ` 指定该参数应该输入的值的类型。  
 `action = ` action 命名参数指定了这个命令行参数应当如何处理。
 如`action = store_true` 表示默认值为`False`当调用该选项时为`True`。**注意**这里不要搞混。`action = 'count'`count the number of occurrences of a specific optional arguments.即输入`python name -c` / `python name -cc` 结果不同。  
 `"-v","--version"` 设定选项缩写。  
 `choices = ` restricting the values the option can accept.    
 `nargs = '+'`  命令行参数应当消耗的数目。`ArgumentParser` 对象通常关联一个单独的命令行参数到一个单独的被执行的动作。 `nargs` 命名参数关联不同数目的命令行参数到单一动作。'+'。和 '\*' 类似，所有当前命令行参数被聚集到一个列表中。另外，当前没有至少一个命令行参数时会产生一个错误信息。  
 
 
