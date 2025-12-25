# Array112
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    for k in range(n):
        print(a[k], end=' ')
    print()

# Array113
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(n - 1):
    max_val = a[0]
    max_pos = 0
    for j in range(n - i):
        if a[j] > max_val:
            max_val = a[j]
            max_pos = j
    a[max_pos], a[n - 1 - i] = a[n - 1 - i], a[max_pos]
    for k in range(n):
        print(a[k], end=' ')
    print()

# Array114
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

for i in range(1, n):
    temp = a[i]
    j = i
    while j > 0 and a[j - 1] > temp:
        a[j] = a[j - 1]
        j -= 1
    a[j] = temp
    for k in range(n):
        print(a[k], end=' ')
    print()

# Array115
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

i_arr = []
for i in range(n + 1):
    i_arr.append(0)
for i in range(1, n + 1):
    i_arr[i] = i

for round_num in range(n - 1):
    for j in range(1, n - round_num):
        if a[i_arr[j] - 1] > a[i_arr[j + 1] - 1]:
            i_arr[j], i_arr[j + 1] = i_arr[j + 1], i_arr[j]

for i in range(1, n + 1):
    print(i_arr[i], end=' ')
print()