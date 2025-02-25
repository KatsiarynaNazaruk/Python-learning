# Python is awesome
for i in range(10):
    print("Python is awesome!")

# Последовательность символов
for i in range(6):
    print("AAA")

for i in range(5):
    print("BBBB")

print("E")

for i in range(9):
    print("TTTTT")

print("G")

# Повторяй за мной 1
predl = input()
kolvo = int(input())

for i in range(kolvo):
    print(predl)


# Звёздный прямоугольник
n = int(input())

for i in range(n):
    print("*" * 19)


# Повторяй за мной 2
text = input()

for i in range(10):
    print(i, text)


# Квадрат числа
n = int(input())

for i in range(n + 1):
    print("Квадрат числа", i, "равен", i * i)


# Звёздный треугольник
n = int(input())

for i in range(n):
    print("*" * (n - i))


# Популяция
m, p, n = int(input()), int(input()), int(input())
print("1", m)
for i in range(n - 1):
    o = m * (p / 100 + 1)
    print(i + 2, o)
    m = o

# Последовательность чисел 1
m, n = int(input()), int(input())
for i in range(m, n + 1):
    print(i)


# Последовательность чисел 2
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1):
        print(i)
elif m > n:
    for i in range(m, n - 1, -1):
        print(i)
elif m == n:
    print(m)


# Последовательность чисел 3
m, n = int(input()), int(input())
for i in range(m, n - 1, -1):
    if i % 2 == 1:
        print(i)


# Последовательность чисел 4
m, n = int(input()), int(input())

for i in range(m, n + 1):
    if i % 17 == 0:
        print(i)
    elif i % 10 == 9:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print(i)


# Таблица умножения
n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", i * n)


# Количество чисел
a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    if (i**3) % 10 == 4 or (i**3) % 10 == 9:
        counter += 1
print(counter)


# Сумма чисел
n = int(input())
total = 0
for i in range(n):
    num = int(input())
    total += num
print(total)


# Асимптотическое приближение
from math import *

n = int(input())
total = 0
for i in range(1, n + 1):
    total = total + 1 / i
new = total - log(n)
print(new)


# Сумма чисел 2
n = int(input())
total = 0
for i in range(1, n + 1):
    if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
        total = total + i
print(total)


# Факториал
n = int(input())
total = 1
for i in range(1, n + 1):
    total = total * i
print(total)


# Без нулей
total = 1
for i in range(10):
    num = int(input())
    if num != 0:
        total = total * num
print(total)


# Сумма делителей
n = int(input())
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        total += i
print(total)


# Знакочередующаяся сумма
n = int(input())
total1 = 0
total2 = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        total1 = total1 - i
    elif i % 2 == 1:
        total2 = total2 + i
print(total1 + total2)
