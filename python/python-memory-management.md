# [深入python内存管理](https://zz.zzs7.top/python-memory-management.html)

python有自己的内存管理机制，有自己的垃圾回收机制  

python内存管理是由**私有堆空间**管理的，所有的python对象和数据结构都存储在私有堆空间中。程序员**没有访问堆的权限**，只有解释器才能操作。为python的堆空
间分配内存的是python的内存管理模块进行的，核心[api](https://baike.baidu.com/item/api/10154)会提供一些访问该模块的方法供程序员使用。python自有的
[垃圾回收机制](https://www.jianshu.com/p/e5447d4d1cc6)回收并释放没有被使用的内存共别的程序使用。  

在python中，整数和短小的字符都会作为对象被缓存，以便重复使用。  

**Notice**  
对于孤立引用环的解决办法，会出现悬空引用的问题，详见[此处](https://www.javazhiyin.com/23191.html)（六）（七）
