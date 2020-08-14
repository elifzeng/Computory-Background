from collections import (
    deque,
)  # collections是python内建的一个集合模块，实现了特定目标的容器，以提供Python标准内建容器 dict , list , set , 和 tuple 的替代选择。

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
# 使用函数deque创建一个双端队列

# print(graph)


def person_is_seller(name):
    return name[-1] == "m"


def search(name):
    search_queue = deque()  # 创建一个队列
    search_queue += graph[name]  # 将“邻居”加入到这个搜索队列中
    searched = []  # 这个数组用于记录检查过的人
    while search_queue:  # 只要队列不为空
        # print('the search queue' , search_queue)
        person = search_queue.popleft()  # popleft头部删除，返回其中的第一个人
        # print('person', person)
        if person not in searched:
            if person_is_seller(person):
                # print(person + " is a mango seller !")
                return True
            else:
                search_queue += graph[person]  # 不是芒果销售商，就将此人的朋友都加入搜索队列
                searched.append(person)  # 将此人标记为检查过
                # print('searched' ,searched)
    return False


search("you")

