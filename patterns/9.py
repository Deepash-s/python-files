n = 5

for i in range(n):
    for j in range(n-i-1):
        print(' ',end='')
    for j in range(2*i+1):
        print('*',end='')
    print()
for i in range(n,-1,-1):
    for j in range(n-i):
        print(' ',end='')
    for j in range(i*2-1):
        print('*',end='')
    print()