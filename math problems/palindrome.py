n=int(input())  

original = n
reverse = 0

while n>0:
    ld = n % 10
    reverse = (reverse*10) + ld
    n = n//10

if reverse == original:
    print('true')
else:
    print('false')