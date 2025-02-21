# Начало столетия
year = int(input())
if year % 100 == 0:
    print("YES")
else:
    print("NO")

# Шахматная доска
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if (a + b) % 2 == 0 and (c + d) % 2 == 0:
    print("YES")
elif (a + b) % 2 == 1 and (c + d) % 2 == 1:
    print("YES")
else:
    print("NO")

# Girls only
num = int(input())
pol = input()
if pol == "m":
    print("NO")
else:
    if 10 <= num <= 15:
        print("YES")
    else:
        print("NO")


# Римские цифры
a = int(input())
if a == 1:
    print("I")
elif a == 2:
    print("II")
elif a == 3:
    print("III")
elif a == 4:
    print("IV")
elif a == 5:
    print("V")
elif a == 6:
    print("VI")
elif a == 7:
    print("VII")
elif a == 8:
    print("VIII")
elif a == 9:
    print("IX")
elif a == 10:
    print("X")
else:
    print("ошибка")

# YES or NO – вот в чём вопрос
a = int(input())
if a % 2 == 1:
    print("YES")
else:
    if 2 <= a <= 5:
        print("NO")
    elif 6 <= a <= 20:
        print("YES")
    elif a > 20:
        print("NO")

# Ход слона
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 - a1 == b2 - b1 or a2 - a1 == b1 - b2:
    print("YES")
else:
    print("NO")


# Ход коня
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if (a2 - a1 == 2 or a1 - a2 == 2) and (b2 - b1 == 1 or b1 - b2 == 1):
    print("YES")
elif (a2 - a1 == 1 or a1 - a2 == 1) and (b2 - b1 == 2 or b1 - b2 == 2):
    print("YES")
else:
    print("NO")


# Ход ферзя
a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
if a2 == a1:
    print("YES")
elif b2 == b1:
    print("YES")
elif a1 - a2 == b1 - b2 or a2 - a1 == b2 - b1 or a1 - a2 == b2 - b1:
    print("YES")
else:
    print("NO")
