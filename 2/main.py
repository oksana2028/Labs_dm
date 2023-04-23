from collections import defaultdict

class Graph():
    def __init__(self):
        def __init__(self):
            self.edges = defaultdict(list)
            self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

class ShortestWay:
    def dijkstra(graph, initial, end):
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()

        while current_node != end:
            visited.add(current_node)
            destinations = graph.edges[current_node]
            weight_to_current_node = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = graph.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)

            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            if not next_destinations:
                return "Route Not Possible"
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

        path = []
        way_weight = 0
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            way_weight += shortest_paths[current_node][1]
            current_node = next_node

        path = path[::-1]
        return [way_weight, path]

nodes = ["0", "1", "2", "3", "4", "5", "6", "7"]
graph = []
odds = []
odd_lines = []
cycles = []
lines = []
straight_odd = []

def is_odd(array):
    for i in range(len(array)):
        # transform string array into integer array
        # and check the number of links for each node
        array[i] = [int(x) for x in array[i] if x != "\n" and x != ' ']
        count = sum(map(lambda x: x > 0, array[i]))
        if count % 2 == 1:
            odds.append([nodes[i], i])
    return odds

def generate_multinode_way(first_node, edges, odd_graph):
    ways_to_node = []
    gr = ShortestWay.Graph()
    for edge in edges:
        gr.add_edge(*edge)
    for i in odd_graph:
        if i[0] != first_node:
            ways_to_node.append(ShortestWay.dijsktra(gr, first_node, i[0]))
    weights_of_ways = Extract(ways_to_node)
    shortest = min(weights_of_ways)
    short_way_index = weights_of_ways.index(shortest)
    ways_to_node[short_way_index].pop(0)
    ways_to_node = ways_to_node[short_way_index][0]
    additional_ways = []
    for i in range(1, int(len(ways_to_node))):
        additional_ways.append([ways_to_node[i - 1], ways_to_node[i]])
    return additional_ways

def duplicate_ways(odd_lines):
    possible_ways_num = int(len(odd_lines) / 4)
    possible_ways = []
    if possible_ways_num == 1:
        possible_ways_num = 4
    for i in range(possible_ways_num):
        # it represents each short way from one odd node to another
        line = []
        line.append(odd_lines[i])
        if int(len(odd_lines) / 2) > 2:
            nodes_num = int(len(odd_lines) / 2)
        else:
            nodes_num = int(len(odd_lines) - 1)
        for j in range(nodes_num):
            if odd_lines[j][1] not in line[0] and odd_lines[j][2] not in line[0]:
                line.append(odd_lines[j])
        if len(line) > 1:
            line_weight = line[0][0] + line[1][0]
        elif len(line) == 1:
            line_weight = line[0][0]
        else:
            print("Could not found the weight of a line")
            exit(1)
        possible_ways.append(line)
        possible_ways.append(line_weight)
    the_lightest = min(possible_ways[1::2])
    found_index = possible_ways.index(the_lightest) - 1
    for i in range(int(len(possible_ways[found_index]))):
        possible_ways[found_index][i].pop(0)
    return possible_ways[found_index]

def create_cycles(lines):
    while lines:
        cycle = []
        cycle.append(lines[0])
        first_el = lines[0][0]
        last_el = lines[0][1]
        lines.pop(0)
        while first_el != last_el:
            for line in lines:
                if last_el in line:
                    cycle.append(line)
                    lines.remove(line)
                    if last_el == line[0]:
                        last_el = line[1]
                    else:
                        last_el = line[0]
        cycles.append(cycle)
    return cycles

def collapse_cycles(cycles):
    while len(cycles) > 1:
        for i in range(int(len(cycles[0]))):
            if cycles[1][0][0] in cycles[0][i]:
                place = cycles[0].index(cycles[0][i]) + 1
                break
            elif cycles[1][0][1] in cycles[0][i]:
                place = cycles[0][i].index(cycles[1][0][1]) + 1
                break
        if place == 1:
            place = 0
        for i in cycles[0]:
            if cycles[0].index(i) == place:
                cycles[1].append(i)
                cycles[0].remove(i)
        for x in cycles[1]:
            cycles[0].append(x)
        cycles.pop(1)
    return cycles[0]

def Extract(lst):
    return [item[0] for item in lst]


file = open("lab2.txt")
for line in file:
    graph.append(line.split())
file.close()
graph.pop(0)
odd_graph = is_odd(graph)
# create an array with all links
edges = []
for i in range(len(graph)):
    for j in range(len(graph)):
        line = []
        line.append(nodes[i])
        if graph[i][j] != 0 and [nodes[j], nodes[i]] not in lines:
            line.append(nodes[j])
            lines.append(line)
            edge = (nodes[i], nodes[j], graph[i][j])
            edges.append(edge)
# add additional lines to array if it is odd
if odd_graph:
    for i in range(len(odd_graph)):
        for j in range(len(odd_graph)):
            if graph[odd_graph[i][1]][odd_graph[j][1]] != 0:
                odd_lines.append([graph[odd_graph[i][1]][odd_graph[j][1]], odd_graph[i][0], odd_graph[j][0]])
                straight_odd.append(odd_graph[i][0])
                straight_odd.append(odd_graph[j][0])
# check if  there is an odd node that needs more than one line to reach another odd node
    for t in odd_graph:
        if t[0] not in straight_odd:
            a = generate_multinode_way(t[0], edges, odd_graph)
            if a:
                for way in a:
                    lines.append(way)
            else:
                print("Could`t generate a way", t[0])
                exit(1)
    for i in duplicate_ways(odd_lines):
        lines.append(i)
# create cycles and unite them into one
cycles = create_cycles(lines)
print(collapse_cycles(cycles))


