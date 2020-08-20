## 说些废话
似曾相识的巧合，昨天在不同的地方看到三句相似的话：
> 完美是优秀的敌人 ————《算法图解》
> We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. – Donald Knuth  
> 第三句我给忘了。 ————啊这。。。

总之，**算法优化**是在写完程序，运行后发现问题比较大的时候突破性能瓶颈用的，好是好，可不要贪杯噢。  
这篇文算是记录我第一次实战算法优化的记录，程序性能分析是软件工程的内容，咱也搞不懂，就按到按到来吧。参考[这篇](https://zhuanlan.zhihu.com/p/24495603)知乎文章。  

## 关于性能分析
[wiki](https://zh.wikipedia.org/zh-cn/%E6%80%A7%E8%83%BD%E5%88%86%E6%9E%90)  
性能分析（performance analysis/ profiling）是以收集程序运行时信息为手段研究程序行为的分析方法，它**分析的是**代码和正在使用的资源之间有怎样的联系，分析**工具**一般为各种性能分析器（profiler）。Python内置的性能分析器为`cProfiler`，本文就用它来分析和优化我的程序。  

## cProfiler
### 快速使用
官方文档的一个简例：  
```python
import cProfile
import re # 提供各种正则表达式的匹配操作
# re.compile()用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
cProfile.run('re.compile("foo|bar")') 
```
---

`这里插播一个关于re的小例子便于理解`，关于 _re_ 的详细内容见[这里](https://www.runoob.com/python/python-reg-expressions.html)和[官方文档](https://docs.python.org/zh-cn/3/library/re.html)。   

![image](https://user-images.githubusercontent.com/52747634/90585250-f9644280-e206-11ea-80de-cf4b295d25c1.png)
![image](https://user-images.githubusercontent.com/52747634/90585274-0ed96c80-e207-11ea-95f7-cf6911526eb6.png)  
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

分析结果(截取片段)：
```
         244 function calls (237 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 enum.py:284(__call__)
        2    0.000    0.000    0.000    0.000 enum.py:526(__new__)
        9    0.000    0.000    0.000    0.000 enum.py:623(name)
        1    0.000    0.000    0.000    0.000 enum.py:793(_missing_)
        1    0.000    0.000    0.000    0.000 enum.py:800(_create_pseudo_member_)
        1    0.000    0.000    0.000    0.000 enum.py:836(__and__)
        1    0.000    0.000    0.000    0.000 enum.py:872(_decompose)
        1    0.000    0.000    0.000    0.000 enum.py:890(<listcomp>)
        1    0.000    0.000    0.000    0.000 re.py:232(compile)
        1    0.000    0.000    0.000    0.000 re.py:271(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
        1    0.000    0.000    0.000    0.000 sre_compile.py:276(_optimize_charset)
        2    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
        1    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:536(_compile_info)
        2    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
        1    0.000    0.000    0.000    0.000 sre_compile.py:598(_code)
      3/1    0.000    0.000    0.000    0.000 sre_compile.py:71(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:759(compile)
        3    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
        7    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
       18    0.000    0.000    0.000    0.000 sre_parse.py:164(__getitem__)
```

由上述结果：
1. 整个过程一共244个函数调用被监控，其中237个是原生调用（即不涉及递归调用）
2. 总的执行时间为0.000秒
3. 结果列表中是按照标准名称进行排序，也就是按照字符串的打印方式（数字也当作字符串）
4. 在列表中:
    - ncalls 为函数调用次数
    - tottime 为函数内部调用时间（不包括他自己调用其他函数的时间）
    - percall等于tottime/ncalls
    - cumtime累积调用时间，与tottime相反，包含了自己内部调用函数的时间
    - 最后一列，文件名，行号，函数名

---
### 知识补充
以下是一些对原博客中的知识补充，为什么不继续照搬呢？因为我菜，看不懂了。  
1. about [*args&**kwargs](https://www.jianshu.com/p/be92113116c8)
*Notice*:文中`d.iteritems()`方法已被python3弃用，现在使用d.items()就可以了。
2. about [decorator](https://www.liaoxuefeng.com/wiki/1016959663602400/1017451662295584)  简而言之，装饰器的目的就是增强函数功能的同时不去修改该函数的定义。
*Notice*:通过写一个带参数的装饰器，就可以分析项目中的任何一个函数。当然，这需要`cProfile`和`pstats`作为接口。
3. about module [pstats](https://docs.python.org/3/library/profile.html). pstats模块是python用来分析cProfile输出的二进制文件内容的。
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

对文中的性能分析装饰器进行注释：
```python
import cProfile
import pstats
import os
# 性能分析装饰器定义
def do_cprofile(filename):
    """
    Decorator for function profiling.
    """
    def wrapper(func):
        def profiled_func(*args, **kwargs):
            # Flag for do profiling or not.
            # sys.getenv()方法用来获取环境变量，判断是否需要进行分析，因此可以通过设置环境变量“export PROFILING=y”来告诉程序是否进行性能分析。
            DO_PROF = os.getenv("PROFILING") 
            if DO_PROF:
                profile = cProfile.Profile() # 创建一个cProfile对象
                profile.enable() # 开始收集性能分析数据
                result = func(*args, **kwargs) # 运行一遍目标函数
                profile.disable() # 停止收集性能分析数据
                # Sort stat by internal time.
                sortby = "tottime"
                ps = pstats.Stats(profile).sort_stats(sortby) # sort_stats(*keys)对报告列表进行排序，函数会依次按照传入的参数排序，关键词包括calls, cumtime等
                ps.dump_stats(filename) # 把stats中的分析数据写入文件（二进制格式）
            else: # 环境变量不匹配时不进行性能分析。
                result = func(*args, **kwargs)
            return result # 其实这里可以写成return func(*args, **kwargs)
        return profiled_func
    return wrapper
```

这样就可以在想进行性能分析的地方进行性能分析，例如我想分析MicroKineticModel类中的run方法：
```python
class MicroKineticModel(km.KineticModel):
    # ...
    # 应用装饰器来分析函数
    @do_cprofile("./mkm_run.prof")
    def run(self, **kwargs):
        # ...
```
好了我先找个简单的程序试试（测试程序在`python/profile_test/`下）。  

#### 另一种方法
其实也可以使用cprofile直接对现有程序进行概要分析，在没有检测某几个特定函数的需求时，直接在`bash`输入：  
`python -m cProfile -o outputfile.prof pythonfile.py`

### 性能分析实践
按照上文的方法，实现了通过装饰器对`fact`函数进行修饰来进行性能分析。现在，在正常运行程序的同时，指定路径下还会生成性能分析报告文件`prof_test.prof`。该文件是一个二进制文件，需要用python的pstats模块的接口来读取。

```python
""" ipython maybe more convenient
"""
import pstats
p = pstats.Stats('prof_test.prof')
p.strip_dirs().sort_stats('cumtime').print_stats(10, 1.0, '.*')
# strip_dirs()删除报告中所有函数文件名的路径信息
# sort_stats(*keys) 对报告列表进行排序，函数会依次按照传入的参数排序
# print_stats(*restrictions) 把信息打印到标准输出。*restrictions用于控制打印结果的形式，例如（10, 1.0, '.*。py.*'）表示打印所有py文件的信息的前10行结果。
```
output:  

![image](https://user-images.githubusercontent.com/52747634/90707812-f3d03080-e2ca-11ea-8920-91c5a9eda6be.png)  

直接看数据表可能不太直观，当数据量很多时也不方便分析，这时候可视化就很香了。

### 分析数据可视化
文中介绍了4种可视化工具，我选择的是[gprof2dot](https://github.com/jrfonseca/gprof2dot)。  
```
sudo yum install python3 graphviz 
pip install grof2dot # install grof2dot  
gprof2dot -f pstats prof_test.prof | dot -Tpng -o prof_test.png
```

生成图片：  
<div align=center><img src="https://user-images.githubusercontent.com/52747634/90721864-4a9a3200-e2ec-11ea-8ce7-ae8ce3dc33c4.png" /></div>

#### Output
接下来的内容摘自[gprof2dot](https://github.com/jrfonseca/gprof2dot) github官方文档。  
A node in the output graph represents a function and has the following layout:
```
+------------------------------+  
|       function name          |  
| total time % ( self time % ) |  
|         total calls          |  
+------------------------------+
```
where:  

- total time % is the percentage of the running time spent in this function and all its children;
- self time % is the percentage of the running time spent in this function alone;
- total calls is the total number of times this function was called (including recursive calls).

An edge represents the calls between two functions and has the following layout:
```

           total time %
              calls
parent --------------------> children
```

Where:  

- total time % is the percentage of the running time transfered from the children to this parent (if available);
- calls is the number of calls the parent function called the children.

*Note* that in recursive cycles, the total time % in the node is the same for the whole functions in the cycle, and there is no total time % figure in the edges inside the cycle, since such figure would make no sense.

The color of the nodes and edges varies according to the total time % value. In the default temperature-like color-map, functions where most time is spent (hot-spots) are marked as saturated red, and functions where little time is spent are marked as dark blue. Note that functions where negligible or no time is spent do not appear in the graph by default.
