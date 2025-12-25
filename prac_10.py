# Proc1
def PowerA3(a):
    b = a ** 3
    return b

# Используем процедуру для пяти чисел
for i in range(5):
    num = float(input())
    result = PowerA3(num)
    print(result)

# Proc2
def PowerA234(a, b, c, d):
    b = a ** 2
    c = a ** 3
    d = a ** 4
    return b, c, d

# Используем процедуру для пяти чисел
for i in range(5):
    num = float(input())
    b, c, d = PowerA234(num, 0, 0, 0)
    print(b, c, d)

# Proc3
def Mean(x, y, amean, gmean):
    amean = (x + y) / 2
    gmean = (x * y) ** 0.5
    return amean, gmean

# Используем процедуру для трех пар
for i in range(3):
    x = float(input())
    y = float(input())
    amean, gmean = Mean(x, y, 0, 0)
    print(amean, gmean)

# Proc4
import math

def TrianglePS(a, p, s):
    p = 3 * a
    s = (a ** 2) * math.sqrt(3) / 4
    return p, s

# Используем процедуру для трех треугольников
for i in range(3):
    a = float(input())
    p, s = TrianglePS(a, 0, 0)
    print(p, s)

# Proc5
def RectPS(x1, y1, x2, y2, p, s):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    p = 2 * (width + height)
    s = width * height
    return p, s

# Используем процедуру для трех прямоугольников
for i in range(3):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    p, s = RectPS(x1, y1, x2, y2, 0, 0)
    print(p, s)

# Proc6
def DigitCountSum(k, c, s):
    c = 0
    s = 0
    temp = k
    while temp > 0:
        digit = temp % 10
        c += 1
        s += digit
        temp //= 10
    return c, s

# Используем процедуру для пяти чисел
for i in range(5):
    k = int(input())
    c, s = DigitCountSum(k, 0, 0)
    print(c, s)

# Proc7
def InvertDigits(k):
    reversed_num = 0
    temp = k
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
    return reversed_num

# Используем процедуру для пяти чисел
for i in range(5):
    k = int(input())
    result = InvertDigits(k)
    print(result)

# Proc8
def AddRightDigit(d, k):
    result = k * 10 + d
    return result

# Используем процедуру для двух добавлений
k = int(input())
d1 = int(input())
d2 = int(input())
result1 = AddRightDigit(d1, k)
print(result1)
result2 = AddRightDigit(d2, result1)
print(result2)

# Proc9
def AddLeftDigit(d, k):
    temp = k
    digits = 0
    while temp > 0:
        digits += 1
        temp //= 10
    result = d * (10 ** digits) + k
    return result

# Используем процедуру для двух добавлений
k = int(input())
d1 = int(input())
d2 = int(input())
result1 = AddLeftDigit(d1, k)
print(result1)
result2 = AddLeftDigit(d2, result1)
print(result2)

# Proc10
def Swap(x, y):
    return y, x

# Используем процедуру для обмена пар
a = float(input())
b = float(input())
c = float(input())
d = float(input())

a, b = Swap(a, b)
c, d = Swap(c, d)
b, c = Swap(b, c)

print(a, b, c, d)

# Proc11
def Minmax(x, y):
    if x < y:
        return x, y
    else:
        return y, x

# Используем процедуру для нахождения мин и макс
a = float(input())
b = float(input())
c = float(input())
d = float(input())

min_val, max_val = Minmax(a, b)
min_val, max_val = Minmax(min_val, c)
min_val, max_val = Minmax(min_val, d)

print(min_val, max_val)

# Proc12
def SortInc3(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

# Используем процедуру для упорядочивания
a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())

a1, b1, c1 = SortInc3(a1, b1, c1)
a2, b2, c2 = SortInc3(a2, b2, c2)

print(a1, b1, c1)
print(a2, b2, c2)

# Proc13
def SortDec3(a, b, c):
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    return a, b, c

# Используем процедуру для упорядочивания
a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())

a1, b1, c1 = SortDec3(a1, b1, c1)
a2, b2, c2 = SortDec3(a2, b2, c2)

print(a1, b1, c1)
print(a2, b2, c2)

# Proc14
def ShiftRight3(a, b, c):
    temp = a
    a = c
    c = b
    b = temp
    return a, b, c

# Используем процедуру для циклического сдвига
a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())

a1, b1, c1 = ShiftRight3(a1, b1, c1)
a2, b2, c2 = ShiftRight3(a2, b2, c2)

print(a1, b1, c1)
print(a2, b2, c2)

# Proc15
def ShiftLeft3(a, b, c):
    temp = a
    a = b
    b = c
    c = temp
    return a, b, c

# Используем процедуру для циклического сдвига
a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())

a1, b1, c1 = ShiftLeft3(a1, b1, c1)
a2, b2, c2 = ShiftLeft3(a2, b2, c2)

print(a1, b1, c1)
print(a2, b2, c2)