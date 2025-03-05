# Список чётных
n = int(input())
mylist = []
for i in range(2, n + 1, 2):
    mylist.append(i)
print(mylist)


# Сумма двух списков
L = input().split()
M = input().split()
N = []
for i in range(len(L)):
    n = int(L[i]) + int(M[i])
    N.append(n)
print(*N)


# Сумма чисел
s = input().split()
total = 0
for i in range(len(s)):
    total += int(s[i])
print("+".join(s) + "=" + str(total))


# Валидный номер
s = input()
s1 = s.split("-")
s2 = "".join(s1)
if len(s2) == 10 and s2.isdigit() == True and s[3] == "-" and s[7] == "-":
    print("YES")
elif (
    len(s2) == 11
    and s2.isdigit() == True
    and s2.startswith("7") == True
    and s[1] == "-"
    and s[5] == "-"
    and s[9] == "-"
):
    print("YES")
else:
    print("NO")


# Самый длинный
s = input().split()
s1 = []
for i in range(len(s)):
    s1.append(len(s[i]))
print(max(s1))


# Молодёжный жаргон
s = input().split()
s2 = []
for i in range(len(s)):
    s2.append((s[i])[1:] + (s[i])[0] + "ки")
print(*s2)
