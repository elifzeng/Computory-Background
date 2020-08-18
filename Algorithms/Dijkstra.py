# Dijkstral's 算法实现，求有向权重图最短路径
# 用一个散列表存图

graph = {}
graph["start"] = {}
graph["start"]["a"] = 6  # 储存权重
graph["start"]["b"] = 2
# print(graph['start'].keys())
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["fin"] = 5
graph["fin"] = {}

# 用一个散列表来储存每个节点的开销
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = float("inf")

# 父节点散列图
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# 储存处理过的节点的数组
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def main():
    node = find_lowest_cost_node(costs)
    while node is not None:  # 这个循环在所有节点都被处理后结束
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost  # 如果经当前节点前往邻居更近，就更新该邻居的开销
                parents[n] = node  # 同时将当前节点设置为该邻居的父节点
        processed.append(node)  # 将当前节点标记为处理过
        node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环
    print(costs)

# main()

