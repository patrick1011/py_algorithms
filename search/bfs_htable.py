def bfs(adj, s):
    level = {s: 0}
    parent = {s: None}
    frontier = [s]
    while frontier:
        _next = []
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = level[u] + 1
                    parent[v] = u
                    _next.append(v)
            frontier = _next
    return level

if __name__ == '__main__':
    adj = {
        "s": ["a", "x"],
        "a": ["z", "s"],
        "z": ["a"],
        "x": ["s", "d", "c"],
        "d": ["x", "c", "f"],
        "c": ["x", "d", "f", "v"],
        "f": ["d", "c", "v"],
        "v": ["c", "f"]
    }

    print(bfs(adj, "s"))
