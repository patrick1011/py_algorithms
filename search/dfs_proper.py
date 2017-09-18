from data_structures.linked_list import SinglyLinkedList


def dfs(adj, s):
    level = {s.key: 0}
    parent = {s.key: None}
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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


if __name__ == "__main__":
    adj = [
        SinglyLinkedList(),
        SinglyLinkedList(),
        SinglyLinkedList(),
        SinglyLinkedList(),
        SinglyLinkedList(),
        SinglyLinkedList(),
        SinglyLinkedList(),
        SinglyLinkedList()
    ]
    adj[0].push(adj[1]).push(adj[2])
    adj[1].push(adj[0])
    adj[2].push(adj[0]).push(adj[3])
    adj[3].push(adj[2]).push(adj[4]).push(adj[5])
    adj[4].push(adj[3]).push(adj[5]).push(adj[6])
    adj[5].push(adj[3]).push(adj[5]).push(adj[6])
