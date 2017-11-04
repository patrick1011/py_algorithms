from collections import defaultdict

graph = defaultdict(set)
graph['A'].add('B') # Put append here AGH
graph['A'].add('C')
graph['B'].add('C')
graph['B'].add('D')
graph['C'].add('A')


# Find all paths between two nodes
connecting_paths = []


def fap(graph, curr, end, path=[]):
    path.append(curr)
    if curr == end:
        connecting_paths.append(path[:])
    for node in (n for n in graph[curr] if n not in path):
        fap(graph, node, end, path)
    del path[-1]

fap(graph, 'A', 'C')
print(connecting_paths)
