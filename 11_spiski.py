# Список чисел
n = int(input())
mylist = list(range(1, n + 1))
print(mylist)


# Список букв
n = int(input())
s = "abcdefghijklmnopqrstuvwxyz"
s1 = s[:n]
list1 = list(s1)
print(list1)


# 1
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[16])


# 2
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[-1])


# 3
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
print(primes[:6])


# 4
numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
print(min(numbers) + max(numbers))


# 5
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)


# 6
rainbow = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
rainbow[3] = "Зеленый"
rainbow[6] = "Фиолетовый"
print(rainbow)


# 7
languages = [
    "Chinese",
    "Spanish",
    "English",
    "Hindi",
    "Arabic",
    "Bengali",
    "Portuguese",
    "Russian",
    "Japanese",
    "Lahnda",
]
languages2 = languages[::-1]
print(languages2)


# 8
numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]
numbers4 = numbers1 * 2 + numbers2 * 9 + numbers3
print(numbers4)


# Все сразу 1
numbers = [
    2,
    6,
    3,
    14,
    10,
    4,
    11,
    16,
    12,
    5,
    4,
    16,
    1,
    0,
    8,
    16,
    10,
    10,
    8,
    5,
    1,
    11,
    10,
    10,
    12,
    0,
    0,
    6,
    14,
    8,
    2,
    12,
    14,
    5,
    6,
    12,
    1,
    2,
    10,
    14,
    9,
    1,
    15,
    1,
    2,
    14,
    16,
    6,
    7,
    5,
]
print(len(numbers))
print(numbers[-1])
print(numbers[::-1])
if 5 in numbers and 17 in numbers:
    print("YES")
else:
    print("NO")
numbers2 = numbers[1:-1]
print(numbers2)


# Список строк
n = int(input())
list1 = []
for i in range(n):
    s = input()
    list1.append(s)
print(list1)


# Алфавит
l = []
let = 97
for i in range(1, 27):
    l.append(chr(let) * i)
    let += 1
print(l)


# Список кубов
n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a**3)
print(l)


# Список делителей
n = int(input())
l = []
for i in range(1, n + 1):
    if n % i == 0:
        l.append(i)
print(l)


# Суммы двух
n = int(input())
first = int(input())
l = []
for i in range(n - 1):
    b = int(input())
    l.append(first + b)
    first = b
print(l)


# Удалите нечётные индексы
n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a)
l2 = l[::2]
print(l2)


# k-ая буква слова
n = int(input())
l = []
a = ""
for i in range(n):
    s = input()
    l.append(s)
k = int(input())
for i in range(len(l)):
    if k <= len(l[i]):
        a += (l[i])[k - 1]
print(a)


# Символы всех строк
n = int(input())
l = []
for i in range(n):
    s = input()
    l.extend(s)
print(l)


# 1
numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
res = 0
for i in range(len(numbers)):
    res += numbers[i] ** 2
print(res)


# Значение функции
n = int(input())
l = []
res = 0
for i in range(n):
    s = int(input())
    l.append(s)
    print(s)
print()
for i in range(len(l)):
    res = l[i] ** 2 + 2 * l[i] + 1
    print(res)


# Remove outliers
n = int(input())
l = []
for i in range(n):
    num = int(input())
    l.append(num)
minn = min(l)
ind_min = l.index(minn)
del l[ind_min]
maxx = max(l)
ind_max = l.index(maxx)
del l[ind_max]
print(*l, sep="\n")


# Без дубликатов
n = int(input())
l = []
for i in range(n):
    s = input()
    if s not in l:
        l.append(s)
print(*l, sep="\n")


# Google search - 1
n = int(input())
l = []
for i in range(n):
    s = input()
    l.append(s)
search = input()
for i in range(len(l)):
    if search.lower() in l[i].lower():
        print(l[i])


# Negatives, Zeros and Positives
n = int(input())
neg = []
zero = []
posit = []
for i in range(n):
    num = int(input())
    if num < 0:
        neg.append(num)
    elif num == 0:
        zero.append(num)
    elif num > 0:
        posit.append(num)
print(*neg, sep="\n")
print(*zero, sep="\n")
print(*posit, sep="\n")


# Построчный вывод
s = input()
list1 = s.split()
print(*list1, sep="\n")


# Инициалы
s = input()
list1 = s.split()
list2 = []
for i in range(len(list1)):
    list2.append((list1[i])[0])
print(".".join(list2) + ".")


# Windows OS
s = input()
list1 = s.split("\\")
print(*list1, sep="\n")


# Диаграмма
s = input()
list1 = s.split()
for i in range(len(list1)):
    print(int(list1[i]) * "+")


# Корректный ip-адрес
s = input().split(".")
flag = True
for i in range(4):
    if int(s[i]) > 255 or int(s[i]) < 0:
        flag = False
        break
if flag == True:
    print("ДА")
else:
    print("НЕТ")


# Добавь разделитель
s = input()
print(*s, sep=input())


# Количество совпадающих пар
s = input().split()
counter = 0
current = 0
for i in range(len(s)):
    current = s[i]
    for j in s[(i + 1) :]:
        if j == current:
            counter += 1
        else:
            continue
print(counter)


# Всё сразу 2
numbers = [8, 9, 10, 11]
numbers.remove(numbers[1])
numbers.insert(1, 17)
numbers.extend([4, 5, 6])
numbers.remove(numbers[0])
numbers.extend(numbers)
numbers.insert(3, 25)
print(numbers)


# Переставить min и max
n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])
maxx = max(n)
minn = min(n)
ind_max = n.index(maxx)
ind_min = n.index(minn)
n[ind_max], n[ind_min] = minn, maxx
print(*n)


# Количество артиклей
s = input().split()
s1 = s.count("a")
s2 = s.count("an")
s3 = s.count("the")
s4 = s.count("A")
s5 = s.count("An")
s6 = s.count("The")
total = s1 + s2 + s3 + s4 + s5 + s6
print(f"Общее количество артиклей: {total}")


# Сортировка чисел
s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
print(*s)
s.sort(reverse=True)
print(*s)


# 1
keywords = [
    "False",
    "True",
    "None",
    "and",
    "with",
    "as",
    "assert",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "try",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "while",
    "yield",
]

new_keywords = [i[1:] for i in keywords]

print(new_keywords)


# 2
keywords = [
    "False",
    "True",
    "None",
    "and",
    "with",
    "as",
    "assert",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "try",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "while",
    "yield",
]

lengths = [len(i) for i in keywords]

print(lengths)


# 3
keywords = [
    "False",
    "True",
    "None",
    "and",
    "with",
    "as",
    "assert",
    "break",
    "class",
    "continue",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "finally",
    "try",
    "for",
    "from",
    "global",
    "if",
    "import",
    "in",
    "is",
    "lambda",
    "nonlocal",
    "not",
    "or",
    "pass",
    "raise",
    "return",
    "while",
    "yield",
]

new_keywords = [i for i in keywords if len(i) >= 5]

print(new_keywords)


# 4
palindromes = [i for i in range(100, 1001) if i % 10 == i // 100]

print(palindromes)


# Списочное выражение 1
n = int(input())
kv = [i**2 for i in range(1, n + 1)]
print(*kv, sep="\n")


# Списочное выражение 2
n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])
kub = [(n[i]) ** 3 for i in range(len(n))]
print(*kub)


# В одну строку 1
s = input().split()
print(*s, sep="\n")
