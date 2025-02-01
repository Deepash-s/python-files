def checkArmstrong(n):
    digits = len(str(n))
    original = n
    total = 0

    while n>0:
        ld = n%10
        total+=(ld**digits)
        n = n//10

    return total == original         


    