from math import sqrt

def verify_prime(n):
	u_bound = int(sqrt(n))
	for i in range(2, u_bound):
		if n % i == 0:
			return False
	return True

n = 23
print(verify_prime(n))