n = int(input("Enter a number:"))

reverse = 0

while n >0:
    ld = n % 10
    reverse = (reverse*10)+ld
    n = n//10

print(reverse)
