# String1
c = input()
print(ord(c))

# String2
n = int(input())
print(chr(n))

# String3
c = input()
prev_char = chr(ord(c) - 1)
next_char = chr(ord(c) + 1)
print(prev_char, next_char)

# String4
n = int(input())
for i in range(n):
    print(chr(ord('A') + i), end='')
print()

# String5
n = int(input())
for i in range(n):
    print(chr(ord('z') - i), end='')
print()

# String6
c = input()
if '0' <= c <= '9':
    print("digit")
elif 'A' <= c <= 'Z' or 'a' <= c <= 'z':
    print("lat")
else:
    print("rus")

# String7
s = input()
print(ord(s[0]), ord(s[-1]))

# String8
n = int(input())
c = input()
print(c * n)

# String9
n = int(input())
c1 = input()
c2 = input()
result = ""
for i in range(n):
    if i % 2 == 0:
        result += c1
    else:
        result += c2
print(result)

# String10
s = input()
print(s[::-1])

# String11
s = input()
result = ""
for i in range(len(s)):
    result += s[i]
    if i < len(s) - 1:
        result += " "
print(result)

# String12
s = input()
n = int(input())
result = ""
for i in range(len(s)):
    result += s[i]
    if i < len(s) - 1:
        result += "*" * n
print(result)