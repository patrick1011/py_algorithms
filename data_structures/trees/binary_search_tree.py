""" BINARY SEARCH TREE (BST)
    Def:
        Let x be a node in a BST. If y is a node in the left
        subtree of x then y.key <= x.key.  If it's in the right
        subtree then y.key >= x.key.
"""
from data_structures.trees.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):
    def __init__(self):
        BinaryTree.__init__(self)

    def insert(self, x):
        if self.root is None:
            self.root = x
            return
        z = self.root
        while z is not None:
            y = z
            if x.key <= z.key:
                z = z.left
            else:
                z = z.right
        x.p = y
        if x.key <= y.key:
            y.left = x
        else:
            y.right = x

    def search(self, x, key):
        if (x is None) or (x.key is key):
            return x
        if key <= x.key:
            return self.search(x.left, key)
        return self.search(x.right, key)

    def delete(self, x):
        if x.left is None:
            self.transplant_node(x, x.right)
        elif x.right is None:
            self.transplant_node(x, x.left)
        else:
            y = self.node_successor(x)
            if y.p is not x:
                self.transplant_node(y, y.right)
                y.right = x.right
                y.right.p = y
            y.left = x.left
            y.left.p = y

    def node_successor(self, x):
        if x.right is not None:
            return self.minimum(x.right)
        y = x.p
        while y is not None and y.right is x:
            x = y
            y = y.p
        return y

    def node_predesessor(self, x):
        if x.left is not None:
            return self.maximum(x.left)
        y = x.p
        while y is not None and y.left is x:
            x = y
            y = y.p
        return y

    def minimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def maximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def transplant_node(self, t, x):
        if t.p is None:
            self.root = x
        elif t is t.p.left:
            t.p.left = x
        else:
            t.p.right = x
        if x is not None:
            x.p = t.p


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.p = None
        self.key = key

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(Node(21))
    bst.insert(Node(30))
    bst.insert(Node(22))
    bst.insert(Node(17))
    bst.insert(Node(33))
    bst.insert(Node(14))
    bst.insert(Node(30))
    bst.insert(Node(20))
    bst.insert(Node(18))
    bst.insert(Node(35))
    bst.insert(Node(45))
    n_nodes = bst.nodes_in_subtree(bst.root)
    print(bst.inorder_traversal(bst.root))
    # a = bst.root.left.right
    # print(a.key)
    # print('--------')
    # bst.inorder_traversal(bst.root)
    # bst.delete(a)
    # print('--------')
    # bst.inorder_traversal(bst.root)
