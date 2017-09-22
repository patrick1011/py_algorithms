"""
    https://leetcode.com/problems/reverse-integer/discuss/

    First came up with crap solution sol1 (40 mins of wrestling with bugs).
    Read sol2 on comments and implemented.

    Take homes: THINK ABOUT THE PROBLEM A LOT MORE WITH PEN AND PAPER.
"""

from math import log10, floor


def sol2(x):
    abs_in = abs(x)
    out = 0
    while abs_in is not 0:
        out = (out * 10) + abs_in % 10
        abs_in = int(abs_in / 10)
        if abs(out) > 2147483647:
            return 0
    return int(out * (x / abs(x)))


def reverse(x):
    abs_in = abs(x)
    if abs_in == 0:
        return 0
    digits = floor(log10(abs_in))
    out = 0
    i = 1
    while i < digits + 2:
        out += (int(abs_in / pow(10, (i - 1))) % 10) * pow(10, digits - (i - 1))
        i += 1
    out = int(out * (x / abs(x)))
    if abs(out) > 2147483647:
        return 0
    return out

if __name__ == '__main__':
    num = 1234123
    ans = sol2(num)
    print(ans)
