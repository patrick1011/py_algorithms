"""
http://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
"""


def fibbonaci(n):
    if n < 2:
        return 1
    else:
        return fibbonaci(n - 1) + fibbonaci(n - 2)

memo = {}
def memo_fibbonaci(n):
    if n in memo:
        return memo[n]
    if n < 2:
        f = 1
    else:
        f = memo_fibbonaci(n - 1) + memo_fibbonaci(n - 2)
    memo[n] = f
    return f

if __name__ == '__main__':
    print(fibbonaci(10))
    print(memo_fibbonaci(10))
