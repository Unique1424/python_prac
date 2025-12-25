# Series1
total = 0.0
for i in range(10):
    num = float(input())
    total += num
print(total)

# Series2
product = 1.0
for i in range(10):
    num = float(input())
    product *= num
print(product)

# Series3
total = 0.0
for i in range(10):
    num = float(input())
    total += num
avg = total / 10
print(avg)

# Series4
n = int(input())
total = 0.0
product = 1.0
for i in range(n):
    num = float(input())
    total += num
    product *= num
print(total, product)

# Series5
n = int(input())
total = 0.0
for i in range(n):
    num = float(input())
    int_part = int(num)
    print(int_part)
    total += int_part
print(total)

# Series6
n = int(input())
product = 1.0
for i in range(n):
    num = float(input())
    frac_part = num - int(num)
    print(frac_part)
    product *= frac_part
print(product)

# Series7
n = int(input())
total = 0
for i in range(n):
    num = float(input())
    rounded = round(num)
    print(rounded)
    total += rounded
print(total)

# Series8
n = int(input())
count = 0
for i in range(n):
    num = int(input())
    if num % 2 == 0:
        print(num)
        count += 1
print(count)

# Series9
n = int(input())
count = 0
for i in range(n):
    num = int(input())
    if num % 2 != 0:
        print(i + 1)
        count += 1
print(count)

# Series10
n = int(input())
has_positive = False
for i in range(n):
    num = int(input())
    if num > 0:
        has_positive = True
print(has_positive)

# Series11
k = int(input())
n = int(input())
has_less = False
for i in range(n):
    num = int(input())
    if num < k:
        has_less = True
print(has_less)

# Series12
count = 0
while True:
    num = int(input())
    if num == 0:
        break
    count += 1
print(count)

# Series13
total = 0
while True:
    num = int(input())
    if num == 0:
        break
    if num > 0 and num % 2 == 0:
        total += num
print(total)

# Series14
k = int(input())
count = 0
while True:
    num = int(input())
    if num == 0:
        break
    if num < k:
        count += 1
print(count)

# Series15
k = int(input())
pos = 0
current_pos = 1
while True:
    num = int(input())
    if num == 0:
        break
    if num > k and pos == 0:
        pos = current_pos
    current_pos += 1
print(pos)

# Series16
k = int(input())
pos = 0
current_pos = 1
while True:
    num = int(input())
    if num == 0:
        break
    if num > k:
        pos = current_pos
    current_pos += 1
print(pos)

# Series17
b = float(input())
n = int(input())
inserted = False
for i in range(n):
    num = float(input())
    if not inserted and b <= num:
        print(b)
        inserted = True
    print(num)
if not inserted:
    print(b)

# Series18
n = int(input())
prev = None
for i in range(n):
    num = int(input())
    if prev is None or num != prev:
        print(num)
        prev = num

# Series19
n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
count = 0
for i in range(1, n):
    if nums[i] < nums[i - 1]:
        print(nums[i])
        count += 1
print(count)

# Series20
n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
count = 0
for i in range(n - 1):
    if nums[i] < nums[i + 1]:
        print(nums[i])
        count += 1
print(count)

# Series21
n = int(input())
nums = []
for i in range(n):
    num = float(input())
    nums.append(num)
is_increasing = True
for i in range(1, n):
    if nums[i] <= nums[i - 1]:
        is_increasing = False
        break
print(is_increasing)

# Series22
n = int(input())
nums = []
for i in range(n):
    num = float(input())
    nums.append(num)
is_decreasing = True
violation_pos = 0
for i in range(1, n):
    if nums[i] >= nums[i - 1]:
        is_decreasing = False
        violation_pos = i + 1
        break
if is_decreasing:
    print(0)
else:
    print(violation_pos)

# Series23
n = int(input())
nums = []
for i in range(n):
    num = float(input())
    nums.append(num)
is_sawtooth = True
violation_pos = 0
for i in range(1, n - 1):
    left = nums[i - 1]
    current = nums[i]
    right = nums[i + 1]
    if not ((current > left and current > right) or (current < left and current < right)):
        is_sawtooth = False
        violation_pos = i + 1
        break
if is_sawtooth:
    print(0)
else:
    print(violation_pos)

# Series24
n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
last_zero = -1
prev_last_zero = -1
for i in range(n - 1, -1, -1):
    if nums[i] == 0:
        if last_zero == -1:
            last_zero = i
        elif prev_last_zero == -1:
            prev_last_zero = i
            break
if prev_last_zero != -1 and last_zero != -1:
    total = 0
    for i in range(prev_last_zero + 1, last_zero):
        total += nums[i]
    print(total)
else:
    print(0)

# Series25
n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
first_zero = -1
last_zero = -1
for i in range(n):
    if nums[i] == 0:
        if first_zero == -1:
            first_zero = i
        last_zero = i
if first_zero != -1 and last_zero != -1 and first_zero < last_zero:
    total = 0
    for i in range(first_zero + 1, last_zero):
        total += nums[i]
    print(total)
else:
    print(0)