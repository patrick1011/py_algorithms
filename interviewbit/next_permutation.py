# Implement the next permutation, which reaanges numbers into the numerically next greater permutation of numbers.

# If such aangement is not possible, it must be reaanged as the lowest possible order ie, sorted in an ascending order.

# The replacement must be in-place, do not allocate extra memory.

# Examples:

# 1,2,3 → 1,3,2

# 3,2,1 → 1,2,3

# 1,1,5 → 1,5,1

# 20, 50, 113 → 20, 113, 50
# Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# next 'largest' number...

# 6 2 7 9 5
# 6 2 7 5 9 <- flip adjacent
# 6 2 9 5 7 <- flip found

# 1 2 3 7 6 2
# 1 2 3 7 2 6 <- flip adjacent
# 1 2 3 2 7 6 <- flip adjacent
# 1 2 6 2 7 3 <- flip found

# O(log(n)) -> find first element < any one to the right, flip them and sort all elements to the right.

# Is it possible to keep the right part already sorted? -> not in linear time. !!!!! but we are guaranteed these are increasing.

# First flip 5 and 2 then recursively call function on entries thatsre to the right
# 6 5 9 7 2

# 6 5 2 9 7

# compare r to l
#  if r > l flip
#  else 
#	  /// want to flip ASAP with any bit that comes along.

def next_permutaiton(a):
	if len(a) <= 1:
		return a
	for i in range(len(a)-1, 0,-1):
		if a[i] > a[i-1]:
			nli = i
			for j in range(i, len(a)):
				if a[i-1] < a[j] < a[nli]:
					nli = j
			a[nli], a[i-1] = a[i-1], a[nli]
			a = a[:i] + list(reversed(a[i:]))
			return a
	a.reverse()
	return a


arr = [319, 695, 52]
# test = list(arr)
print(next_permutaiton(arr))
# ans = [695, 319, 52]
# exp = [695, 52, 319]