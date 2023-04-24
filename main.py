import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        for i in range(vertices):
            self.graph.append([0] * vertices)

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight

    def solve_tsp(self, start_vertex):
        heap = []
        heapq.heappush(heap, (0, [start_vertex], set([start_vertex])))
        best_cost = float('inf')
        best_path = []

        while heap:
            (cost, path, visited) = heapq.heappop(heap)

            if len(visited) == self.vertices and self.graph[path[-1]][start_vertex] != 0:
                path.append(start_vertex)
                cost += self.graph[path[-2]][start_vertex]
                if cost < best_cost:
                    best_cost = cost
                    best_path = path

            for i in range(self.vertices):
                if i not in visited and self.graph[path[-1]][i] != 0:
                    new_cost = cost + self.graph[path[-1]][i]

                    if new_cost < best_cost:
                        new_path = path.copy()
                        new_path.append(i)
                        new_visited = visited.copy()
                        new_visited.add(i)
                        heapq.heappush(heap, (new_cost, new_path, new_visited))

        return best_path, best_cost


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
    g = read_graph_file('lab3.txt')
    path, cost = g.solve_tsp(0)
    print('Path:', path)
    print('Cost:', cost)
