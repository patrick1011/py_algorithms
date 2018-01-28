def str_to_int(x):
    out, j = 0, 1
    for _, _chr in enumerate(reversed(x)):
        if _chr == '-':
            out *= -1
        else:
            out += (ord(_chr) - ord('0')) * j
            j *= 10
    return out

print(str_to_int('-123'))
