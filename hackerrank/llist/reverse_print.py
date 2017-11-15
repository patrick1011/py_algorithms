https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

def ReversePrint(n):
    if n:
        ReversePrint(n.next)
        print(n.data)
