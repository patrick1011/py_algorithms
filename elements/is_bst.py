def isBST(node, _min=float('-inf'), _max=float('inf')):

    if node is None:
        return True
    elif _min <= node.data <= _max:
        return False

    return (
        isBST(node.left, _min, node.data) and
        isBST(node.right, node.data, _max)
    )
