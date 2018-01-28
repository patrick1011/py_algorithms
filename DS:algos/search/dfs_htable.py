parent = {"s": None}


def dfs_visit(adj, par):
    for v in adj[par]:
        if v not in parent:
            parent[v] = par
            dfs_visit(adj, v)


# def dfs(adj, V):
#     parent = {}
#     for s in V:
#         if s not in parent:
#             dfs_visit(adj, s, parent)
#     print(parent, 'a')

if __name__ == '__main__':
    V = ["s", "a", "z", "x", "d", "c", "f", "v"]
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

    dfs_visit(adj, "s")
    print(parent)
