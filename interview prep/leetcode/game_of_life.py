# According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

# Any live cell with fewer than two live neighbors dies, as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Write a function to compute the next state (after one update) of the board given its current state.

# Follow up: 
# Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

# Rules:
#	< 2 neighbours die.
#	2/3 neighbours lives on
#	> 3 neighbours dies

#	dead with 3 neighbouts becomes alive

#	0,	0,	0,	0
#	0,	0,	1,	0
#	0,	0,	0,	0
#	1,	1,	0,	0
# --->
#	0,	0,	0,	0
#	0,	0,	0,	0
#	0,	0,	0,	0
#	1,	1,	0,	0

#  Algorithm:
#	For each cell look at 8 'connected' cells.
#	Decive on fate based on that -> O(8nm) = O(nm)

# Encoding:
#	00: nothing
#	01: 1 on the last
#	10: 0 on the last and 1 on the next
#	11: 1 on last and 1 on the next

import copy

def main(arr):
	def _compute_count(i, j, n, m, arr):
		loc, count = (-1, 0, 1), 0
		for di in loc:
			for dj in loc:
				if (di != 0 or dj != 0) and (0 <= i + di < m) and (0 <= j + dj < n):
					count += (arr[i + di][j + dj] & 1)
		return count

	m = len(arr)
	n = len(arr[0])
	for i in range(m):
		for j in range(n):
			count = _compute_count(i, j, n, m, arr)
			print(count, "({}, {})".format(i,j))
			if (arr[i][j] & 1):
				if (count < 2 or count > 3):
					arr[i][j] = 1
				else:
					arr[i][j] |= 2
			else:
				if count == 3:
					arr[i][j] |= 2
				else:
					arr[i][j] = 0

	for i in range(m):
		for j in range(n):
			arr[i][j] >>= 1
	return arr

if __name__ == '__main__':
	test_arr = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0]]
	next = main(test_arr)
	print(next)




