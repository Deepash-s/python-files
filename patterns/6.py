n = int(input("Enter a number: "))

for i in range(n,-1,-1):
    for j in range(i):
        print(j+1,end=' ')
    print(end='\n') 