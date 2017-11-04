# http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

from collections import defaultdict

graph = defaultdict(set)
graph['A'].add('B') # Put append here AGH
graph['A'].add('C')
graph['B'].add('C')
graph['B'].add('D')
graph['C'].add('A')


# Imperative Connected Components
def dfs_imperative(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex])
    return visited


def dfs_recursive(graph, curr, visited=set()):
    if curr not in visited:
        visited.add(curr)
        for _next in graph[curr]:
            dfs_recursive(graph, _next, visited)
    return visited


#  DO THIS WITH BFS IT'D USE LESS SPACE
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    paths = []
    while stack:
        (vertex, path) = stack.pop()
        for _next in graph[vertex] - set(path):
            if _next == goal:
                paths.append(path + [_next])
            else:
                stack.append((_next, path + [_next]))
    return paths


def dfs_recursive(graph, curr, visited=set()):
    if curr not in visited:
        visited.add(curr)
        for n in graph[curr]:
            dfs_recursive(graph, n, visited)
    return visited



dfs_recursive(graph, 'A')
