#!/usr/bin/env
"""
ref: https://www.jianshu.com/p/a8cb5375171a
通过traceback追溯哪块代码出了问题
Python的traceback module提供一整套接口用于提取，格式化和打印Python程序的stack traces信息
"""

#%%
import sys
import traceback
#%%
def func1():
    raise NameError('--func1 exception--')

#%%
def main():
    try:
        func1()
    except Exception as e:
        # print('ddd')
        exc_type, exc_value, exc_traceback_obj = sys.exc_info() # sys.exc_info返回一个元组
        print(f'exc_type: {exc_type}')
        print(f'exc_value: {exc_value}')
        print(f'exc_traceback_obj: {exc_traceback_obj}')
        print('----------------1-------------------------')
        traceback.print_tb(exc_traceback_obj)
        print('-----------------2---------------------')
        traceback.print_exception(exc_type, exc_value, exc_traceback_obj, limit=2, file=sys.stdout)
        

#%%
if __name__ == '__main__':
    main()
# %%
