def add(x, y):
	out, carry = x ^ y, x & y
	while carry:
		carry <<= 1
		out, carry = carry  ^ out,  carry & out
	return out
