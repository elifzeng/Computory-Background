[a simple explainment about class](https://www.zhihu.com/question/46973549/answer/293788116)

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

class关键字后面跟类的名称就定义了一个类，类的名称可以任意，采用驼峰命名法，也即每个单词的首字母大写，如Book、Person、WildAnimal等.

这里的`__init__`方法(initialization)是一个特殊的方法，在使用类创建对象之后被执行，用于给新创建的对象初始化属性用。
初始化属性的语句就是`self.name = name`这种了，这一句不太好理解，我们把它改编一下就好理解了：

```python
def __init__(self, n, a):
    self.name = n
    self.age = a
```

首先这是一个方法，方法的形参有self，n和a三个。
这个self，表示对象本身，谁调用，就表示谁（这句话不好理解，先记住，我们后面分析）。
语法上，类中的方法的第一个参数都是self，这是和普通方法区别的地方。
这里self.name = n和self.age = a表示将外部传来的n和a，赋值给了self对象的name和age属性。
这里的n和a，其实叫什么都可以，但是会有个问题：一般我们调用方法的时候，想自动提示一下或者查看文档看一下这个方法的参数要求，
如果形参名都是n、a、m、i这些，会让人摸不着头脑，不知道到底该传入什么样的实参。因为这里我们传入实参是为了给属性赋值，为了能见名知意，
将形参的名字定义的跟属性一致，调用者就知道该怎么传参了。
所以才有了上面的写法。

再来说创建对象：

p = Person('小明', 20)
这句话就创建出来了一个具体的人，并且给这个人起了个名字叫小明，指定了小明的年龄为20，并且将小明这个对象赋值给了变量p，此时p就表示
小明这个人（对象）

这就造出了一个人。

既然你是神，当然想造出什么样的人都可以，比如造出一个200岁的叫杰拉考的人：

p = Person('杰拉考', 200)
这句话后面的Person('杰拉考', 200)用于创建出了一个对象（人），并且调用了init(self,name,age)方法完成了该人的属性的初始化，
杰拉考赋值给了name，200赋值给了age属性。
那self呢？self不需要传参，上面我们说过，self，表示对象本身，谁调用，就表示谁，此时的self就表示你Person('杰拉考', 200)创造出来的那个对象，
也即是p。
也即，我们创造出了p，然后给p的属性赋了值，此时p就表示拥有属性值之后的那个人。

可以使用点.来调用对象的属性，比如输出p的名字和年龄，完整代码为：

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p = Person('杰拉考', 200)
print(p.name)
print(p.age)
输出结果：

杰拉考
200
接下来我们再在Person类中定义一个方法，用于自我介绍：

def desc(self):
    print("我叫%s，今年%d岁" % (self.name, self.age))
在类的内部，访问自己的属性和方法，都需要通过self，self就是外部对象在类内部的表示，此时可以使用p调用该方法，完整代码如下：

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def desc(self):
        print("我叫%s，今年%d岁" % (self.name, self.age))
p = Person('杰拉考', 200)
# 调用自我介绍方法 desc方法中的self就是外部的这个p
p.desc()
输出为：

我叫杰拉考，今年200岁
当前desc方法中的self，就是外部的那个对象p，如果我再定义了一个对象p2，那么p2调用desc时，desc中的self就表示p2这个对象。
正所谓：谁调用，就表示谁