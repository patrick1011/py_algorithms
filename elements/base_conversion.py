from math import pow, floor, log

def char_to_int(char):
	if ord(char) <= ord('9'):
		return ord(char) - ord('0')
	return ord(char) - ord('A') + 10

def to_base_ten(s, b):
	int_s = 0
	for i, char in enumerate(reversed(s)):
		int_s += pow(b, i) * char_to_int(char)
	return int_s

def to_base_b(int_s, b):
	_max, out = floor(log(int_s, b)), ''
	for i in range(_max + 1):
		contrib = int(int_s // pow(b, _max - i))
		out = out + str(contrib)
		int_s -= pow(b, _max - i) * contrib
	return out

print(to_base_b(123, 4))
# print(to_base_ten('1323', 4))
