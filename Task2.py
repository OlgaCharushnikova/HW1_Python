sum = int(input("Введите сумму чисел: "))
comp = int(input("Введите спроизведение чисел: "))
i = 1
j = 1
c1 = 0
c2 = 0
for i in range(sum - 1):
    for j in range(sum - 1):
        if i * j == comp and i + j == sum:
            c1 = i
            c2 = j
print(f'Сумма = {sum}, Произведение = {comp}. Число 1 = {c1}, Число 2 = {c2}')