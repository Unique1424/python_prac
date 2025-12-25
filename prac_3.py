# If1
a = int(input())
if a > 0:
    a += 1
print(a)

# If2
a = int(input())
if a > 0:
    a += 1
else:
    a -= 2
print(a)

# If3
a = int(input())
if a > 0:
    a += 1
elif a < 0:
    a -= 2
else:
    a = 10
print(a)

# If4
a = int(input())
b = int(input())
c = int(input())
count = 0
if a > 0:
    count += 1
if b > 0:
    count += 1
if c > 0:
    count += 1
print(count)

# If5
a = int(input())
b = int(input())
c = int(input())
pos_count = 0
neg_count = 0
if a > 0:
    pos_count += 1
elif a < 0:
    neg_count += 1
if b > 0:
    pos_count += 1
elif b < 0:
    neg_count += 1
if c > 0:
    pos_count += 1
elif c < 0:
    neg_count += 1
print(pos_count, neg_count)

# If6
a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)

# If7
a = int(input())
b = int(input())
if a < b:
    print(1)
else:
    print(2)

# If8
a = int(input())
b = int(input())
if a > b:
    print(a, b)
else:
    print(b, a)

# If9
a = float(input())
b = float(input())
if a > b:
    a, b = b, a
print(a, b)

# If10
a = int(input())
b = int(input())
if a != b:
    s = a + b
    a = s
    b = s
else:
    a = 0
    b = 0
print(a, b)

# If11
a = int(input())
b = int(input())
if a != b:
    m = max(a, b)
    a = m
    b = m
else:
    a = 0
    b = 0
print(a, b)

# If12
a = int(input())
b = int(input())
c = int(input())
min_val = a
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
print(min_val)

# If13
a = int(input())
b = int(input())
c = int(input())
if a <= b <= c or c <= b <= a:
    print(b)
elif b <= a <= c or c <= a <= b:
    print(a)
else:
    print(c)

# If14
a = int(input())
b = int(input())
c = int(input())
min_val = a
max_val = a
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c
print(min_val, max_val)

# If15
a = int(input())
b = int(input())
c = int(input())
if a <= b <= c:
    sum_max = b + c
elif a <= c <= b:
    sum_max = c + b
elif b <= a <= c:
    sum_max = a + c
elif b <= c <= a:
    sum_max = c + a
elif c <= a <= b:
    sum_max = a + b
else: # c <= b <= a
    sum_max = b + a
print(sum_max)

# If16
a = float(input())
b = float(input())
c = float(input())
if a < b < c:
    a *= 2
    b *= 2
    c *= 2
else:
    a = -a
    b = -b
    c = -c
print(a, b, c)

# If17
a = float(input())
b = float(input())
c = float(input())
if (a < b < c) or (a > b > c):
    a *= 2
    b *= 2
    c *= 2
else:
    a = -a
    b = -b
    c = -c
print(a, b, c)

# If18
a = int(input())
b = int(input())
c = int(input())
if a == b:
    print(3)
elif a == c:
    print(2)
else:
    print(1)

# If19
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == b == c:
    print(4)
elif a == b == d:
    print(3)
elif a == c == d:
    print(2)
else:
    print(1)

# If20
a = int(input())
b = int(input())
c = int(input())
dist_b = abs(a - b)
dist_c = abs(a - c)
if dist_b <= dist_c:
    print(b, dist_b)
else:
    print(c, dist_c)

# If21
x = int(input())
y = int(input())
if x == 0 and y == 0:
    print(0)
elif y == 0:
    print(1)
elif x == 0:
    print(2)
else:
    print(3)

# If22
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)

# If23
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1
if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1
print(x4, y4)

# If24
x = float(input())
if x > 0:
    import math
    f = 2 * math.sin(x)
else:
    f = 6 - x
print(f)

# If25
n = int(input())
if n % 2 == 0:
    parity = "четное"
else:
    parity = "нечетное"
if n < 10:
    digits = "однозначное"
elif n < 100:
    digits = "двузначное"
else:
    digits = "трехзначное"
print(f"{parity} {digits} число")