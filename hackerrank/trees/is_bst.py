def check_binary_search_tree_(root):
    def check(n, ll, lr):
        if n is None:
            return True
        if lr < n.data < ll:
            return (
                check(n.left, n.data, lr) and 
                check(n.right, ll, n.data)
            )
        return False

    return check(root, float('+inf'), float('-inf'))
