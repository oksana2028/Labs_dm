class Graph:
    def __init__(self, v):
        self.v = v
        self.parent = [i for i in range(v)]
        self.rank = [0 for i in range(v)]
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        while e < self.v - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(u)
            y = self.find(v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(x, y)

        print("Minimum Spanning Tree:")
        for u, v, weight in result:
            print(f"{u} - {v}: {weight}")


# зчитування вхідних даних з файлу
with open('lab1.txt', 'r') as file:
    n = int(file.readline().strip())
    g = Graph(n)
    for i in range(n):
        row = list(map(int, file.readline().strip().split()))
        for j in range(n):
            if row[j] != 0:
                g.add_edge(i, j, row[j])

g.kruskal_mst()
