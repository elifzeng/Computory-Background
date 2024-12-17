#!/usr/bin/env python
#%%
# Unix/Linux的操作系统提供了一个fork()系统调用，它非常特殊。普通的函数，调用一次，返回一次，但fork()调用一次，返回两次。
# 因为操作系统自动把当前进程（父进程）复制了一份（子进程），然后，分别在父进程和子进程内返回。子进程永远返回0,而父进程返回子进程的ID。
# 这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
# Notice: 本脚本中每一段代码最好复制到单独的脚本中运行，不要在jupyter中运行

# python的os模块封装了常见的系统调用，其中就包括fork,可以在python程序中轻松创建子进程
import os

print(f"Processing {os.getpid()} start...")
# only works on Unix/Linux/Mac

# 调用一次，返回两次，第一次返回父进程pid，第二次返回子进程pid
pid = os.fork()

if pid == 0:
    print(f"I am child process {os.getpid()} and my parent is {os.getppid()}")

else:
    print(f"I {os.getpid()} just created a child process {pid}.")
# %%
# multiprocessing module example

# Process 用于创建进程
from multiprocessing import Process
import os


def run_proc(name):

    print(f"Run child process {name} {os.getpid()}")


if __name__ == "__main__":
    print(f"Parent process {os.getpid()}")
    # in multiprocessing, 每一个进程都用一个Process类来表示
    # Process(target=函数名字，args=(), name, kwargs), target:加进程调用的函数名，name,进程的名字，args：元组参数，如果参数就一个，记得加逗号
    p = Process(target=run_proc, args=("test",))
    print("Child process will start.")
    # start() 启动进程，并调用该子进程中的p.run()
    # run() 进程启动时运行的方法，正是它去调用target指定的函数，自定义类的类中一定要实现该方法
    p.start()
    # join([timeout]) 进程同步， 主进程等待子进程完成后再执行后面的代码。线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。
    # timeout是可选的超时时间（超过这个时间，父进程不再等待子线程，继续往下执行）
    # 需要强调的是，p.join()只能join住start开启的进程，而不能join住run开启的进程
    p.join()

print("Child process end.")

# %%
# Pool 用于创建管理进程池
# Pool类用于需要执行的目标很多，而手动限制进程数量又太繁琐的情况。
# Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到Pool中时，如果池还没满，那么就会创建一个新的进程来执行该请求；
# 但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中的进程结束，就重用进程池中的进程。
# 关于进程池阻塞可以看[这篇博文](https://www.cnblogs.com/tujia/p/13684251.html)，或者/home/elifzeng/Computory-Background/python/Multiprocessing_and_multithreading/Thread_Blocking.py

# Pool + map
# map方法适用于只有一个参数的函数。它将一个可迭代对象（如列表）中的每个元素作为参数传递给目标函数，并返回一个结果列表。
from multiprocessing import Pool


def test(i):
    print(i)


if __name__ == "__main__":
    lists = range(100)
    pool = Pool()
    pool.map(test, lists) # 若有输出，此处返回一个list
    print("test")
    pool.close()        # 关闭进程池，不再接受新的进程
    pool.join()         # 主进程阻塞等待子进程的退出

# Pool + starmap
# starmap 方法适用于有多个参数的函数。它将一个可迭代对象中的每个元素（通常是一个元组）解包后作为参数传递给目标函数，并返回一个结果列表。
from multiprocessing import Pool

def multiply(x, y):
    return x * y

if __name__ == '__main__':
    with Pool(4) as p:
        result = p.starmap(multiply, [(1, 2), (3, 4), (5, 6)])
    print(result)  # 输出: [2, 12, 30]
    
# %%
# 异步进程池（非阻塞）
from multiprocessing import Pool


def test(i):
    print(i)


if __name__ == "__main__":

    pool = Pool(8)

    for i in range(100):
        """
        For循环中执行步骤：
        （1）循环遍历，将100个子进程添加到进程池（相对父进程会阻塞）
        （2）每次执行8个子进程，等一个子进程执行完后，立马启动新的子进程（相对父进程不阻塞）
        apply_async为异步进程池写法。异步指的是启动子进程的过程，与父进程本身的执行（print）是异步的，而For循环中往进程池中添加子进程的过程，与父进程本身的执行却是同步的。
        """
        pool.apply_async(
            test, args=(i,)
        )  # 维持执行的进程总数为8, 当一个进程执行完后启动一个新进程。运行效果是先运行了print('test')之后，再运行test()

    print("test")
    # close(): close pool to inhibit other operation. If all operations keep mount, they will be completed before the process done.
    pool.close()
    # join(): wait for all process exit. This method can be called only after close() or terminate(), which not allow new process get into pool.
    pool.join()

# %%
# 异步进程池（非阻塞）
from multiprocessing import Pool


def test(i):
    print(i)


if __name__ == "__main__":
    pool = Pool(8)
    for i in range(100):
        """
            实际测试发现，for 循环内部执行步骤：
            （1）遍历100个可迭代对象，往进程池放一个子进程
            （2）执行这个子进程，等子进程执行完毕，再往进程池放一个子进程，再执行。（同时只执行一个子进程）
            for循环执行完毕，再执行print函数
        """
        pool.apply(
            test, args=(i,)
        )  # 维持执行的进程总数为8,当一个进程执行完后启动一个新进程。运行效果是先运行了test()之后，再运行print('test')。apply()是阻塞的，很少使用。

    print("test")
    pool.close()
    pool.join()

#%%
# Queue (用于进程通信，资源共享)
# 在使用多进程的过程中，最好不要使用共享资源。普通的全局变量是不能被子进程所共享的，只有通过Multiprocessing组件沟再的数据结构可以被共享。
# Queue是用来创建进程间资源共享的队列的类，使用Queue可以达到多进程间数据传递的功能（缺点：只适用Process类，不能在Pool进程池中使用）。

from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print(f"Process to write: {os.getpid()}")

    for value in ["A", "B", "C"]:
        print(f"Put {value} to queue...")
        # put()：用以插入数据到队列
        q.put(value)
        time.sleep(random.random())


def read(q):
    print(f"Process to read: {os.getpid()}")
    while True:
        # get(): 可以从队列读取并删除一个元素。
        value = q.get(True)
        print(f"Get {value} from queue.")


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()  # 等pw结束
    pr.terminate()  # pr进程里是死循环，无法等待其结束，只能强行终止。

#%%
# JoinableQueue
# JoinableQueue就像是一个Queue对象，但队列允许项目的使用者通知生成者项目已经被成功处理。通知进程是使用共享的信号和条件变量来实现的。

from multiprocessing import Process, JoinableQueue
import time, random


def consumer(q):
    while True:
        # get():如果由于队列为空没有取到任何元素，则在此等待
        res = q.get()
        print(f"消费者拿到了{res}")
        # task_done(): JoinableQueue特有的方法，使用者使用此方法发出信号，表示q.get()的返回项目已经被处理。如果调用此方法的次数大于从队列中删除项目的数量，将引发ValueError异常。
        q.task_done()


def producer(seq, q):
    for item in seq:
        time.sleep(random.randrange(1, 2))
        q.put(item)
        print(f"生产者做好了{item}")

    q.join()


if __name__ == "__main__":
    q = JoinableQueue()
    seq = ("产品%s" % i for i in range(5))
    p = Process(target=consumer, args=(q,))
    p.daemon = (
        True  # 设置为守护进程，在主线程停止时p也停止，但是不用担心，producer内调用q.join保证了consumer已经处理完队列中的所有元素
    )
    p.start()
    producer(seq, q)
    print("主线程")

#%%
# Value, Array(用于进程通信，资源共享)
# multiprocessing中Value和Array的实现原理都是在共享内存中创建ctypes()对象来达到共享数据的目的，两者实现方法大同小异，只是选用不同的ctypes数据类型而已。
# ctypes 是 Python 的外部函数库。它提供了与 C 兼容的数据类型，并允许调用 DLL 或共享库中的函数。可使用该模块以纯 Python 形式对这些库进行封装。

# Array
import multiprocessing


def f(n, a):
    n.value = 3.14
    a[0] = 5


if __name__ == "__main__":
    # Notice: Value 和 Array只适用于Process类
    num = multiprocessing.Value("d", 0.0)
    arr = multiprocessing.Array("i", range(10))
    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])

#%%
# Pipe （用于管道通信）
# 多进程还有一种数据传递方式叫管道原理，和Queue相同。Pipe可以在进程之间创建一条管道，并返回元组（conn1, conn2）
# 其中conn1, conn2表示管道两端的连接对象，强调一点：必须在产生Process对象之前产生管道。
from multiprocessing import Process, Pipe
import time

# 子进程执行方法
def f(Subconn):
    time.sleep(1)
    # send():通过连接发送对象。obj是与序列化兼容的任意对象
    Subconn.send("吃了吗")
    # recv():接收conn2.send(obj)发送的对象。如果没有消息可接收，recv方法会一直阻塞。如果连接的另外一端已经关闭，那么recv方法回抛出EOFError。
    print("来自父亲的问候:", Subconn.recv())
    # close()关闭连接。如果conn1被垃圾回收，将自动调用此方法
    Subconn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()  # 创建管道两端
    p = Process(target=f, args=(child_conn,))  # 创建子进程
    p.start()
    print("来自儿子的问候:", parent_conn.recv())
    parent_conn.send("嗯😋")

#%%
# Manager(用于资源共享)
# Manager()返回的manager对象控制了一个server进程，此进程包含的python对象可以被其他的进程通过proxies来访问。从而达到多进程间数据通信且安全。
# Manager模块常与Pool模块一起使用。
# Manager() 是 BaseManager的子类，返回一个启动的SyncManager()实例，可用于创建共享对象并返回访问这些共享对象的代理。
# 这一部分和管理器服务器有关，暂时用不上，需要了解时看看原公众号文章吧。

#%%
# 同步子进程模块
# Lock(互斥锁)
# Lock锁的作用是当多个进程需要访问共享资源的时候，避免访问的冲突。
# 加锁保证了多个进程修改同一块数据时，同一时间只能有一个修改，即串行的修改，牺牲了速度但保证了数据安全。Lock包含两种状态————锁定和非锁定，以及两个基本的方法。

from multiprocessing import Process, Lock


def l(lock, num):
    # acquire([timeout]):使线程进入同步阻塞状态，尝试获得锁定。
    lock.acquire()
    print(f"Hello Num:{num}")
    # 释放锁。使用前线程必须已获得锁定，否则将抛出异常。
    lock.release()


if __name__ == "__main__":
    lock = Lock()
    for num in range(20):
        Process(target=l, args=(lock, num)).start()

#%%
# RLock(可重入的互斥锁（同一个进程可以多次获得它，同时不会造成阻塞）)
# RLock(可重入锁)是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。
# 拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。可以认为RLock包含一个锁定池和一个初始值为0的计数器，
# 每次成功调用acquire()/release(),计数器将+1/-1,为0时锁处于未锁定状态。
# 用法同Lock

#%%
# Semaphore(信号量)
# 信号量是一个更高级的锁机制。信号量内部有一个计数器而不像锁对象内部有锁标识，而且只有当占用信号量的线程数超过信号量时线程才阻塞。
# 这允许了多个线程可以同时访问相同的代码区。比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去，
# 如果指定信号量为3, 那么来一个人获得一把锁，计数加1,当计数等于3时，后面的人均需要等待。一旦释放，就有人可以获得一把锁。

# 方法同Lock
from multiprocessing import Process, Semaphore
import time, random


def go_wc(sem, user):
    sem.acquire()
    print(f"{user}占到一个茅坑")
    time.sleep(random.randint(0, 3))
    sem.release()
    print(user, "OK")


if __name__ == "__main__":
    sem = Semaphore(2)
    p_l = []
    for i in range(5):
        p = Process(target=go_wc, args=(sem, f"user{i}"))
        p.start()
        p_l.append(p)

    for i in p_l:
        i.join()

#%%
# Condition (条件变量)
# 可以把Condition理解为一把高级的锁，它提供了比Lock, RLock更高级的功能，允许我们能够控制复杂的线程同步问题。Condition在内部维护一个锁对象（默认是Rlock），
# 可以在创建Condition对象的时候把锁对象作为参数传入。Condition也提供了acquire, release方法，其含义与锁的acquire, release方法一致，其实它只是简单的调用内部对象的
# 对应方法而已。Condition还提供了其他方法。
import multiprocessing
import time


def stage_1(cond):
    """perform first stage of work,
    then notify stage_2 to continue
    """
    name = multiprocessing.current_process().name
    print("Starting", name)
    with cond:
        print(f"{name} done and ready for stage 2")
        # notify_all(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
        cond.notify_all()


def stage_2(cond):
    """wait for the condition telling us stage_1 is done"""
    name = multiprocessing.current_process().name
    print("Starting", name)
    with cond:
        # wait([timeout]):调用这个方法将使线程进入Condition的等额带池中等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。
        # 处于wait状态的线程接到通知后会重新判断条件。
        cond.wait()
        print(f"{name} running")


if __name__ == "__main__":

    condition = multiprocessing.Condition()
    s1 = multiprocessing.Process(name="s1", target=stage_1, args=(condition,))
    s2_clients = [
        multiprocessing.Process(
            name=f"stage_2[{i}]", target=stage_2, args=(condition,),
        )
        for i in range(1, 3)
    ]

    for c in s2_clients:
        c.start()
        time.sleep(1)

    s1.start()
    s1.join()

    for c in s2_clients:
        c.join()

#%%
# Event(事件)
# Event内部包含了一个标志位，初始的时候为false。可以使用set()来将其设置为true；或者使用clear()将其从新设置为false；
# 可以使用is_set()来检查标志位的状态；另一个最重要的函数就是wait(timeout=None)，用来阻塞当前线程，直到event的内部标志位被设置为true或者timeout超时。
# 如果内部标志位为true则wait()函数理解返回。

import multiprocessing
import time


def wait_for_event(e):
    """Wait for the event to be set before doing anything"""
    print("wait_for_event: starting")
    e.wait()
    print("wait_for_event: e.is_set()->", e.is_set())


def wait_for_event_timeout(e, t):
    """Wait t seconds and then timeout"""
    print("wait_for_event_timeout: e.is_set()->", e.is_set())
    e.wait(t)
    print('wait_for_event_timeout: e.is_set()->', e.is_set())


if __name__ == "__main__":
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name="block", target=wait_for_event, args=(e,),)

    w1.start()
    w2 = multiprocessing.Process(
        name="nonblock", target=wait_for_event_timeout, args=(e, 2),
    )

    w2.start()
    print('main: waiting before calling Event.set()')

    time.sleep(3)

    e.set()
    print('main: event is set')

#%%
# multiprocessing.dummy 与 multiprocessing区别：dummy模块是多线程，而multiprocessing是多进程,api都是通用的。
# multiprocessing.dummy 通常在IO场景可以尝试使用,比如使用如下方式引入线程池
from multiprocessing.dummy import Pool as ThreadPool

#%%
