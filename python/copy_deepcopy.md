# Python拷贝(深拷贝deepcopy与浅拷贝copy)
Python中的对象之间赋值时是按引用传递的，如果需要拷贝对象，需要使用标准库中的copy模块。

1. copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。

2. copy.deepcopy 深拷贝 拷贝对象及其子对象  


![image](https://user-images.githubusercontent.com/52747634/71762571-b7062380-2f0b-11ea-9fe1-317a81f674b0.png)

3. 直接copy与 copy.copy, copy.deepcopy的区别（此处涉及python动态对象和引用的知识，具体可查阅书籍）：
```python
>>>a = [1,2,3]
>>>b = a
>>>b
[1,2,3]
>>>b[2] = 0
>>>b
[1,2,0]
>>>a
[1,2,0] # change with b
>>>c = copy.copy(a)
>>>c
[1,2,0]
>>>c[1] = 8
>>>c
[1,8,0]
>>>a
[1,2,0]# not change with c
>>>d = copy.deepcopy(a)
>>>a[1] = 9
>>>a
[1,9,0]
>>>d
[1,2,0]# not change with a
```
