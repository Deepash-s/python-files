n=5

for i in range(n):
        for j in range(n-1,n-i-1-1,-1):
            print(chr(65 + j), end=" ")
        print()