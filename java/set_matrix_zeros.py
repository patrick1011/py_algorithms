# Given an m x n matrix of 0s and 1s, if an element is 0, set its entire row and column to 0.

# Do it in place.

# Example

# Given array A as

# 1 0 1
# 1 1 1 
# 1 1 1
# On returning, the array A should be :

# 0 0 0
# 1 0 1
# 1 0 1
# Note that this will be evaluated on the extra memory used. 
# Try to minimize the space and time complexity.


## thoughts : brute force: iterator through m * n elements.  For each check flip (m + n) other elements.
#				O(m * n * max(m + n))


# can store column and row indicies to set to 0 in a hash table: space O(m + n), time O(2 * m * n).
# Could instead store bits -> 1 leave unchanged, -> 0 flip.


def main():
	n = m = 3;
	a = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]

	if not A:
		return []

	c, r = pow(2, m) - 1, pow(2, n) - 1

	for i in range(len(a)):
		for j in range(len(a[0])):
			if a[i][j] == 0:
				rbitmask |= 1 << i
				cbitmask |= 1 << j

	for i in range(len(a)):
		for j in range(len(a[0])):
			if (r(bitmask >> i) & 1) or ((cbitmask >> j) & 1):
				a[i][j] = 0

	print(a)


main()










