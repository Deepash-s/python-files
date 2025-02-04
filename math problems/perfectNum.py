n = int(input('Enter a number:'))
original = n
div = []

if n==0:
    print(0)
else:
    for i in range(1,n+1):
        if n%i==0:
            div.append(i)

div.pop()
sum = 0
for i in div:
    sum+=i

if sum==original:
    print(True)
else:
    print(False)
