# Array90
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
for i in range(k, n):
    a[i - 1] = a[i]
new_size = n - 1
for i in range(new_size):
    print(a[i])

# Array91
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
l = int(input())
for i in range(l, n):
    a[i - (l - k + 1)] = a[i]
new_size = n - (l - k + 1)
print(new_size)
for i in range(new_size):
    print(a[i])

# Array92
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(n):
    if a[i] % 2 == 0:
        a[new_size] = a[i]
        new_size += 1
print(new_size)
for i in range(new_size):
    print(a[i])

# Array93
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(1, n, 2):
    a[new_size] = a[i]
    new_size += 1
print(new_size)
for i in range(new_size):
    print(a[i])

# Array94
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(0, n, 2):
    a[new_size] = a[i]
    new_size += 1
print(new_size)
for i in range(new_size):
    print(a[i])

# Array95
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(n):
    if new_size == 0 or a[i] != a[new_size - 1]:
        a[new_size] = a[i]
        new_size += 1
print(new_size)
for i in range(new_size):
    print(a[i])

# Array96
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(n):
    is_duplicate = False
    for j in range(new_size):
        if a[j] == a[i]:
            is_duplicate = True
            break
    if not is_duplicate:
        a[new_size] = a[i]
        new_size += 1
print(new_size)
for i in range(new_size):
    print(a[i])

# Array97
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(n):
    is_duplicate = False
    for j in range(i + 1, n):
        if a[j] == a[i]:
            is_duplicate = True
            break
    if not is_duplicate:
        a[new_size] = a[i]
        new_size += 1
print(new_size)
for i in range(new_size):
    print(a[i])

# Array98
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
count = [0] * 1000001
for i in range(n):
    count[a[i]] += 1
new_size = 0
for i in range(n):
    if count[a[i]] >= 3:
        a[new_size] = a[i]
        new_size += 1
print(new_size)
for i in range(new_size):
    print(a[i])

# Array99
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
count = [0] * 1000001
for i in range(n):
    count[a[i]] += 1
new_size = 0
for i in range(n):
    if count[a[i]] <= 2:
        a[new_size] = a[i]
        new_size += 1
print(new_size)
for i in range(new_size):
    print(a[i])

# Array100
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
count = [0] * 1000001
for i in range(n):
    count[a[i]] += 1
new_size = 0
for i in range(n):
    if count[a[i]] != 2:
        a[new_size] = a[i]
        new_size += 1
print(new_size)
for i in range(new_size):
    print(a[i])

# Array101
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
for i in range(n, k - 1, -1):
    a[i] = a[i - 1]
a[k - 1] = 0
new_size = n + 1
for i in range(new_size):
    print(a[i])

# Array102
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
for i in range(n, k, -1):
    a[i] = a[i - 1]
a[k] = 0
new_size = n + 1
for i in range(new_size):
    print(a[i])

# Array103
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
min_val = a[0]
max_val = a[0]
min_pos = 0
max_pos = 0
for i in range(n):
    if a[i] < min_val:
        min_val = a[i]
        min_pos = i
    if a[i] > max_val:
        max_val = a[i]
        max_pos = i
# Вставка перед мин
for i in range(n, min_pos, -1):
    a[i] = a[i - 1]
a[min_pos] = 0
n += 1
# Вставка после макс (номер макс может измениться, если он после мин)
if max_pos >= min_pos:
    max_pos += 1
for i in range(n, max_pos + 1, -1):
    a[i] = a[i - 1]
a[max_pos + 1] = 0
new_size = n + 1
for i in range(new_size):
    print(a[i])

# Array104
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
m = int(input())
for i in range(n + m - 1, k - 1, -1):
    a[i] = a[i - m]
for i in range(k - 1, k - 1 + m):
    a[i] = 0
new_size = n + m
for i in range(new_size):
    print(a[i])

# Array105
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
m = int(input())
for i in range(n + m - 1, k, -1):
    a[i] = a[i - m]
for i in range(k, k + m):
    a[i] = 0
new_size = n + m
for i in range(new_size):
    print(a[i])

# Array106
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(n):
    a[new_size] = a[i]
    new_size += 1
    if i % 2 != 0:  # четный номер (индекс нечетный)
        a[new_size] = a[i]
        new_size += 1
for i in range(new_size):
    print(a[i])

# Array107
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(n):
    a[new_size] = a[i]
    new_size += 1
    if i % 2 == 0:  # нечетный номер (индекс четный)
        a[new_size] = a[i]
        new_size += 1
        a[new_size] = a[i]
        new_size += 1
for i in range(new_size):
    print(a[i])

# Array108
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(n):
    if a[i] > 0:
        a[new_size] = 0
        new_size += 1
    a[new_size] = a[i]
    new_size += 1
for i in range(new_size):
    print(a[i])

# Array109
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(n):
    a[new_size] = a[i]
    new_size += 1
    if a[i] < 0:
        a[new_size] = 0
        new_size += 1
for i in range(new_size):
    print(a[i])

# Array110
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(n):
    a[new_size] = a[i]
    new_size += 1
    if a[i] % 2 == 0:
        a[new_size] = a[i]
        new_size += 1
for i in range(new_size):
    print(a[i])

# Array111
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_size = 0
for i in range(n):
    a[new_size] = a[i]
    new_size += 1
    if a[i] % 2 != 0:
        a[new_size] = a[i]
        new_size += 1
        a[new_size] = a[i]
        new_size += 1
for i in range(new_size):
    print(a[i])