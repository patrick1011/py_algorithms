# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# You need to do this in place.

# Note that if you end up using an additional array, you will only receive partial score.

# Example:

# If the array is

# [
#     [1, 2, 3],
#     [4, 5, 6],
#	  [7, 8, 9]
# ]
# Then the rotated array becomes:

# [
#     [7, 4, 1],
#     [8, 5, 2],
#	  [9, 6, 3]
# ]


# a rotation implies element 
#	(i, j) -> (j, n - i - 1)
#	(0, 0) -> (0, 1)
#	(0, 1) -> (1, 1)
#	(1, 0) -> (0, 0)
#	(1, 1) -> (1, 0)							

# can we apply (i, j) -> formula to upper triangle? no...
# for each border:
# 	do 4 'corners' first
#		1. flip top left and top right
#		2. flip top left and bottom left				<-- try to combine these
#		3. flip bottom left and bottom right
# 	then do other non-corner border nodes. 
#		1. flip top and left.
#		2. flip left and right.
#		3. flip left and bottom.
#		This works if we init top to (0, 0), right to (0, n) etc

def ans(a):
	n = len(a)
	def flip_outer_ring(a, o):
		for k in range(o, n-1-o):
			# top = 0, k
			# left = n - k - 1, 0
			# right = k, n - 1
			# bottom = n - 1, n - k -1
			a[o][k], a[n-k-1][o] = a[n-k-1][o], a[o][k]
			a[n-k-1][o], a[k][n-1-o] = a[k][n-1-o], a[n-k-1][o]
			a[n-k-1][o], a[n-1-o][n-k-1] = a[n-1-o][n-k-1], a[n-k-1][o]

	for o in range(n // 2):
		flip_outer_ring(a, o)

# n = 0, 0
# n = 1, 0
# n = 2, 1
# n = 3, 1
# n = 4, 2
# n = 5, 2
# n = 6, 3

a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]
]

# a = [[1,2,3],[4,5,6],[7,8,9]]

ans(a)

print(a)


