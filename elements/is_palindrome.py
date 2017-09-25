def is_palindrome(s):
    i = (len(s) // 2) - 1
    while i > 0:
        if s[i] != s[-(i + 1)]:
            return False
        i -= 1
    return True


print(is_palindrome(''))
