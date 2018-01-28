# Give a N*N square matrix, return an array of its anti-diagonals. Look at the example for more details.

# Example:

		
# Input: 	

# 1 2 3
# 4 5 6
# 7 8 9

# Return the following :

# [ 
#   [1],
#   [2, 4],
#   [3, 5, 7],
#   [6, 8],
#   [9]
# ]


# Input : 
# 1 2
# 3 4

# Return the following  : 

# [
#   [1],
#   [2, 3],
#   [4]
# ]

# s = 1, 2, 3, 4
# n = 1, 3, 5, 7....

def anti_diagonals(arr):
	out = [[] for _ in range(len(arr)*2 - 1)]
	for i in range(len(arr)):
		for j in range(len(arr)):
			out[i + j].append(arr[i][j])
	return out



a = []

print(anti_diagonals(a))

