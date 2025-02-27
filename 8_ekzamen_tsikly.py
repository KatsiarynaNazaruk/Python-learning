# Ревью кода-7
n = int(input())
s = 0
while n > 0:
    num = n % 10
    if num % 2 == 0:
        s += num
    n //= 10
print(s)


# Ревью кода-8
n = 8
count = 0
maximum = -(10**12)
for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print("NO")


# Ревью кода-9
n = 4
count = 0
maximum = -(10**8)
for i in range(1, n + 1):
    x = int(input())
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print("NO")


# Звёздная рамка
n = int(input())
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * 19)
    else:
        print("*", " " * 15, "*")


# Третья цифра
n = int(input())
while n > 99:
    num = n % 10
    n = n // 10
print(num)


# Все вместе 2
n = int(input())
last = n % 10
kolvo = 0
posl = 0
chetn = 0
summa5 = 0
proizv7 = 1
skolko05 = 0

while n > 0:
    num = n % 10
    if num == 3:
        kolvo += 1
    if num == last:
        posl += 1
    if num % 2 == 0:
        chetn += 1
    if num > 5:
        summa5 += num
    if num > 7:
        proizv7 *= num
    if num == 0 or num == 5:
        skolko05 += 1
    n = n // 10

print(kolvo, posl, chetn, summa5, proizv7, skolko05, sep="\n")
