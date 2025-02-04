def printNos(n,current=1):
        if current<=n:
            print(current, end=' ')
            printNos(n, current+1)
        else:
            return

printNos(10)