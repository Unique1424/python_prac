# For36
n = int(input())
k = int(input())
total = 0.0
for i in range(1, n + 1):
    total += i ** k
print(total)

# For37
n = int(input())
total = 0.0
for i in range(1, n + 1):
    total += i ** i
print(total)

# For38
n = int(input())
total = 0.0
for i in range(1, n + 1):
    total += i ** (n - i + 1)
print(total)

# For39
a = int(input())
b = int(input())
for i in range(a, b + 1):
    for j in range(i):
        print(i)

# For40
a = int(input())
b = int(input())
for i in range(a, b + 1):
    times = i - a + 1
    for j in range(times):
        print(i)