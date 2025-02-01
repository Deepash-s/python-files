def countDigits(n: int) -> int:
    digits = []
    original = n
    count = 0

    while (n > 0) : 
        lastDigit = n % 10
        digits.append(lastDigit)
        n = n // 10

    for digit in digits:
        if digit != 0 and original % digit == 0:
            count+=1
        
    return count