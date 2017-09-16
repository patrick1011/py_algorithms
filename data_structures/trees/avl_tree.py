""" AVL tree
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/recitation-videos/MIT6_006F11_rec06.pdf
"""

from data_structures.trees.binary_search_tree import BinarySearchTree


class AVLTree(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)

    def insert(self, x):
        BinarySearchTree.insert(self, x)
        self.rebalance(x)

    def height(self, x):
        if x is None:
            return -1
        return x.height

    def update_height(self, x):
        x.height = max(self.height(x.left), self.height(x.right)) + 1

    def rebalance(self, x):
        if x is None:
            return
        self.update_height(x)
        if self.height(x) > 3:
            return
        if self.height(x.left) > 1 + self.height(x.right):
            if self.height(x.left.left) >= self.height(x.left.right):
                self.right_rotate(x)
            else:
                self.left_rotate(x.left)
                self.right_rotate(x)
        elif self.height(x.right) > 1 + self.height(x.left):
            if self.height(x.right.right) >= self.height(x.right.left):
                self.left_rotate(x)
            else:
                self.right_rotate(x.right)
                self.left_rotate(x)
        self.rebalance(x.p)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y
        self.update_height(y.left)
        self.update_height(y.right)
        self.update_height(y)

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y
        self.update_height(y.left)
        self.update_height(y.right)
        self.update_height(y)


class AvlNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.p = None
        self.key = key
        self.height = None

    def __repr__(self):
        return str(self.key)
if __name__ == '__main__':
    avl = AVLTree()
    avl.insert(AvlNode(1))
    avl.insert(AvlNode(2))
    avl.insert(AvlNode(3))
    avl.insert(AvlNode(4))
    avl.insert(AvlNode(5))
    avl.insert(AvlNode(6))
    avl.insert(AvlNode(7))
    avl.insert(AvlNode(8))
    avl.insert(AvlNode(9))
    avl.insert(AvlNode(10))
    avl.insert(AvlNode(11))
    n_nodes = avl.nodes_in_subtree(avl.root)
    print('---------')
    print(avl.height_of_tree(avl.root))
    print('---------')
    avl.inorder_traversal(avl.root)
