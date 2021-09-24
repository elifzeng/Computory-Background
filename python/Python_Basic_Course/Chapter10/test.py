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