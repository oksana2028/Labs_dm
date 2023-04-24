def get_exponential_neighborhoods(graph):
    neighborhoods = []

    for i in range(len(graph)):
        neighborhood = []
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                neighborhood.append(j)
        neighborhoods.append(neighborhood)

    exponential_neighborhoods = []

    for i in range(len(graph)):
        neighborhood = neighborhoods[i]
        exponential_neighborhood = neighborhood.copy()
        for j in range(len(neighborhood)):
            vertex = neighborhood[j]
            for k in range(len(neighborhood)):
                if k != j:
                    neighbor = neighborhood[k]
                    for l in range(len(neighborhoods[neighbor])):
                        candidate = neighborhoods[neighbor][l]
                        if candidate not in exponential_neighborhood and graph[vertex][candidate] == 1:
                            exponential_neighborhood.append(candidate)
        exponential_neighborhood.sort()
        exponential_neighborhoods.append(exponential_neighborhood)

    return exponential_neighborhoods


def is_isomorphic(graph1, graph2):
    if len(graph1) != len(graph2):
        return False

    en1 = get_exponential_neighborhoods(graph1)
    en2 = get_exponential_neighborhoods(graph2)

    for i in range(len(en1)):
        if en1[i] != en2[i]:
            return False

    return True


if __name__ == '__main__':
    graph1 = [
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]
    ]

    graph2 = [
        [0, 0, 1, 0, 1],
        [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0]
    ]

    if is_isomorphic(graph1, graph2):
        print('Graphs are isomorphic')
    else:
        print('Graphs are not isomorphic')
