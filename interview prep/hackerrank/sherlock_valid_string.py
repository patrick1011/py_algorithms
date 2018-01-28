# https://www.hackerrank.com/challenges/sherlock-and-valid-string/forum

def isValid(s):
    freq = Counter(s)
    freq_dist = Counter(freq.values())
    freqs, keys = list(freq_dist.values()), list(freq_dist.keys())
    valid_conditions = (
        len(freq_dist) < 2 or
        len(freq_dist) == 2 and (
            1 in freqs and (
                keys[freqs.index(1)] == 1 or (keys[freqs.index(1)] == min(keys) + 1)
            )
        )
    )
    return 'YES' if valid_conditions else 'NO'
