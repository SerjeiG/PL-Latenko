month = int(input("Введите номер месяца \n"))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("В месяце 31 день")
elif month == 2:
    print("В месяце 28 дней")
elif month > 12 | month < 1:
    print("Такого месяца нет")
else:
    print("В месяце 30 дней")