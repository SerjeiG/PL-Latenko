n = int(input("Введите количество чисел N (n < 9): "))
s = ""
for i in range(1, n+2):
    for a in range(1, i):
        s += str(a)
    print(s)
    s = ""