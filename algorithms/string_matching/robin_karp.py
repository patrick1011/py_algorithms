def robin_karp(text, pattern):
    prime = 101
    last_hash = compute_hash(text[:len(pattern)], prime) * prime
    pattern_hash = compute_hash(pattern, prime)
    last_val, next_val, i = 0, 0, 0
    max_length = (len(text) - len(pattern))
    while i <= max_length:
        new_hash = compute_rolling_hash(
            last_hash=last_hash,
            last_val=last_val,
            next_val=next_val,
            prime=prime,
            m=len(pattern)
        )
        if new_hash == pattern_hash:
            return True
        last_hash = new_hash
        last_val = text[i]
        if i <= max_length:
            next_val = text[i + len(pattern)]
        i += 1
    return False


def compute_hash(pattern, prime):
    _sum = 0
    for i, elem in enumerate(pattern):
        _sum = _sum + elem * pow(prime, i)
    return _sum


def compute_rolling_hash(last_hash, last_val, next_val, prime, m):
    return (last_hash - last_val)/prime + next_val * pow(prime, m - 1)

if __name__ == '__main__':
    text = [1, 2, 10, 1, 2, 3, 1, 2, 3, 1, 2, 17]
    pattern = [1, 2, 3, 1, 2, 17]
    print(robin_karp(text, pattern))
