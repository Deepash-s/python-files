n = 1

def recursion(n):
    if n<=5:
        print(n)
    else:
        return
    n+=1
    recursion(n)

recursion(n)