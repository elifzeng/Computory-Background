#!/usr/bin/env python
#%%
from _typeshed import Self


class A:
    def hello(self):
        print("Hello, I'm A")

class B(A): # A是B的超类，B是A的子类。B可以从A中继承属性与方法
    pass
# b = B()
# %%
class C(A):
    def hello(self): # 重写从超类A继承的方法，定制子类C的行为
        print("Hello, I'm C ")
# %%
class Bird:
    def __init__(self) -> None:
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah...')
            self.hungry = False
        else:
            print('No, thanks!')
#%%
class SongBird(Bird):
    def __init__(self) -> None:
        super().__init__() # equal to super(SongBird, self)
        self.sound = 'Squawk!'
    def sing(self):
        print(self.sound)
# b = SongBird()
# b.sing()
# b.eat()
# %%
import hello
# %%
# import a module twice
import importlib
halo = importlib.reload(hello)
# hello
# %%
import hello2
# hello2.hello()
# %%
import hello3
# hello3.hello()
# __name__
# hello3.__name__
#%%
import hello4
# hello4.hello()
# %%
import sys, pprint # pretty print 美化打印
pprint.pprint(sys.path)
# %%
# cp hello4.py /home/elifzeng/.local/lib/python3.7/site-packages/another_hello.py
import another_hello
# another_hello.hello()
# %%
# explore module
import copy
# dir(copy)
# [n for n in dir(copy) if not n.startswith('_')]
# %%