
# You are given an array (zero indexed) of N non-negative integers, A0, A1 ,…, AN-1.
# Find the minimum sub array Al, Al+1 ,…, Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted.
# If A is already sorted, output -1.

# Example :

# Input 1:

# A = [1, 3, 2, 4, 5]

# Return: [1, 2]

# Input 2:

# A = [1, 2, 3, 4, 5]

# Return: [-1]
# In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.


# O(n) time O(1) space...
# Iterate through A with l & r incrementing
# When arr[i] > arr[i+1] set l = i
# Then when i == arr.length - 1 or arr[i+1] > arr[l] set r = i, break	

# A = [3, 2, 1] this works.

# Edge cases: 
# 	l=0: 




# example : [2, 6, 4, 8, 10, 9, 15]
# 	l = 1, r = 5
# example : [2, 6, 4, 1, 10, 9, 15]
# 	l = 0, r = 5


# Algorithm:

# Find first element that's not in order i and l will be the
# furthest left element in the array s.t. arr[l] > arr[i].
# if there is no such element l will be 1st element in the array.

# Could do something similar which would be cleaner by...
# computing the min starting from the right.  

# To find the right element do symetric thing or...
# multiply a by -1, reverse then do the above. O(n) operations

# ^						x
# |                       x
# |          x         
# |       x         x  x
# |    x          x
# |x 
# |__________________________


def find_left(a):
	target, l = None, None
	for i in range(1, len(a)):
		if a[i] < a[i-1]:
			target = i
			break

	print(target)

	if target != None:
		for i in range(len(a)):
			if a[target] < a[i]:
				l = i
				break
	return l

def main():
	a = [ 1, 2, 2, 3, 3, 5, 6, 6, 14, 17, 18, 17, 18, 15, 15, 17, 19, 14, 19, 18 ]
	l = find_left(a)
	if l == None:
		return [-1]

	a.reverse()
	for i in range(len(a)):
		a[i] *= -1

	r = len(a) - 1 - find_left(a)

	print(l, r)

	

main()













