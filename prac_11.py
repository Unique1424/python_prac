# Proc16
def Sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

# Используем функцию для выражения
a = float(input())
b = float(input())
result = Sign(a) + Sign(b)
print(result)

# Proc17
def RootsCount(a, b, c):
    d = b * b - 4 * a * c
    if d > 0:
        return 2
    elif d == 0:
        return 1
    else:
        return 0

# Используем функцию для трех уравнений
for i in range(3):
    a = float(input())
    b = float(input())
    c = float(input())
    count = RootsCount(a, b, c)
    print(count)

# Proc18
import math

def CircleS(r):
    s = math.pi * r * r
    return s

# Используем функцию для трех кругов
for i in range(3):
    r = float(input())
    area = CircleS(r)
    print(area)

# Proc19
import math

def RingS(r1, r2):
    s1 = math.pi * r1 * r1
    s2 = math.pi * r2 * r2
    return s1 - s2

# Используем функцию для трех колец
for i in range(3):
    r1 = float(input())
    r2 = float(input())
    area = RingS(r1, r2)
    print(area)

# Proc20
import math

def TriangleP(a, h):
    b = math.sqrt((a / 2) ** 2 + h ** 2)
    p = a + 2 * b
    return p

# Используем функцию для трех треугольников
for i in range(3):
    a = float(input())
    h = float(input())
    perimeter = TriangleP(a, h)
    print(perimeter)

# Proc21
def SumRange(a, b):
    if a > b:
        return 0
    total = 0
    for i in range(a, b + 1):
        total += i
    return total

# Используем функцию для двух сумм
a = int(input())
b = int(input())
c = int(input())
sum_ab = SumRange(a, b)
sum_bc = SumRange(b, c)
print(sum_ab, sum_bc)

# Proc22
def Calc(a, b, op):
    if op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        return a / b
    else: # op == 4
        return a + b

# Используем функцию для трех операций
a = float(input())
b = float(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())

result1 = Calc(a, b, n1)
result2 = Calc(a, b, n2)
result3 = Calc(a, b, n3)

print(result1, result2, result3)

# Proc23
def Quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

# Используем функцию для трех точек
for i in range(3):
    x = float(input())
    y = float(input())
    quad = Quarter(x, y)
    print(quad)

# Proc24
def Even(k):
    return k % 2 == 0

# Используем функцию для подсчета четных чисел
count_even = 0
for i in range(10):
    k = int(input())
    if Even(k):
        count_even += 1
print(count_even)

# Proc25
def IsSquare(k):
    root = int(k ** 0.5)
    return root * root == k

# Используем функцию для подсчета квадратов
count_squares = 0
for i in range(10):
    k = int(input())
    if IsSquare(k):
        count_squares += 1
print(count_squares)

# Proc26
def IsPower5(k):
    temp = 1
    while temp < k:
        temp *= 5
    return temp == k

# Используем функцию для подсчета степеней пятерки
count_powers = 0
for i in range(10):
    k = int(input())
    if IsPower5(k):
        count_powers += 1
print(count_powers)

# Proc27
def IsPowerN(k, n):
    temp = 1
    while temp < k:
        temp *= n
    return temp == k

# Используем функцию для подсчета степеней N
n = int(input())
count_powers = 0
for i in range(10):
    k = int(input())
    if IsPowerN(k, n):
        count_powers += 1
print(count_powers)

# Proc28
def IsPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Используем функцию для подсчета простых чисел
count_primes = 0
for i in range(10):
    k = int(input())
    if IsPrime(k):
        count_primes += 1
print(count_primes)

# Proc29
def DigitCount(k):
    count = 0
    temp = k
    while temp > 0:
        count += 1
        temp //= 10
    return count

# Используем функцию для подсчета цифр
for i in range(5):
    k = int(input())
    count = DigitCount(k)
    print(count)

# Proc30
def DigitN(k, n):
    count = 0
    temp = k
    while temp > 0:
        count += 1
        temp //= 10
    if count < n:
        return -1
    temp = k
    for i in range(count - n):
        temp //= 10
    return temp % 10

# Используем функцию для нахождения цифр
for i in range(5):
    k = int(input())
    for n in range(1, 6):
        digit = DigitN(k, n)
        print(digit, end=' ')
    print()

# Proc31
def IsPalindrom(k):
    original = k
    reversed_num = 0
    temp = k
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
    return original == reversed_num

# Используем функцию для подсчета палиндромов
count_palindromes = 0
for i in range(10):
    k = int(input())
    if IsPalindrom(k):
        count_palindromes += 1
print(count_palindromes)