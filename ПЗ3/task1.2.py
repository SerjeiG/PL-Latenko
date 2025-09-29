num = int(input("Введите двухзначное число "))
first_part = num // 10
second_part = num % 10
if first_part == second_part:
    print("Да")
else:
    print("Нет")