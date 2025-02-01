letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

for i in range(1,6):
    for j in range(i):
        print(letters[i-1],end=' ')
    print()