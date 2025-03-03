# Какая следующая буква?
s = input()
ord1 = ord(s)
ord2 = ord1 + 1
if s == "Я":
    print("Дальше букв нет")
else:
    print(chr(ord2))


# Символы в диапазоне
a, b = int(input()), int(input())
for i in range(a, b + 1):
    print(chr(i), end=" ")


# Простой шифр
s = input()
for i in range(len(s)):
    num = ord(s[i])
    print(num, end=" ")


# Самое тяжёлое слово
a, b, c, d = input(), input(), input(), input()
ves_a = 0
ves_b = 0
ves_c = 0
ves_d = 0
for i in range(len(a)):
    ves_a += ord(a[i])
for i in range(len(b)):
    ves_b += ord(b[i])
for i in range(len(c)):
    ves_c += ord(c[i])
for i in range(len(d)):
    ves_d += ord(d[i])
if ves_a >= ves_b and ves_a >= ves_c and ves_a >= ves_d:
    print(a)
elif ves_b >= ves_c and ves_b >= ves_d:
    print(b)
elif ves_c >= ves_d:
    print(c)
else:
    print(d)


# Стоимость ответа
s = input()
total = 0
bee = chr(128029)
for i in range(len(s)):
    total += ord(s[i])
summa = total * 3
print("Текст сообщения: '" + s + "'")
print("Стоимость сообщения: " + str(summa) + bee)


# Накручиваем стоимость ответа
s = input()
total = 0
bee = chr(128029)
for i in range(len(s)):
    total += ord(s[i])
summa = total * 3

s1 = (
    s.replace("e", "е")
    .replace("y", "у")
    .replace("o", "о")
    .replace("p", "р")
    .replace("a", "а")
    .replace("x", "х")
    .replace("c", "с")
    .replace("E", "Е")
    .replace("T", "Т")
    .replace("O", "О")
    .replace("P", "Р")
    .replace("A", "А")
    .replace("H", "Н")
    .replace("X", "Х")
    .replace("C", "С")
    .replace("B", "В")
    .replace("M", "М")
)
total1 = 0
for i in range(len(s1)):
    total1 += ord(s1[i])
summa1 = total1 * 3
print("Старая стоимость: " + str(summa) + bee)
print("Новая стоимость: " + str(summa1) + bee)


# Шифр Цезаря
n = int(input())
s = input()
for i in range(len(s)):
    ord1 = ord(s[i])
    ord2 = ord1 - n
    chr2 = chr(ord2)
    print(chr2, end="")


# Строковые минимум и максимум
a = input()
minn = "яя"
maxx = "А"
while a != "КОНЕЦ":
    if a < minn:
        minn = a
    if a > maxx:
        maxx = a
    a = input()
print(f"Минимальная строка ⬇️: {minn}")
print(f"Максимальная строка ⬆️: {maxx}")


# Волшебное число
a, b, c, d = input(), input(), input(), input()
minn = min(a, b, c, d)
maxx = max(a, b, c, d)
ord1 = ord(minn[-1])
ord2 = ord(maxx[-1])
vol = (ord1 * ord2) ** 2
print(vol)


# Название класса
n = int(input())
for i in range(n):
    klass = input()
    if klass[0] in "0123456789" and klass[-1] in "АБВГДЕЖЗИЙКЛМНОП" and len(klass) == 2:
        print("YES")
    else:
        print("NO")


# Каждый третий
s = input()
s1 = ""
for i in range(len(s)):
    if i % 3 != 0:
        s1 += s[i]
print(s1)


# Замени меня полностью
s = input()
s1 = s.replace("1", "one")
print(s1)


# Удали меня полностью4
s = input()
s1 = s.replace("@", "")
print(s1)


# Второе вхождение
s = input()
if s.count("f") == 0:
    print("-2")
elif s.count("f") == 1:
    print("-1")
elif s.count("f") >= 2:
    n = s.find("f")
    s1 = s[n + 1 :]
    n2 = s1.find("f") + n + 1
    print(n2)
