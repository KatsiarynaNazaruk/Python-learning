# 1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[:12])


# 2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[-9:])


# 3
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])


# 4
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[::7])


# Палиндром
s = input()
s1 = s[::-1]
if s == s1:
    print("YES")
else:
    print("NO")


# Делаем срезы 1
s = input()
kolvo = len(s)
tri = s * 3
first = s[0]
first3 = s[0:3]
last3 = s[-3:]
obrat = s[::-1]
udal = s[1:-1]
print(kolvo, tri, first, first3, last3, obrat, udal, sep="\n")


# Делаем срезы 2
s = input()
third = s[2]
predposl = s[-2]
first5 = s[:5]
nolast2 = s[:-2]
chetn = s[::2]
nechetn = s[1::2]
obrat = s[::-1]
obrat2 = s[::-2]
print(third, predposl, first5, nolast2, chetn, nechetn, obrat, obrat2, sep="\n")


# Две половинки
s = input()
mid = len(s) // 2 + len(s) % 2
s1 = s[:mid]
s2 = s[mid:]
print(s2 + s1)


# Заглавные буквы
s = input()
s1 = s.title()
if s == s1:
    print("YES")
else:
    print("NO")


# sWAP cASE
s = input()
s1 = s.swapcase()
print(s1)


# Хороший оттенок
s = input()
s1 = s.lower()
p = "хорош"
if p in s1:
    print("YES")
else:
    print("NO")


# Нижний регистр
s = input()
cnt = 0
for i in range(len(s)):
    if s[i] in "abcdefghijklmnopqrstuvwxyz" and s[i] not in "0123456789":
        cnt += 1
print(cnt)


# Количество слов
s = input()
print(s.count(" ") + 1)


# Минутка генетики
s = input()
s1 = s.lower()
a = s1.count("а")
g = s1.count("г")
c = s1.count("ц")
t = s1.count("т")
print("Аденин:", a)
print("Гуанин:", g)
print("Цитозин:", c)
print("Тимин:", t)


# Очень странные дела
n = int(input())
cnt = 0
while n > 0:
    s = input()
    if s.count("11") >= 3:
        cnt += 1
    n = n - 1
print(cnt)


# Количество цифр
s = input()
cnt = 0
for i in range(len(s)):
    if s[i] in "0123456789":
        cnt += 1
print(cnt)


# .com or .ru
s = input()
if s.endswith(".com") == True or s.endswith(".ru") == True:
    print("YES")
else:
    print("NO")


# Самый частотный символ
s = input()
cnt = 0
let = ""
for i in range(len(s)):
    num = s.count(s[i])
    if num >= cnt:
        cnt = num
        let = s[i]
print(let)


# Первое и последнее вхождение
s = input()
cnt = 0
for i in range(len(s)):
    if s[i] == "f":
        cnt += 1
if cnt == 0:
    print("NO")
elif cnt == 1:
    print(s.find("f"))
elif cnt > 1:
    print(s.find("f"), s.rfind("f"))


# Удаление фрагмента
s = input()
first = s.find("h")
last = s.rfind("h")
s1 = s.replace(s[first : last + 1], "")
print(s1)
