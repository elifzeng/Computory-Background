# Python 多线程与多进程

## 关于线程与进程的区别、Python全局解释器锁GIL

[a detailed ref](https://mp.weixin.qq.com/s/i3RvQc5uI9dVZ82pcwOQsQ)

## Python的多进程包multiprocessing

### multiprocessing产生背景

linux 系统中的父进程和子进程见`/home/elifzeng/Computory-Background/python/Multiprocessing_and_multithreading/Multiprocessing.py`. windows无fork调用，由于Python是跨平台的，其需要提供一个跨平台的多进程支持。而multiprocessing就是跨平台版本的多进程模块，其封装了fork()的调用，在windows上也可以“模拟“出fork的效果。

### multiprocessing 常用组件及功能

multiprocessing : Process, Queue, Pool, Lock  

创建管理进程模块：

1. Process (用于创建进程)
2. Pool (用于创建管理进程池)
3. Queue (用于进程通信，资源共享)
4. Value, Array (用于进程通信，资源共享)
5. Pipe (用于管道通信)
6. Manager (用于资源共享)

同步子进程模块：

1. Condition (条件变量)
2. Event (事件)
3. Lock (互斥锁)
4. RLock (可重入的互斥锁(同一个进程可以多次获得它，同时不会造成阻塞))
5. Semaphore(信号量)

detailed usage can be seen [here](https://mp.weixin.qq.com/s/i3RvQc5uI9dVZ82pcwOQsQ)  
examples can be seen in `/home/elifzeng/Computory-Background/python/Multiprocessing_and_multithreading/Multiprocessing.py`  

### [守护进程](https://blog.csdn.net/u012063703/article/details/51601579)

如果你设置一个线程为守护线程，，就表示你在说这个线程是不重要的，在进程退出的时候，不用等待这个线程退出。  
如果你的主线程在退出的时候，不用等待那些子线程完成，那就设置这些线程的daemon属性。即，在线程开始（thread.start()）之前，调用setDeamon（）函数，设定线程的daemon标志。（thread.setDaemon(True)）就表示这个线程“不重要”。  
如果你想等待子线程完成再退出，那就什么都不用做。，或者显示地调用thread.setDaemon(False)，设置daemon的值为false。新的子线程会继承父线程的daemon标志。整个Python会在所有的非守护线程退出后才会结束，即进程中没有非守护线程存在的时候才结束。  

## Python并发之concurrent.futures

(这部分有点太难了，先不管)

Python标准库为我们提供了threading和multiprocessing模块编写相应的多线程/多进程代码。从Python3.2开始，标准库为我们提供了concurrent.futures模块，它提供了ThreadPoolExecutor和ProcessPoolExecutor两个类，实现了对threading和multiprocessing的更高级的抽象，对编写线程池/进程池提供了直接的支持。concurrent.futures基础模块是executor和future.  

1. Executor
2. Future

**Executor**是一个抽象类，它不能被直接使用。它为具体的异步执行定义了一些基本的方法。  ThreadPoolExecutor和ProcessPoolExecutor继承了Executor，分别被用来创建线程池和进程池的代码。  

Future可以理解为一个在未来完成的操作，这是异步编程的基础。通常情况下，我们执行io操作，访问url时（如下）在等待结果返回之前会产生阻塞，cpu不能做其他事情，而Future的引入帮助我们在等待的这段时间可以完成其他的操作。  
