class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def find_path(self, source, sink, parent):
        visited = [False] * self.vertices
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)
            for i in range(len(self.graph)):
                if visited[self.graph[i][1]] == False and self.graph[i][2] > 0 and self.graph[i][0] == u:
                    queue.append(self.graph[i][1])
                    visited[self.graph[i][1]] = True
                    parent[self.graph[i][1]] = i

        return True if visited[sink] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.vertices
        max_flow = 0

        while self.find_path(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][2])
                s = self.graph[parent[s]][0]

            max_flow += path_flow
            v = sink
            while v != source:
                u = self.graph[parent[v]][0]
                self.graph[parent[v]][2] -= path_flow
                for i in range(len(self.graph)):
                    if self.graph[i][0] == self.graph[parent[v]][1] and self.graph[i][1] == u:
                        self.graph[i][2] += path_flow
                        break
                v = u

        return max_flow


def read_graph_file(filename):
    with open(filename) as file:
        lines = file.readlines()
        n = int(lines[0])
        g = Graph(n)
        for i in range(n):
            line = lines[i+1].split()
            for j in range(n):
                g.add_edge(i, j, int(line[j]))
        return g


if __name__ == '__main__':
    g = read_graph_file('lab4.txt')
    source = 0
    sink = g.vertices - 1
    max_flow = g.ford_fulkerson(source, sink)
    print("Max Flow: {}".format(max_flow))
