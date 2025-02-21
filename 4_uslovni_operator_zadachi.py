print("Hello world")
print("Python")


# Гонка спидстеров
n, k = int(input()), int(input())
if n > k:
    print("NO")
elif n < k:
    print("YES")
elif n == k:
    print("Don't know")

# Вид треугольника
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print("Равносторонний")
elif a == b or a == c or b == c:
    print("Равнобедренный")
else:
    print("Разносторонний")

# Серединное число
a, b, c = int(input()), int(input()), int(input())
if a > b > c or c > b > a:
    print(b)
elif c > a > b or b > a > c:
    print(a)
else:
    print(c)

# Количество дней
a = int(input())
if a == 2:
    print("28")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print("30")
else:
    print("31")

# Церемония взвешивания
a = int(input())
if a < 60:
    print("Легкий вес")
elif 60 <= a < 64:
    print("Первый полусредний вес")
elif 64 <= a < 69:
    print("Полусредний вес")

# Самописный калькулятор
a = int(input())
b = int(input())
c = input()
if c == "+":
    print(a + b)
elif c == "-":
    print(a - b)
elif c == "*":
    print(a * b)
elif c == "/" and b != 0:
    print(a / b)
elif c == "/" and b == 0:
    print("На ноль делить нельзя!")
else:
    print("Неверная операция")


# Цветовой микшер
a, b = input(), input()
if a == "красный":
    if b == "красный":
        print("красный")
    elif b == "синий":
        print("фиолетовый")
    elif b == "желтый":
        print("оранжевый")
    else:
        print("ошибка цвета")
elif a == "желтый":
    if b == "желтый":
        print("желтый")
    elif b == "синий":
        print("зеленый")
    elif b == "красный":
        print("оранжевый")
    else:
        print("ошибка цвета")
elif a == "синий":
    if b == "синий":
        print("синий")
    elif b == "красный":
        print("фиолетовый")
    elif b == "желтый":
        print("зеленый")
    else:
        print("ошибка цвета")
else:
    print("ошибка цвета")

# Цвета колеса рулетки
a = int(input())
if a == 0:
    print("зеленый")
elif 1 <= a <= 10 and a % 2 == 1:
    print("красный")
elif 1 <= a <= 10 and a % 2 == 0:
    print("черный")
elif 11 <= a <= 18 and a % 2 == 1:
    print("черный")
elif 11 <= a <= 18 and a % 2 == 0:
    print("красный")
elif 19 <= a <= 28 and a % 2 == 1:
    print("красный")
elif 19 <= a <= 28 and a % 2 == 0:
    print("черный")
elif 29 <= a <= 36 and a % 2 == 1:
    print("черный")
elif 29 <= a <= 36 and a % 2 == 0:
    print("красный")
elif a > 36 or a < 0:
    print("ошибка ввода")

# Пересечение отрезков
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a2 < a1:
    # теперь отрезок a1, b1 точно левее (по крайней мере своим левым концом) отрезка a2, b2
    a1, b1, a2, b2 = a2, b2, a1, b1

if a2 > b1:
    print("пустое множество")
elif a2 == b1:
    print(a2)
else:
    if b1 < b2:
        print(a2, b1)
    else:
        print(a2, b2)
