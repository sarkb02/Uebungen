n = 1
while n <= 100:
    if (n % 3 == 0) & (n % 5 == 0):
        print("Digital History")
    elif n % 5 == 0:
        print("History")
    elif n % 3 == 0:
        print("Digital")
    else:
        print(n)
    n = n + 1 # n += 1