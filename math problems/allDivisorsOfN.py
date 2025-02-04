n = int(input('Enter a number:'))

div = []

if n==0:
    print(0)
else:
    for i in range(1,n+1):
        if n%i==0:
            div.append(i)
        
for i in div:
    print(i,end=' ')