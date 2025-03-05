# Звёздный прямоугольник 1
def draw_box():
    print(10 * "*")
    for i in range(12):
        print("*" + "        " + "*")
    print(10 * "*")


draw_box()


# Звёздный треугольник 1
def draw_triangle():
    for i in range(10):
        print("*" * (i + 1))


draw_triangle()


# Звёздный треугольник
# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base // 2 + 2):
        print(fill * i)
    for i in range(base // 2, 0, -1):
        print(fill * i)


# считываем данные
fill = input()
base = int(input())
# вызываем функцию
draw_triangle(fill, base)


# ФИО
def print_fio(name, surname, patronymic):
    print((surname.upper())[0], (name.upper())[0], (patronymic.upper())[0], sep="")


name, surname, patronymic = input(), input(), input()

print_fio(name, surname, patronymic)


# Сумма цифр
def print_digit_sum(num):
    total = 0
    while num > 0:
        a = num % 10
        total += a
        num = num // 10
    print(total)


num = int(input())

print_digit_sum(num)


# Конвертер километров
def convert_to_miles(km):
    miles = km * 0.6214
    return miles


num = int(input())

print(convert_to_miles(num))


# Количество дней
def get_days(month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 28


num = int(input())

print(get_days(num))


# Делители 1
def get_factors(num):
    mylist = []
    for i in range(1, num + 1):
        if num % i == 0:
            mylist.append(i)
    return mylist


n = int(input())

print(get_factors(n))


# Делители 2
def number_of_factors(num):
    mylist = []
    for i in range(1, num + 1):
        if num % i == 0:
            mylist.append(i)
    len1 = len(mylist)
    return len1


n = int(input())

print(number_of_factors(n))


# Найти всех
def find_all(target, symbol):
    mylist = []
    for i in range(len(target)):
        if target[i] == symbol:
            mylist.append(target.find(symbol))
            target = target.replace(symbol, "1", 1)
    return mylist


s = input()
char = input()

print(find_all(s, char))


# Merge lists 1
def merge(list1, list2):
    list3 = list1 + list2
    list3.sort()
    return list3


numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))


# Merge lists 2
def nice():
    q = []
    for i in range(int(input())):
        a = [int(c) for c in input().split()]
        q.extend(a)
    q.sort()
    return q


print(*nice())


# Is the Triangle Valid?
def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return True
    else:
        return False


a, b, c = int(input()), int(input()), int(input())

print(is_valid_triangle(a, b, c))


# Is the Number Prime?
def is_prime(num):
    if num == 1:
        return False  # число 1 не является простым

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # сразу возвращает False, когда находим делитель

    return True


n = int(input())

print(is_prime(n))


# Good password
def is_password_good(password):
    if (
        len(password) >= 8
        and not password.islower()
        and not password.isupper()
        and password.isalnum()
        and not password.isdigit()
        and not password.isalpha()
    ):
        return True
    else:
        return False


txt = input()

print(is_password_good(txt))


# Ровно в одном
def is_one_away(word1, word2):
    cnt = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
    if cnt == 1:
        return True
    else:
        return False


txt1 = input()
txt2 = input()

print(is_one_away(txt1, txt2))
