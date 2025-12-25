# String26
n = int(input())
s = input()
if len(s) > n:
    result = s[len(s) - n:]
elif len(s) < n:
    result = '.' * (n - len(s)) + s
else:
    result = s
print(result)

# String27
n1 = int(input())
n2 = int(input())
s1 = input()
s2 = input()
part1 = s1[:n1]
part2 = s2[len(s2) - n2:]
result = part1 + part2
print(result)

# String28
c = input()
s = input()
result = ""
for char in s:
    if char == c:
        result += c + c
    else:
        result += char
print(result)

# String29
c = input()
s = input()
s0 = input()
result = ""
for char in s:
    if char == c:
        result += s0 + char
    else:
        result += char
print(result)

# String30
c = input()
s = input()
s0 = input()
result = ""
for char in s:
    result += char
    if char == c:
        result += s0
print(result)

# String31
s = input()
s0 = input()
if s0 in s:
    print(True)
else:
    print(False)

# String32
s = input()
s0 = input()
count = 0
pos = 0
while pos <= len(s) - len(s0):
    if s[pos:pos + len(s0)] == s0:
        count += 1
        pos += len(s0)
    else:
        pos += 1
print(count)

# String33
s = input()
s0 = input()
pos = s.find(s0)
if pos != -1:
    result = s[:pos] + s[pos + len(s0):]
else:
    result = s
print(result)

# String34
s = input()
s0 = input()
pos = s.rfind(s0)
if pos != -1:
    result = s[:pos] + s[pos + len(s0):]
else:
    result = s
print(result)

# String35
s = input()
s0 = input()
result = s.replace(s0, '')
print(result)

# String36
s = input()
s1 = input()
s2 = input()
pos = s.find(s1)
if pos != -1:
    result = s[:pos] + s2 + s[pos + len(s1):]
else:
    result = s
print(result)

# String37
s = input()
s1 = input()
s2 = input()
pos = s.rfind(s1)
if pos != -1:
    result = s[:pos] + s2 + s[pos + len(s1):]
else:
    result = s
print(result)

# String38
s = input()
s1 = input()
s2 = input()
result = s.replace(s1, s2)
print(result)

# String39
s = input()
first_space = s.find(' ')
second_space = s.find(' ', first_space + 1)
if first_space != -1 and second_space != -1:
    result = s[first_space + 1:second_space]
else:
    result = ""
print(result)

# String40
s = input()
first_space = s.find(' ')
last_space = s.rfind(' ')
if first_space != -1 and last_space != -1 and first_space != last_space:
    result = s[first_space + 1:last_space]
else:
    result = ""
print(result)