# What is abstract syntax tree
[抽象语法树](https://www.cnblogs.com/zhuchengyang/p/7692626.html)  
我们知道人类语言上，无论什么语种，都会有「主语」「动词」「宾语」「标点符号」来描述一个现实世界所发生的事件。  
而在计算机编程语言上，无论什么语种，都会有「类型」「运算符」「流程语句」「函数」「对象」等概念来表达计算机中存在内存中的0和1，以及背后运算与逻辑。  
不同的语言，都会配之不同的语法分析器，而语法分析器是把源代码作为字符串读入、解析，并建立语法树的程序。语法的设计和语法分析器的实现是决定语言外在表现的重要因素。  
>在计算机科学中，抽象语法树（abstract syntax tree 或者缩写为 AST），或者语法树（syntax tree），是源代码的抽象语法结构的树状表现形式，这里特指编程语言的源代码。树上的每个节点都表示源代码中的一种结构。之所以说语法是「抽象」的，是因为这里的语法并不会表示出真实语法中出现的每个细节。
## 一则简单例子
![image](https://user-images.githubusercontent.com/52747634/126323155-f3fba945-04ec-4086-8c69-a8ccfcdf2cc3.png)
![image](https://user-images.githubusercontent.com/52747634/126323264-3bbf2606-eec4-47ff-87c5-9a53c1e7638e.png)
可以看出，对于这三种简单的语言，它们只是在这个语法树上按不同的规则遍历而已。三者的代码看起来差别很大，但实际上所用的树结构是相同的。  
  
通过Python语言自带的库文件**ast**，我们可以查看特定的代码被转换成怎样的语法树。
```python
>>> import ast
>>> ast.dump(ast.parse("(1 + 2) * 3"))
'Module(
    body=[
        Expr(
            value=BinOp(
                left=BinOp(
                    left=Num(n=1), 
                    op=Add(), 
                    right=Num(n=2)
                ), 
                op=Mult(), 
                right=Num(n=3)
            )
        )
    ]
)'
```
`BinOp op = Mult()`表示乘法运算，与*相对应；  
`BinOp op = Add()`表示加法运算，与+相对应；  
`Num n = 1`既为数值1。  
![image](https://user-images.githubusercontent.com/52747634/126323608-97e5c59c-b775-4f2a-9add-517b426f5bb9.png)
## 语法树的用处
如果想做「语法高亮」、「关键字匹配」、「作用域判断」、「语言转换」以及「代码压缩」等等，都是最好把代码解构成语法树之后再去各种操作，当然仅仅解构还不够，还需要提供各种函数去遍历与修改语法树。
