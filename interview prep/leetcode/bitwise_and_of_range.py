from math import log

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        if (m == n):
            return m
        shift = int(log(m ^ n, 2))
        return m >> shift << shift
        
