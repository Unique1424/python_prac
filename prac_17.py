# String13
s = input()
count = 0
for c in s:
    if '0' <= c <= '9':
        count += 1
print(count)

# String14
s = input()
count = 0
for c in s:
    if 'A' <= c <= 'Z':
        count += 1
print(count)

# String15
s = input()
count = 0
for c in s:
    if 'a' <= c <= 'z' or 'а' <= c <= 'я':
        count += 1
print(count)

# String16
s = input()
result = ""
for c in s:
    if 'A' <= c <= 'Z':
        result += chr(ord(c) + 32)
    else:
        result += c
print(result)

# String17
s = input()
result = ""
for c in s:
    if 'a' <= c <= 'z' or 'а' <= c <= 'я':
        result += chr(ord(c) - 32)
    else:
        result += c
print(result)

# String18
s = input()
result = ""
for c in s:
    if 'A' <= c <= 'Z':
        result += chr(ord(c) + 32)
    elif 'a' <= c <= 'z':
        result += chr(ord(c) - 32)
    elif 'А' <= c <= 'Я':
        result += chr(ord(c) + 32)
    elif 'а' <= c <= 'я':
        result += chr(ord(c) - 32)
    else:
        result += c
print(result)

# String19
s = input()
try:
    float_val = float(s)
    if '.' in s:
        print(2)
    else:
        print(1)
except ValueError:
    print(0)

# String20
n = int(input())
s = str(n)
for c in s:
    print(c)

# String21
n = int(input())
s = str(n)
for i in range(len(s) - 1, -1, -1):
    print(s[i])

# String22
s = input()
total = 0
for c in s:
    if '0' <= c <= '9':
        total += int(c)
print(total)

# String23
s = input()
result = 0
current_num = 0
sign = 1
for i in range(len(s)):
    c = s[i]
    if '0' <= c <= '9':
        current_num = current_num * 10 + int(c)
    else: # c is '+' or '-'
        result += sign * current_num
        current_num = 0
        if c == '+':
            sign = 1
        else: # c == '-'
            sign = -1
result += sign * current_num
print(result)

# String24
s = input()
result = 0
for c in s:
    result = result * 2 + int(c)
print(result)

# String25
n = int(input())
if n == 0:
    print('0')
else:
    binary_str = ""
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n //= 2
    print(binary_str)