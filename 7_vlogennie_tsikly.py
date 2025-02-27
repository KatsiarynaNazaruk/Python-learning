#Таблица-1
n = int(input())
for i in range(n):
    for j in range(3):
        print(n, end = ' ')
    print()


#Таблица-2
n = int(input())
for i in range(n):
    for j in range(5):
        print(i+1, end = ' ')
    print()

#Таблица-3
n = int(input())
for i in range(1, n + 1):
    for j in range(1,10):
        print(i, '+', j, '=', i + j)
    print()


#Звёздный треугольник
n = int(input())
for i in range(1, n//2+2):
    for j in range(i):
        print('*', end = '')
    print()
for i in range(n//2, 0, -1):
    for j in range(i):
        print('*', end = '')
    print()



#Численный треугольник 1
n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end = '')
    print()


#12 месяцев
total = 0 
2	for n in range(1, 13):
3	    for k in range(1, 12):
4	        for m in range(1, 11):
5	            if 28 * n + 30 * k + 31 * m == 365:
6	                total += 1
7	                print('n =', n, 'k =', k, 'm =', m)


#Старинная задача
total = 0
for n in range(1, 10):
    for k in range(1, 20):
        for m in range(1, 200):
            if 10 * n + 5 * k + 1/2 * m == 100:
                if n + k + m == 100:
                    total += 1
                    print('n =', n, 'k =', k, 'm =', m)
print('Общее количество натуральных решений =', total)


#Численный треугольник 2
n = int(input())
a = 0
for i in range(1,n + 1):
    for j in range(i):
        a = a + 1
        print(a, end = ' ')
    print()












