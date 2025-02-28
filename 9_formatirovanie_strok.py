# Плохие комментарии
n = int(input())
for i in range(n):
    s = input()
    if s.isspace() == True or s == "":
        print(i + 1, ": ", "COMMENT SHOULD BE DELETED", sep="")
    else:
        print(i + 1, ": ", s, sep="")


# Автомобильный номер
s = input()
s1 = s[0]
s2 = s[1:4]
s3 = s[4:6]
s4 = s[7:]
if (
    s1 in "АВЕКМНОРСТУХ"
    and s2.isdigit() == True
    and s[4] in "АВЕКМНОРСТУХ"
    and s[5] in "АВЕКМНОРСТУХ"
    and s[6] == "_"
    and s4.isdigit() == True
    and (len(s4) == 2 or len(s4) == 3)
):
    print("YES")
else:
    print("NO")


# Проверь никнейм
s = input()

if s.startswith("@") and 5 <= len(s) <= 15 and s[1:].isalnum() and s == s.lower():
    print("Correct")
else:
    print("Incorrect")


# 1
year = 2010
price = "10k"
cur = "Bitcoin"
s = "In {0}, someone paid {1} {2} for two pizzas.".format(year, price, cur)
print(s)


# 2
year = 2010
price = "10K"
cur = "Bitcoin"
s = f"In {year}, someone paid {price} {cur} for two pizzas."
print(s)


# Курсы валют
date, euro, uan = input(), input(), input()
s = f"На {date}: 1€ = {euro}₽, 1¥ = {uan}₽"
print(s)


# Сумма кубов/Куб суммы
a, b = int(input()), int(input())
summa_kubov = a**3 + b**3
kub_summi = (a + b) ** 3
print(f"Для чисел {a} и {b}:")
print(f"  Сумма кубов: {a}**3 + {b}**3 = {summa_kubov}")
print(f"  Куб суммы: ({a} + {b})**3 = {kub_summi}")


# (Не) Активное похудение
den = int(input())
ves = float(input())
if ves <= 100 - 0.2 * den:
    print("Все идет по плану")
    print(f"#{den} ДЕНЬ: ТЕКУЩИЙ ВЕС = {ves} кг, ЦЕЛЬ по ВЕСУ = {100 - 0.2 * den} кг")
else:
    print("Что-то пошло не так")
    print(f"#{den} ДЕНЬ: ТЕКУЩИЙ ВЕС = {ves} кг, ЦЕЛЬ по ВЕСУ = {100 - 0.2 * den} кг")
