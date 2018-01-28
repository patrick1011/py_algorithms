"""
    Rod Cutting:
"""


def solve(n_total, p):
    memo = {}
    s = {}
    def dp(n):
        if n not in memo:
            max_so_far = 0
            j = 0
            for i in range(1, n + 1):
                if max_so_far < p[i] + dp(n - i):
                    max_so_far = p[i] + dp(n - i)
                    j = i
            memo[n] = max_so_far
            s[n] = j
        print(s)
        return memo[n]
    return dp(n_total)

if __name__ == '__main__':
    prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    print(solve(8, prices))
