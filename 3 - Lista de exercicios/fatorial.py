n = int(input("digite um numero para fatorar: "))
i = 1
fat = n
if fat == 0:
    print(fat+1)
else:
    while i < n:
        fat = fat * (n - i)
        i = i + 1

    print(fat)