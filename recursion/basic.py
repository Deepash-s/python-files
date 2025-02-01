n = 1

def recursion(n):
    if n>5:
        return
    print(n)
    n+=1
    recursion(n)

recursion(n)