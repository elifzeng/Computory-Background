[specific explanation](https://liam.page/2017/06/30/understanding-yield-in-python/)  
### iterator 迭代器
`iteration`迭代，即逐个获取对象的过程。
`iterator`是一个对象。迭代器抽象的是一个「数据流」，是只允许迭代一次的对象。对迭代器不断调用 next() 方法，则可以依次获取下一个元素；当迭代器中没有元素时，调用 next() 方法会抛出 StopIteration 异常。  
```python
for x in something:
  print(x)
```

Python 处理 for 循环时，首先会调用内建函数 iter(something)，它实际上会调用 something.__iter__()，返回 something 对应的迭代器。而后，for 循环会调用内建函数 next()，作用在迭代器上，获取迭代器的下一个元素，并赋值给 x。此后，Python 才开始执行循环体。  

### generator 生成器  
生成器是一种特殊的迭代器。如果一个函数包含 yield 表达式，那么它是一个生成器函数；调用它会返回一个特殊的迭代器，称为生成器。
```python
def func():
    return 1

def gen():
    yield 1

print(type(func))   # <class 'function'>
print(type(gen))    # <class 'function'>

print(type(func())) # <class 'int'>
print(type(gen()))  # <class 'generator'>
```
如果一个函数定义中包含 yield 表达式，那么该函数是一个生成器函数（而非普通函数）。实际上，yield 仅能用于定义生成器函数。  

yield 和 return 有很大差别，当函数运行到 return 所在代码行后就会终止，而当函数运行到 yield 所在代码行后会先‘冻结’，将生成的值返回给调用它的`for loop`，随后再接着yield所在行的**下一行**继续执行：  
```python
def yield_test(n):  
    for i in range(n):  
        # return call(i)
        yield call(i) 
        print("i=",i)  
    #做一些其它的事情      
    print("do something.")      
    print("end.")  
  
def call(i):  
    return i*2  
  
#使用for循环  
for j in yield_test(5):  
    print(j,",")  
```
结果：
```bash
0 ,
i= 0
2 ,
i= 1
4 ,
i= 2
6 ,
i= 3
8 ,
i= 4
do something.
end.
```
```python
def yield_test(n):  
    for i in range(n):  
        return call(i)
        # yield call(i) 
        print("i=",i)  
    #做一些其它的事情      
    print("do something.")      
    print("end.")  
  
def call(i):  
    return i*2  
  
#使用for循环  
# for j in yield_test(5):  
#     print(j,",")  
print(yield_test(5))
```
运行到`return call(i)` 后终止，返回call(0)，此时yield_test(5)为一`int`，值为0。结果：  
```
0
```
#### yield 的好处
在很多时候，我们只是需要逐个顺序访问容器内的元素。大多数时候，我们不需要「一口气获取容器内所有的元素」。比方说，顺序访问容器内的前 5 个元素，可以有两种做法：

获取容器内的所有元素，然后取出前 5 个；  
从头开始，逐个迭代容器内的元素，迭代 5 个元素之后停止。  

显而易见，如果容器内的元素数量非常多（比如有 10 ** 8 个），或者容器内的元素体积非常大，那么后一种方案能节省巨大的时间、空间开销。
