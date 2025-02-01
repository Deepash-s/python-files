import math
from collections import *
from sys import *
from os import *

n = int(input())
if n <= 1:
    print("NO")
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print("YES")
    else:
        print("NO")



