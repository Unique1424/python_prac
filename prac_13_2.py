# Array65
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
val_k = a[k - 1]
for i in range(n):
    a[i] += val_k
for i in range(n):
    print(a[i])

# Array66
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
first_even = None
for i in range(n):
    if a[i] % 2 == 0:
        first_even = a[i]
        break
if first_even is not None:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] += first_even
for i in range(n):
    print(a[i])

# Array67
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
last_odd = None
for i in range(n):
    if a[i] % 2 != 0:
        last_odd = a[i]
if last_odd is not None:
    for i in range(n):
        if a[i] % 2 != 0:
            a[i] += last_odd
for i in range(n):
    print(a[i])

# Array68
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
a[min_pos], a[max_pos] = a[max_pos], a[min_pos]
for i in range(n):
    print(a[i])

# Array69
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(0, n, 2):
    if i + 1 < n:
        a[i], a[i + 1] = a[i + 1], a[i]
for i in range(n):
    print(a[i])

# Array70
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
mid = n // 2
for i in range(mid):
    a[i], a[i + mid] = a[i + mid], a[i]
for i in range(n):
    print(a[i])

# Array71
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n // 2):
    a[i], a[n - 1 - i] = a[n - 1 - i], a[i]
for i in range(n):
    print(a[i])

# Array72
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
l = int(input())
start = k - 1
end = l - 1
while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1
for i in range(n):
    print(a[i])

# Array73
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
l = int(input())
start = k
end = l - 2
while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1
for i in range(n):
    print(a[i])

# Array74
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
start = min(min_pos, max_pos) + 1
end = max(min_pos, max_pos)
for i in range(start, end):
    a[i] = 0
for i in range(n):
    print(a[i])

# Array75
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
start = min(min_pos, max_pos)
end = max(min_pos, max_pos)
while start < end:
    a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1
for i in range(n):
    print(a[i])

# Array76
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
to_zero = set()
if n == 1:
    pass
else:
    for i in range(n):
        is_local_max = True
        if i > 0 and a[i] <= a[i - 1]:
            is_local_max = False
        if i < n - 1 and a[i] <= a[i + 1]:
            is_local_max = False
        if is_local_max:
            to_zero.add(i)
for i in range(n):
    if i in to_zero:
        a[i] = 0
for i in range(n):
    print(a[i])

# Array77
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
to_square = set()
if n == 1:
    pass
else:
    for i in range(n):
        is_local_min = True
        if i > 0 and a[i] >= a[i - 1]:
            is_local_min = False
        if i < n - 1 and a[i] >= a[i + 1]:
            is_local_min = False
        if is_local_min:
            to_square.add(i)
for i in range(n):
    if i in to_square:
        a[i] = a[i] * a[i]
for i in range(n):
    print(a[i])

# Array78
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
new_a = []
for i in range(n):
    total = a[i]
    count = 1
    if i > 0:
        total += a[i - 1]
        count += 1
    if i < n - 1:
        total += a[i + 1]
        count += 1
    avg = total / count
    new_a.append(avg)
for i in range(n):
    print(new_a[i])

# Array79
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n - 1, 0, -1):
    a[i] = a[i - 1]
a[0] = 0
for i in range(n):
    print(a[i])

# Array80
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
for i in range(n - 1):
    a[i] = a[i + 1]
a[n - 1] = 0
for i in range(n):
    print(a[i])