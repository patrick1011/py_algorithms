from collections import deque, defaultdict

graph = defaultdict(set)
graph['A'].add('B')
graph['A'].add('C')
graph['B'].add('D')
graph['B'].add('C')
graph['C'].add('A')


def bfs(graph, start):
    visited, queue = set(), deque(start)
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, target):
    queue, valid_paths = deque([(start, [start])]), []
    while queue:
        (vertex, path) = queue.popleft()
        for _next in graph[vertex] - set(path):
            if _next == target:
                print(path + [_next])
                valid_paths.append(path + [_next])
            else:
                queue.append((_next, path + [_next]))
    return valid_paths

print(bfs_paths(graph, 'A', 'C'))
