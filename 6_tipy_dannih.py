# Площадь треугольника
a, b = float(input()), float(input())
s = 0.5 * a * b
print(s)

# Две старушки
s, v1, v2 = float(input()), float(input()), float(input())
t = s / (v1 + v2)
print(t)

# Обратное число
a = float(input())
if a == 0:
    print("Обратного числа не существует")
else:
    print(1 / a)

# 451 градус по Фаренгейту
tf = float(input())
print(5 / 9 * (tf - 32))

# Dog age
age = int(input())
if age <= 2:
    dog_age = age * 10.5
else:
    dog_age = 2 * 10.5 + (age - 2) * 4
print(dog_age)

# Первая цифра после точки
a = float(input())
b = a * 10
c = b % 10
print(int(c))

# Дробная часть
a = float(input())
print(a - int(a))

# Наибольшее и наименьшее
a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
print("Наименьшее число =", min(a, b, c, d, e))
print("Наибольшее число =", max(a, b, c, d, e))

# Сортировка трёх
a, b, c = int(input()), int(input()), int(input())
sum = a + b + c
min_n = min(a, b, c)
max_n = max(a, b, c)
print(max_n)
print(sum - min_n - max_n)
print(min_n)

# Интересное число
abc = int(input())
c = abc % 10
b = (abc % 100) // 10
a = abc // 100
dif = max(a, b, c) - min(a, b, c)
sred = (a + b + c) - max(a, b, c) - min(a, b, c)
if dif == sred:
    print("Число интересное")
else:
    print("Число неинтересное")


# Абсолютная сумма
a1, a2, a3, a4, a5 = (
    float(input()),
    float(input()),
    float(input()),
    float(input()),
    float(input()),
)
total = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)
print(total)

# Манхэттенское расстояние
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
man = abs(p1 - q1) + abs(p2 - q2)
print(man)

# What's Your Name?
name = input()
surname = input()
print("Hello " + name + " " + surname + "! You have just delved into Python")

# Футбольная команда
team = input()
dlina = len(team)
print("Футбольная команда", team, "имеет длину", dlina, "символов")

# Три города
a1, b1, c1 = input(), input(), input()
a = len(a1)
b = len(b1)
c = len(c1)
if a > b > c:
    print(c1)
    print(a1)
elif a > c > b:
    print(b1)
    print(a1)
elif b > a > c:
    print(c1)
    print(b1)
elif b > c > a:
    print(a1)
    print(b1)
elif c > a > b:
    print(b1)
    print(c1)
elif c > b > a:
    print(a1)
    print(c1)

# Арифметические строки
a, b, c = input(), input(), input()
len_a = len(a)
len_b = len(b)
len_c = len(c)
mi = min(len(a), len(b), len(c))
ma = max(len(a), len(b), len(c))
mid = (len_a + len_b + len_c) - mi - ma
d = (ma - mi) / 2
if mid == mi + d:
    print("YES")
else:
    print("NO")

# Цвет настроения синий
a = input()
if "синий" in a:
    print("YES")
else:
    print("NO")

# Отдыхаем ли?
a = input()
if "суббота" in a or "воскресенье" in a:
    print("YES")
else:
    print("NO")


# Корректный email
email = input()
if "@" in email and "." in email:
    print("YES")
else:
    print("NO")

# Евклидово расстояние
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
import math

e = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(e)

# Площадь и длина
r = float(input())
from math import *

s = pi * r**2
c = 2 * pi * r
print(s)
print(c)

# Средние значения
a, b = float(input()), float(input())
from math import *

arif = (a + b) / 2
geom = sqrt(a * b)
garm = 2 * a * b / (a + b)
kvad = sqrt((a**2 + b**2) / 2)
print(arif, geom, garm, kvad, sep="\n")

# Тригонометрическое выражение
from math import *

x = float(input())
r = (x * pi) / 180
z = sin(r) + cos(r) + tan(r) ** 2
print(z)

# Пол и потолок
x = float(input())
from math import *

x1 = floor(x)
x2 = ceil(x)
print(x1 + x2)

# Правильный многоугольник
n, a = float(input()), float(input())
from math import *

s = (n * a**2) / (4 * tan(pi / n))
print(s)
