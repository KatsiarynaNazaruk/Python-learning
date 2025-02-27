# 1
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[7])


# 2
s = "In 2010, someone paid 10k Bitcoin for two pizzas."
print(s[39])


# В столбик
s = input()
for i in range(0, len(s), 2):
    print(s[i])


# В столбик 2
s = input()
for i in range(len(s) - 1, -1, -1):
    print(s[i])


# ФИО
name = input()
surname = input()
patr = input()

print(surname[0], name[0], patr[0], sep="")


# Цифра 1
s = input()
sum = 0
for i in range(0, len(s)):
    sum += int(s[i])
print(sum)


# Цифра 2
s = input()
flag = False
for i in range(0, len(s)):
    if s[i] in "0123456789":
        flag = True
        break
if flag == True:
    print("Цифра")
else:
    print("Цифр нет")


# Сколько раз?
s = input()
counter1 = 0
counter2 = 0
for i in range(0, len(s)):
    if s[i] in "+":
        counter1 += 1
    if s[i] in "*":
        counter2 += 1
print("Символ + встречается", counter1, "раз")
print("Символ * встречается", counter2, "раз")


# Одинаковые соседи
s = input()
cnt = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        cnt += 1
print(cnt)


# Гласные и согласные
s1 = input()
s = s1.lower()
cnt_g = 0
cnt_s = 0
for i in range(len(s)):
    if s[i] in "ауоыиэяюе":
        cnt_g += 1
    if s[i] in "бвгджзйклмнпрстфхцчшщ":
        cnt_s += 1
print("Количество гласных букв равно", cnt_g)
print("Количество согласных букв равно", cnt_s)
