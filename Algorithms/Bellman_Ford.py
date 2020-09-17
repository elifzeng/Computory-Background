# Bellman Ford Algorithm
# 解决边的权重可以为负值的单源最短路径问题，算法复杂度为 O(VE)


class Graph:
    def __init__(self, V):  # 初始化， 有V个顶点的图graph
        self.V = V
        self.graph = []

    # add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])  # 这三个变量分别为从s节点到d节点这条边的权重w

    # print the solution
    def print_solultion(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print(f"{i}\t\t{dist[i]}")

    def bellman_ford(self, src):
        # step1: fill the distance array and predecessor（父节点） array
        dist = [float("Inf")] * self.V  # 给所有节点路径距离赋值为无穷大
        # Mark the source vertex
        dist[src] = 0  # 选择开始节点，将其路径距离赋值为0

        # step2: relax edges |V|-1 times 松弛操作
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    # ！= float("Inf")确保了正在检查的节点顺序
                    dist[d] = dist[s] + w

        # step3: detect negative cycle
        for s, d, w in self.graph:
            # 已经遍历完所有节点后，如果路径距离还能再变小，说明有权重为负值的环路，该算法就不适用了
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found, print the distance
        self.print_solultion(dist)


if __name__ == "__main__":
    g = Graph(5)
    for s, d, w in [
        (0, 1, 4),
        (0, 2, 2),
        (1, 2, 3),
        (2, 1, 1),
        (1, 3, 2),
        (1, 4, 3),
        (2, 4, 5),
        (2, 3, 4),
        (4, 3, -5),
    ]:
        g.add_edge(s, d, w)  # add edge
    g.bellman_ford(0)  # set vertex 0 as the source vertex
