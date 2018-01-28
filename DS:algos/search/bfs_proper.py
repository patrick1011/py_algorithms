from data_structures.linked_list import SinglyLinkedList


def dfs(adj, s):
    level = {s: 0}
    parent = {s: None}
    frontier = [s]
    while frontier:
        print('a')
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

    adj[0].push(Node(adj[1]))
    adj[0].push(Node(adj[2]))

    adj[1].push(Node(adj[0]))

    adj[2].push(Node(adj[0]))
    adj[2].push(Node(adj[3]))

    adj[3].push(Node(adj[2]))
    adj[3].push(Node(adj[4]))
    adj[3].push(Node(adj[5]))

    adj[4].push(Node(adj[3]))
    adj[4].push(Node(adj[5]))
    adj[4].push(Node(adj[6]))

    adj[5].push(Node(adj[3]))
    adj[5].push(Node(adj[4]))
    adj[5].push(Node(adj[7]))

    adj[6].push(Node(adj[4]))
    adj[6].push(Node(adj[5]))
    adj[6].push(Node(adj[7]))

    adj[7].push(Node(adj[5]))
    adj[7].push(Node(adj[6]))

    dfs(adj, adj[2])
