#!/usr/bin/env python
# %%
import time
import threading
from concurrent.futures import ThreadPoolExecutor


def worker(name):
    print(f"{name} start...")
    time.sleep(2)
    print(f"{name} done.")


# %%
# 单线程阻塞
# 阻塞线程的情况下，程序会先等待线程任务执行完，再往下执行其他代码
def single_thread_block():
    t = threading.Thread(target=worker, args=("alice",))
    t.start()
    # 阻塞
    t.join()
    print("Finished")


# %%
# 单线程不阻塞
# 不阻塞线程的情况下，程序会直接往下走，线程任务是后完成的（因为我在线程任务里加了sleep），类似于异步；
# 同时，我们还可以发现，程序（主线程）执行完最后一行代码之后，如果线程任务还没完成，程序不会马上死掉，还是会等线程任务执行完才会结束
# 注：jupyter notebook上的运行结果和直接在终端运行结果可能不同，以终端运行结果为准
def single_thread_no_block():
    t = threading.Thread(target=worker, args=("bob",))
    print("aaa")
    t.start()
    print("Finished")


# %%
# 多线程的错误阻塞
# t1.join直接阻塞了程序，t2还没start，t1.join阻塞程序直到t1的任务已完成。所以会看到alice done之后，bob才能start
def multi_thread_error_block():
    t1 = threading.Thread(target=worker,args=('alice',))
    t1.start()
    t1.join()
    t2 = threading.Thread(target=worker, args=('bob',))
    t2.start()
    t2.join()
    print('Finished')

#%%
# 多线程的正确阻塞
# 需要将所有子线程都start之后，才能阻塞(join)；线程任务也不是按顺序完成了，哪个先完成，得看哪个线程任务耗时少，也有可能回会同时完成（并发）
def multi_thread_block():
    t1 = threading.Thread(target=worker, args=('alice',))
    t2 = threading.Thread(target=worker, args=('bob',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Finished')

# %%
# 多线程不阻塞
# 参考上面单线程不阻塞，不阻塞的情况下，也是会等待全部线程任务执行完成才结束程序的。多线程有一定的并发现象。
def multi_thread_no_block():
    t1 = threading.Thread(target=worker, args=('alice',))
    t2 = threading.Thread(target=worker, args=('bob',))
    t1.start()
    t2.start()
    print('Finished')

# %%
# 守护线程（后台线程）阻塞
# 如果设置一个线程为守护线程，就表示这个线程是不重要的，在进程退出时，不用等待这个线程退出
# 和守护线程不阻塞一起看
def daemon_thread_block():
    t1 = threading.Thread(daemon=True, target=worker, args=('alice',))
    t2 = threading.Thread(daemon=True, target=worker, args=('bob',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Finished')

# %%
# 守护线程不阻塞
# 可以看到和“多线程不阻塞”很不一样，主程序并不会等待子线程完成任务才结束。而是直接就结束了。这是守护线程（后台线程）的一个特点：不阻塞的情况下，后台线程（守护线程）会在主线程结束的时候自动死掉。
def daemon_thread_no_block():
    t1 = threading.Thread(daemon=True, target=worker, args=('alice',))
    t2 = threading.Thread(daemon=True, target=worker, args=('bob',))
    t1.start()
    t2.start()
    print('Finished')

# %%
# 守护线程不阻塞但主线程比较晚结束
# 这里的主线程并没有等子线程，只是主线程耗时比子线程还要久，子线程先执行完毕了
def daemon_thread_no_block_late():
    t1 = threading.Thread(daemon=True, target=worker, args=('alice',))
    t2 = threading.Thread(daemon=True, target=worker, args=('bob',))
    t1.start()
    t2.start()
    time.sleep(5)
    print('Finished')

# %%
# 线程池
# 线程池并没有join方法，但它默认是阻塞的。运行结果基本和“多线程的正确阻塞”一样，只是线程池方便管理
def thread_pool():
    with ThreadPoolExecutor(max_workers=3) as p:
        p.submit(worker, 'alice')
        p.submit(worker, 'bob')
    print('Finished')
# %%
if __name__ == "__main__":
    # single_thread_block()
    # single_thread_no_block()
    # multi_thread_error_block()
    # multi_thread_block()
    # multi_thread_no_block()
    # daemon_thread_block()
    # daemon_thread_block() # finished in 2.04s
    # daemon_thread_no_block() # finished in 0.064s
    # daemon_thread_no_block_late()
    thread_pool()
# %%
