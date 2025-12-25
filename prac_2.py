# Boolean1
a = int(input())
b = a > 0
print(b)

# Boolean2
a = int(input())
b = a % 2 != 0
print(b)

# Boolean3
a = int(input())
b = a % 2 == 0
print(b)

# Boolean4
a = int(input())
b = int(input())
c = a > 2 and b <= 3
print(c)

# Boolean5
a = int(input())
b = int(input())
c = a >= 0 or b < -2
print(c)

# Boolean6
a = int(input())
b = int(input())
c = int(input())
d = a < b < c
print(d)

# Boolean7
a = int(input())
b = int(input())
c = int(input())
d = (a < b < c) or (c < b < a)
print(d)

# Boolean8
a = int(input())
b = int(input())
c = (a % 2 != 0) and (b % 2 != 0)
print(c)

# Boolean9
a = int(input())
b = int(input())
c = (a % 2 != 0) or (b % 2 != 0)
print(c)

# Boolean10
a = int(input())
b = int(input())
c = (a % 2 != 0) != (b % 2 != 0)
print(c)

# Boolean11
a = int(input())
b = int(input())
c = (a % 2 == 0) == (b % 2 == 0)
print(c)

# Boolean12
a = int(input())
b = int(input())
c = int(input())
d = a > 0 and b > 0 and c > 0
print(d)

# Boolean13
a = int(input())
b = int(input())
c = int(input())
d = a > 0 or b > 0 or c > 0
print(d)

# Boolean14
a = int(input())
b = int(input())
c = int(input())
d = (a > 0 and b <= 0 and c <= 0) or (a <= 0 and b > 0 and c <= 0) or (a <= 0 and b <= 0 and c > 0)
print(d)

# Boolean15
a = int(input())
b = int(input())
c = int(input())
d = (a > 0 and b > 0 and c <= 0) or (a > 0 and b <= 0 and c > 0) or (a <= 0 and b > 0 and c > 0)
print(d)

# Boolean16
a = int(input())
b = a % 2 == 0 and 10 <= a <= 99
print(b)

# Boolean17
a = int(input())
b = a % 2 != 0 and 100 <= a <= 999
print(b)

# Boolean18
a = int(input())
b = int(input())
c = int(input())
d = (a == b) or (b == c) or (a == c)
print(d)

# Boolean19
a = int(input())
b = int(input())
c = int(input())
d = (a == -b) or (b == -c) or (a == -c)
print(d)

# Boolean20
a = int(input())
b = a // 100
c = (a // 10) % 10
d = a % 10
e = b != c and b != d and c != d
print(e)