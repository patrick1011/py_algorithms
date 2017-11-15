import sys
from math import floor


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    valid = False
    ftd = [s[0:i+1] for i in range(floor(len(s) / 2))]
    for c in ftd:
        next_int, i = c, 0
        while i < len(s):
            if next_int != ''.join(s[i:i+len(next_int)]):
                break
            i += len(next_int)
            next_int = str(int(next_int) + 1)
        if i == len(s):
            valid = True
            print('YES ' + c)
    if valid is False:
        print('NO')
