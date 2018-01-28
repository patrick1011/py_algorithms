"""
    https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


def sol(_input):

    seen = {}
    for _, char in enumerate(_input):
        seen[char] = False

    j = 0
    len_so_far = 0
    max_len = 0
    for _, char in enumerate(_input):
        if not seen[char]:
            seen[char] = True
            len_so_far += 1
            if len_so_far > max_len:
                max_len = len_so_far
        else:
            found_repeat = False
            while not found_repeat:
                if char is _input[j]:
                    found_repeat = True
                else:
                    seen[_input[j]] = False
                    len_so_far -= 1
                j += 1

    return max_len

if __name__ == '__main__':
    str1 = "abcabcbbeqbb"
    print(sol(str1))
