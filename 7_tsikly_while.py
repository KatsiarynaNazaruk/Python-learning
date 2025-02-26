# До КОНЦА 1
text = input()
while text != "КОНЕЦ":
    print(text)
    text = input()


# До КОНЦА 2
text = input()
while text != "КОНЕЦ" and text != "конец":
    print(text)
    text = input()


# Количество членов
text = input()
counter = 0
while text != "стоп" and text != "хватит" and text != "достаточно":
    counter += 1
    text = input()
print(counter)


# Пока делимся
n = int(input())
while n % 7 == 0:
    print(n)
    n = int(input())


# Сумма чисел
n = int(input())
total = 0
while n >= 0:
    total += n
    n = int(input())
print(total)


# Количество пятёрок
n = int(input())
counter = 0
while 1 <= n <= 5:
    if n == 5:
        counter += 1
    n = int(input())
print(counter)


# Ведьмаку заплатите чеканной монетой
price = int(input())
counter = 0
while price >= 25:
    n25 = price // 25
    counter += n25
    price = price - n25 * 25
while price >= 10:
    n10 = price // 10
    counter += n10
    price = price - n10 * 10
while price >= 5:
    n5 = price // 5
    counter += n5
    price = price - n5 * 5
while price >= 1:
    n1 = price // 1
    counter += n1
    price = price - n1 * 1
print(counter)


# Обратный порядок 1
n = int(input())
while n != 0:
    last = n % 10
    print(last)
    n = n // 10


# Обратный порядок 2
n = int(input())
num = ""
while n != 0:
    last = n % 10
    num = num + str(last)
    n = n // 10
print(int(num))


# max и min
n = int(input())
minnum = 9
maxnum = 0
while n != 0:
    num = n % 10
    if num < minnum:
        minnum = num
    if num > maxnum:
        maxnum = num
    n = n // 10
print("Максимальная цифра равна", maxnum)
print("Минимальная цифра равна", minnum)


# Все вместе
n = int(input())
summa = 0
kolvo = 0
proizv = 1
srarifm = 0
pervaia = 0
sum_perv_posl = 0
posl = n % 10

while n != 0:
    num = n % 10
    summa += num
    kolvo += 1
    proizv *= num
    srarifm = summa / kolvo
    pervaia = num
    n = n // 10
sum_perv_posl = pervaia + posl
print(summa, kolvo, proizv, srarifm, pervaia, sum_perv_posl, sep="\n")


# Вторая цифра
n = int(input())
while n > 9:
    num = n % 10
    num2 = num
    n = n // 10
print(num2)


# Одинаковые цифры
n = int(input())
number = n % 10
counter = 0
while n != 0:
    num = n % 10
    if num != number:
        counter += 1
    n = n // 10
if counter != 0:
    print("NO")
else:
    print("YES")


# Упорядоченные цифры
n = int(input())
last = n % 10
flag = "YES"
while n != 0:
    num = n % 10
    if num < last:
        flag = "NO"
    last = num
    n = n // 10
print(flag)


# Наименьший делитель
n = int(input())
for i in range(2, n + 1):
    if n % i == 0:
        break
print(i)


# Следуй правилам
n = int(input())
for i in range(1, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)
