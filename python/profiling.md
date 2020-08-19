### 说些废话
似曾相识的巧合，昨天在不同的地方看到三句相似的话：
> 完美是优秀的敌人 ————《算法图解》
> We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. – Donald Knuth
> 第三句我给忘了。 ————啊这。。。

总之，**算法优化**是在写完程序，运行后发现问题比较大的时候突破性能瓶颈用的，好是好，可不要贪杯噢。  
这篇文算是记录我第一次实战算法优化的记录吧，程序性能分析是软件工程的内容，咱也搞不懂，就按到按到来吧。参考[这篇](https://zhuanlan.zhihu.com/p/24495603)知乎文章。  

### 关于性能分析
[wiki](https://zh.wikipedia.org/zh-cn/%E6%80%A7%E8%83%BD%E5%88%86%E6%9E%90)  
性能分析（performance analysis/ profiling）是以收集程序运行时信息为手段研究程序行为的分析方法，它**分析的是**代码和正在使用的资源之间有怎样的联系，分析**工具**一般为各种性能分析器（profiler）。Python内置的性能分析器为`cProfiler`，本文就用它来分析和优化我的程序。  

### cProfiler
#### 快速使用
官方文档的一个简例：  
```python
import cProfile
import re
cProfile.run('re.compile("foo|bar")')
```
