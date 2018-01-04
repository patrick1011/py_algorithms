# Definition for a  binary tree node


# Path may start at leaf or internal node...

#  Standard question involves computing longest path from root to leaves...

# Edge cases - empty tree, 1 node tree.

# At any given node -> compute longest path to a leaf on left and right.
#   1. maximum sum left path. -> 2
#   2. maximum sum right path. -> 3
#   3. Decide max sum path here is either...
#       - sum left + sum right + current node
#       - current node val + max(sum left, 0)
#       - current node val + max(sum right, 0)
#       candidate solution, compare to current max sub path



# Go through tree 


#   Solution path can either:
#       be in the left subtree
#       be in the right subtree
#       or can go through the node

#	We should try all possible cominations.
#	Visit each child node with 1 variable -> 'Max to get here'.
#	If we know maxsumpath ending @ parent node then maxsumpath @ child is:
#		maxsumpaath @ parent + child
#	!!! but then maxsumpath @ parent could actually be going through a child.

#	Max sum path ending at node can either come from parent, left child or right child.
#	For leaves max sum path can only come from parent.

#
# This is a classical DP on tree problem.
# Can you try to compute the answer for any vertex if you have answer for their left and right child?

#               1
#            /    \
#           2      3
#         /  \    /  \
#   	 9    7  2   -4  

# 9 -100 -200 -1 -300 -400 -1 -1 -1 -1

#            -100
#            /    
#          -200   
#             \      
#   	      -300
#			  /  
#			-400

class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


# t = Node(-100)
# l = Node(-200)
# lr = Node(-300)
# lrl = Node(-400)

# t.left = l
# l.right = lr
# lr.left = lrl


t = Node(1)
l = Node(2)
ll = Node(9)
lr = Node(7)
r = Node(3)
rl = Node(2)
rr = Node(-4)

t.left = l
t.right = r
l.left = ll
l.right = lr
r.left = rl
r.right = rr 

def maxPathSum(n):

	max_paths = {}

	def recursive_child_paths(n):
		mlp = n.val + (recursive_child_paths(n.left) if n.left else 0)
		mrp = n.val + (recursive_child_paths(n.right) if n.right else 0)

		max_paths[n] = [mlp, mrp, None]

		return max(0, mlp, mrp)

	def recursive_parent_paths(n, parent_val):
		max_paths[n][2] = n.val + parent_val

		if n.left:
			recursive_parent_paths(n.left, max(max_paths[n][2], max_paths[n][1]))
		if n.right:
			recursive_parent_paths(n.right, max(max_paths[n][2], max_paths[n][0]))


	recursive_child_paths(n)
	recursive_parent_paths(n, 0)

	_max_arr = max([max(max_paths[c]) for c in max_paths])

	return _max_arr


print(maxPathSum(t))












