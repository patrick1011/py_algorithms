"""
Given an expression string exp , write a program
to examine whether the pairs and the orders of
“{“,”}”,”(“,”)”,”[“,”]” are correct in exp. For
example, the program should print true for
exp = “[()]{}{[()()]()}” and false for exp = “[(])”

http://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/
"""
from data_structures.stack import Stack


def closes_bracket(top_char, char):
    if (top_char == '(') and (char == ')') or   \
        (top_char == '{') and (char == '}') or  \
        (top_char == '[') and (char == ']'):
        return True
    return False


def ans(input_str):
    char_stack = Stack()
    for _, char in enumerate(input_str):
        if char in ['(', '[', '{']:
            char_stack.push(char)
        if char in [')', ']', '}']:
            try:
                top_char = char_stack.top()
            except ValueError:
                return False
            if closes_bracket(top_char, char):
                char_stack.pop()
            else:
                return False
    return char_stack.isEmpty()


example_1 = '([])'
print(ans(example_1))
example_2 = '[(])'
print(ans(example_2))
