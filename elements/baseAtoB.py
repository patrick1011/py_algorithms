def base1to2(_str, b1, b2):
    out = 0
    for i, val in enumerate(_str):
        out = out * 10
        if ord('0') <= ord(val) <= ord('9'):
            out += (ord(val) - ord('0'))
        else:
            out += 10 + (ord(val) - ord('A') + 1)
    return out


def baseBto10(_str, b):
    out = 0
    for i, val in enumerate(_str):
        if ord('0') <= ord(val) <= ord('9'):
            contribution = (ord(val) - ord('0'))
        else:
            contribution = ord(val) - ord('A') + 10
        out += pow(b, len(_str) - i - 1) * contribution
    return out

print(baseBto10('FFF', 16))
