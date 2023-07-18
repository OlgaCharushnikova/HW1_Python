n = int(input("Введите число n: "))
i = 1
while i < n:
    i *= 2
    if i < n:
        print(i, end = ' ') 