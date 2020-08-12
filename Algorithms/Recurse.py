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
def fact(n):
    if n == 1:
        return n
    else:
        print(fact(n - 1))
        return n * fact(n - 1)


print(fact(5))
