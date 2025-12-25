# Minmax1
n = int(input())
first_num = float(input())
min_val = first_num
max_val = first_num
for i in range(1, n):
    num = float(input())
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
print(min_val, max_val)

# Minmax2
n = int(input())
first_a = float(input())
first_b = float(input())
min_area = first_a * first_b
for i in range(1, n):
    a = float(input())
    b = float(input())
    area = a * b
    if area < min_area:
        min_area = area
print(min_area)

# Minmax3
n = int(input())
first_a = float(input())
first_b = float(input())
max_perimeter = 2 * (first_a + first_b)
for i in range(1, n):
    a = float(input())
    b = float(input())
    perimeter = 2 * (a + b)
    if perimeter > max_perimeter:
        max_perimeter = perimeter
print(max_perimeter)

# Minmax4
n = int(input())
first_num = float(input())
min_val = first_num
min_pos = 1
for i in range(1, n):
    num = float(input())
    if num < min_val:
        min_val = num
        min_pos = i + 1
print(min_pos)

# Minmax5
n = int(input())
first_m = float(input())
first_v = float(input())
max_density = first_m / first_v
max_pos = 1
for i in range(1, n):
    m = float(input())
    v = float(input())
    density = m / v
    if density > max_density:
        max_density = density
        max_pos = i + 1
print(max_pos, max_density)

# Minmax7
n = int(input())
first_num = int(input())
max_val = first_num
min_val = first_num
first_max_pos = 1
last_min_pos = 1
for i in range(1, n):
    num = int(input())
    if num > max_val:
        max_val = num
        first_max_pos = i + 1
    if num <= min_val:
        min_val = num
        last_min_pos = i + 1
print(first_max_pos, last_min_pos)

# Minmax8
n = int(input())
first_num = int(input())
min_val = first_num
first_min_pos = 1
last_min_pos = 1
for i in range(1, n):
    num = int(input())
    if num < min_val:
        min_val = num
        first_min_pos = i + 1
        last_min_pos = i + 1
    elif num == min_val:
        last_min_pos = i + 1
print(first_min_pos, last_min_pos)

# Minmax9
n = int(input())
first_num = int(input())
max_val = first_num
first_max_pos = 1
last_max_pos = 1
for i in range(1, n):
    num = int(input())
    if num > max_val:
        max_val = num
        first_max_pos = i + 1
        last_max_pos = i + 1
    elif num == max_val:
        last_max_pos = i + 1
print(first_max_pos, last_max_pos)

# Minmax10
n = int(input())
first_num = int(input())
min_val = first_num
max_val = first_num
min_pos = 1
max_pos = 1
for i in range(1, n):
    num = int(input())
    if num < min_val:
        min_val = num
        min_pos = i + 1
    elif num > max_val:
        max_val = num
        max_pos = i + 1
extreme_pos = min(min_pos, max_pos)
print(extreme_pos)

# Minmax11
n = int(input())
first_num = int(input())
min_val = first_num
max_val = first_num
last_min_pos = 1
last_max_pos = 1
for i in range(1, n):
    num = int(input())
    if num < min_val:
        min_val = num
        last_min_pos = i + 1
    elif num > max_val:
        max_val = num
        last_max_pos = i + 1
extreme_pos = max(last_min_pos, last_max_pos)
print(extreme_pos)

# Minmax12
n = int(input())
min_positive = None
for i in range(n):
    num = float(input())
    if num > 0:
        if min_positive is None or num < min_positive:
            min_positive = num
if min_positive is not None:
    print(min_positive)
else:
    print(0)

# Minmax13
n = int(input())
first_odd = None
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        if first_odd is None:
            first_odd = (num, i + 1)
        elif num > first_odd[0]:
            first_odd = (num, i + 1)
if first_odd is not None:
    print(first_odd[1])
else:
    print(0)

# Minmax14
b = float(input())
min_val = None
min_pos = 0
for i in range(10):
    num = float(input())
    if num > b:
        if min_val is None or num < min_val:
            min_val = num
            min_pos = i + 1
if min_val is not None:
    print(min_val, min_pos)
else:
    print(0, 0)

# Minmax15
b = float(input())
c = float(input())
max_val = None
max_pos = 0
for i in range(10):
    num = float(input())
    if b < num < c:
        if max_val is None or num > max_val:
            max_val = num
            max_pos = i + 1
if max_val is not None:
    print(max_val, max_pos)
else:
    print(0, 0)

# Minmax16
n = int(input())
first_num = int(input())
min_val = first_num
min_pos = 1
for i in range(1, n):
    num = int(input())
    if num < min_val:
        min_val = num
        min_pos = i + 1
print(min_pos - 1)

# Minmax17
n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
max_val = max(nums)
last_max_pos = -1
for i in range(n):
    if nums[i] == max_val:
        last_max_pos = i
print(n - last_max_pos - 1)

# Minmax19
n = int(input())
first_num = int(input())
min_val = first_num
count = 1
for i in range(1, n):
    num = int(input())
    if num < min_val:
        min_val = num
        count = 1
    elif num == min_val:
        count += 1
print(count)

# Minmax20
n = int(input())
first_num = int(input())
min_val = first_num
max_val = first_num
count = 1
for i in range(1, n):
    num = int(input())
    if num < min_val:
        min_val = num
        count = 1
    elif num > max_val:
        max_val = num
        count = 1
    elif num == min_val or num == max_val:
        count += 1
print(count)

# Minmax21
n = int(input())
first_num = float(input())
min_val = first_num
max_val = first_num
total = first_num
for i in range(1, n):
    num = float(input())
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num
    total += num
avg = (total - min_val - max_val) / (n - 2)
print(avg)

# Minmax22
n = int(input())
first_num = float(input())
second_num = float(input())
if first_num < second_num:
    min1, min2 = first_num, second_num
else:
    min1, min2 = second_num, first_num
for i in range(2, n):
    num = float(input())
    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2:
        min2 = num
print(min1, min2)

# Minmax23
n = int(input())
first_num = float(input())
second_num = float(input())
third_num = float(input())
# Сортируем первые три
if first_num < second_num:
    first_num, second_num = second_num, first_num
if second_num < third_num:
    second_num, third_num = third_num, second_num
if first_num < second_num:
    first_num, second_num = second_num, first_num
max1, max2, max3 = first_num, second_num, third_num
for i in range(3, n):
    num = float(input())
    if num > max1:
        max3 = max2
        max2 = max1
        max1 = num
    elif num > max2:
        max3 = max2
        max2 = num
    elif num > max3:
        max3 = num
print(max1, max2, max3)

# Minmax24
n = int(input())
first_num = float(input())
second_num = float(input())
max_sum = first_num + second_num
prev = second_num
for i in range(2, n):
    num = float(input())
    current_sum = prev + num
    if current_sum > max_sum:
        max_sum = current_sum
    prev = num
print(max_sum)

# Minmax25
n = int(input())
first_num = float(input())
second_num = float(input())
min_product = first_num * second_num
min_pos1 = 1
min_pos2 = 2
prev = second_num
for i in range(2, n):
    num = float(input())
    current_product = prev * num
    if current_product < min_product:
        min_product = current_product
        min_pos1 = i
        min_pos2 = i + 1
    prev = num
print(min_pos1, min_pos2)