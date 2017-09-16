""" BINARY TREE
    Definitions:
        1. Full: every node has 0 or 2 children.
        2. Complete: Every level filled except last which is left.
        3. Perfect: All internal nodes have 2 children.
        4. Balanced: Height is O(log(n)).
        5. Degenerate: Each node has one child.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


class BinaryTree:
    def __init__(self):
        self.root = None

    def height_of_tree(self, node):
        if node is None:
            return 0
        lheight = self.height_of_tree(node.left)
        rheight = self.height_of_tree(node.right)
        if lheight > rheight:
            return lheight + 1
        return rheight + 1

    def inorder_traversal(self, x):
        if x is not None:
            self.inorder_traversal(x.left)
            print(x.key)
            self.inorder_traversal(x.right)

    def nodes_in_subtree(self, x):
        if x is None:
            return 0
        l_subtree_nodes = self.nodes_in_subtree(x.left)
        r_subtree_nodes = self.nodes_in_subtree(x.right)
        return l_subtree_nodes + r_subtree_nodes + 1

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(1)
    root.right.right.left = Node(10)
    # print(height_of_tree(root))
