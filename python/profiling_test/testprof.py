"""for testing profiling python programme,
you should run 'export PRORILING=y' firstly
"""

import cProfile
import pstats
import os

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

# 递归
def countdown(i):
    print(i)
    if i <= 1:  # base case 基线条件
        return
    else:  # recursice case 递归条件
        countdown(i - 1)


# countdown(5)

# Stack 栈
def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()


def greet2(name):
    print(" how are you, " + name + "?")


def bye():
    print("ok bye!")


# greet("elif")

# 递归调用栈
# calculating n!
@do_cprofile('./prof_test.prof') # 指定分析数据储存路径
def fact(n):
    if n == 1:
        return n
    else:
        # print(fact(n - 1))
        return n * fact(n - 1)


print(fact(5))
