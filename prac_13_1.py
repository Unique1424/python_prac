# Array18
a = []
for i in range(10):
    a.append(int(input()))
last_val = a[9]
found = False
for i in range(9):
    if a[i] < last_val:
        print(a[i])
        found = True
        break
if not found:
    print(0)

# Array19
a = []
for i in range(10):
    a.append(int(input()))
first_val = a[0]
last_val = a[9]
pos = 0
for i in range(1, 9):
    if first_val < a[i] < last_val:
        pos = i + 1
if pos != 0:
    print(pos)
else:
    print(0)

# Array20
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
l = int(input())
total = 0
for i in range(k - 1, l):
    total += a[i]
print(total)

# Array21
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
l = int(input())
total = 0
count = l - k + 1
for i in range(k - 1, l):
    total += a[i]
avg = total / count
print(avg)

# Array22
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
l = int(input())
total = 0
for i in range(n):
    if not (k - 1 <= i <= l - 1):
        total += a[i]
print(total)

# Array23
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
l = int(input())
total = 0
count = 0
for i in range(n):
    if not (k - 1 <= i <= l - 1):
        total += a[i]
        count += 1
if count > 0:
    avg = total / count
    print(avg)
else:
    print(0)

# Array24
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
if n < 2:
    print(0)
else:
    diff = a[1] - a[0]
    is_arithmetic = True
    for i in range(2, n):
        if a[i] - a[i - 1] != diff:
            is_arithmetic = False
            break
    if is_arithmetic:
        print(diff)
    else:
        print(0)

# Array25
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
if n < 2 or a[0] == 0:
    print(0)
else:
    ratio = a[1] / a[0]
    is_geometric = True
    for i in range(2, n):
        if a[i - 1] == 0 or a[i] / a[i - 1] != ratio:
            is_geometric = False
            break
    if is_geometric:
        print(ratio)
    else:
        print(0)

# Array26
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
if n < 2:
    print(0)
else:
    is_alternating = True
    for i in range(1, n):
        if (a[i] % 2) == (a[i - 1] % 2):
            is_alternating = False
            print(i + 1)
            break
    if is_alternating:
        print(0)

# Array27
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
if n < 2:
    print(0)
else:
    is_alternating = True
    for i in range(1, n):
        if (a[i] > 0) == (a[i - 1] > 0):
            is_alternating = False
            print(i + 1)
            break
    if is_alternating:
        print(0)

# Array28
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
min_val = None
for i in range(1, n, 2):
    if min_val is None or a[i] < min_val:
        min_val = a[i]
print(min_val)

# Array29
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max_val = None
for i in range(0, n, 2):
    if max_val is None or a[i] > max_val:
        max_val = a[i]
print(max_val)

# Array30
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
indices = []
for i in range(n - 1):
    if a[i] > a[i + 1]:
        indices.append(i + 1)
print(len(indices))
for idx in indices:
    print(idx, end=' ')
print()

# Array31
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
indices = []
for i in range(1, n):
    if a[i] > a[i - 1]:
        indices.append(i + 1)
print(len(indices))
for idx in reversed(indices):
    print(idx, end=' ')
print()

# Array32
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
pos = 0
if n == 1:
    pos = 1
else:
    for i in range(n):
        is_local_min = True
        if i > 0 and a[i] >= a[i - 1]:
            is_local_min = False
        if i < n - 1 and a[i] >= a[i + 1]:
            is_local_min = False
        if is_local_min:
            pos = i + 1
            break
print(pos)

# Array33
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
pos = 0
if n == 1:
    pos = 1
else:
    for i in range(n):
        is_local_max = True
        if i > 0 and a[i] <= a[i - 1]:
            is_local_max = False
        if i < n - 1 and a[i] <= a[i + 1]:
            is_local_max = False
        if is_local_max:
            pos = i + 1
print(pos)

# Array34
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
min_local = None
if n == 1:
    min_local = a[0]
else:
    for i in range(n):
        is_local_min = True
        if i > 0 and a[i] >= a[i - 1]:
            is_local_min = False
        if i < n - 1 and a[i] >= a[i + 1]:
            is_local_min = False
        if is_local_min:
            if min_local is None or a[i] < min_local:
                min_local = a[i]
if min_local is not None:
    print(min_local)
else:
    print(0)

# Array35
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max_local = None
if n == 1:
    max_local = a[0]
else:
    for i in range(n):
        is_local_max = True
        if i > 0 and a[i] <= a[i - 1]:
            is_local_max = False
        if i < n - 1 and a[i] <= a[i + 1]:
            is_local_max = False
        if is_local_max:
            if max_local is None or a[i] > max_local:
                max_local = a[i]
if max_local is not None:
    print(max_local)
else:
    print(0)

# Array36
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
max_non_extreme = None
if n == 1:
    max_non_extreme = a[0]
else:
    for i in range(n):
        is_local_min = True
        is_local_max = True
        if i > 0 and a[i] >= a[i - 1]:
            is_local_min = False
        if i < n - 1 and a[i] >= a[i + 1]:
            is_local_min = False
        if i > 0 and a[i] <= a[i - 1]:
            is_local_max = False
        if i < n - 1 and a[i] <= a[i + 1]:
            is_local_max = False
        is_extreme = is_local_min or is_local_max
        if not is_extreme:
            if max_non_extreme is None or a[i] > max_non_extreme:
                max_non_extreme = a[i]
if max_non_extreme is not None:
    print(max_non_extreme)
else:
    print(0)