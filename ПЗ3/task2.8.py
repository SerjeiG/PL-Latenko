x = int(input("Введите х: "))
y = int(input("Введите y: "))
if x<2 & y==2:
    B = x * y
elif x > y:
    B = y**2 + x**2
else:
    B = x**2 + 2

print(f"Ответ: {B}")