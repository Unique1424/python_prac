# Series26
k = int(input())
n = int(input())
for i in range(n):
    a = float(input())
    result = a ** k
    print(result)

# Series27
n = int(input())
for i in range(n):
    a = float(input())
    if i == 0:
        result = a
    else:
        result = a ** (i + 1)
    print(result)

# Series28
n = int(input())
for i in range(n):
    a = float(input())
    if i == 0:
        result = a ** n
    elif i == n - 1:
        result = a
    else:
        result = a ** (n - i)
    print(result)

# Series29
k = int(input())
n = int(input())
total_sum = 0.0
for set_num in range(k):
    for elem_num in range(n):
        num = int(input())
        total_sum += num
print(total_sum)

# Series30
k = int(input())
n = int(input())
for set_num in range(k):
    set_sum = 0
    for elem_num in range(n):
        num = int(input())
        set_sum += num
    print(set_sum)

# Series31
k = int(input())
n = int(input())
count_sets_with_2 = 0
for set_num in range(k):
    has_two = False
    for elem_num in range(n):
        num = int(input())
        if num == 2:
            has_two = True
    if has_two:
        count_sets_with_2 += 1
print(count_sets_with_2)

# Series32
k = int(input())
n = int(input())
for set_num in range(k):
    first_two_pos = 0
    for elem_num in range(n):
        num = int(input())
        if num == 2 and first_two_pos == 0:
            first_two_pos = elem_num + 1
    if first_two_pos != 0:
        print(first_two_pos)
    else:
        print(0)

# Series33
k = int(input())
n = int(input())
for set_num in range(k):
    last_two_pos = 0
    for elem_num in range(n):
        num = int(input())
        if num == 2:
            last_two_pos = elem_num + 1
    if last_two_pos != 0:
        print(last_two_pos)
    else:
        print(0)

# Series34
k = int(input())
n = int(input())
for set_num in range(k):
    has_two = False
    set_sum = 0
    for elem_num in range(n):
        num = int(input())
        set_sum += num
        if num == 2:
            has_two = True
    if has_two:
        print(set_sum)
    else:
        print(0)

# Series35
k = int(input())
total_count = 0
for set_num in range(k):
    count = 0
    while True:
        num = int(input())
        if num == 0:
            break
        count += 1
    print(count)
    total_count += count
print(total_count)

# Series36
k = int(input())
count_increasing = 0
for set_num in range(k):
    prev = None
    is_increasing = True
    while True:
        num = int(input())
        if num == 0:
            break
        if prev is not None and num <= prev:
            is_increasing = False
        prev = num
    if is_increasing:
        count_increasing += 1
print(count_increasing)

# Series37
k = int(input())
count_inc_or_dec = 0
for set_num in range(k):
    nums = []
    while True:
        num = int(input())
        if num == 0:
            break
        nums.append(num)
    if len(nums) >= 2:
        is_increasing = True
        is_decreasing = True
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                is_increasing = False
            if nums[i] >= nums[i - 1]:
                is_decreasing = False
        if is_increasing or is_decreasing:
            count_inc_or_dec += 1
print(count_inc_or_dec)

# Series38
k = int(input())
for set_num in range(k):
    nums = []
    while True:
        num = int(input())
        if num == 0:
            break
        nums.append(num)
    if len(nums) >= 2:
        is_increasing = True
        is_decreasing = True
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                is_increasing = False
            if nums[i] >= nums[i - 1]:
                is_decreasing = False
        if is_increasing:
            print(1)
        elif is_decreasing:
            print(-1)
        else:
            print(0)
    else:
        print(0)

# Series39
k = int(input())
count_sawtooth = 0
for set_num in range(k):
    nums = []
    while True:
        num = int(input())
        if num == 0:
            break
        nums.append(num)
    if len(nums) >= 3:
        is_sawtooth = True
        for i in range(1, len(nums) - 1):
            left = nums[i - 1]
            current = nums[i]
            right = nums[i + 1]
            if not ((current > left and current > right) or (current < left and current < right)):
                is_sawtooth = False
                break
        if is_sawtooth:
            count_sawtooth += 1
print(count_sawtooth)

# Series40
k = int(input())
for set_num in range(k):
    nums = []
    while True:
        num = int(input())
        if num == 0:
            break
        nums.append(num)
    if len(nums) >= 3:
        is_sawtooth = True
        for i in range(1, len(nums) - 1):
            left = nums[i - 1]
            current = nums[i]
            right = nums[i + 1]
            if not ((current > left and current > right) or (current < left and current < right)):
                is_sawtooth = False
                break
        if is_sawtooth:
            print(len(nums))
        else:
            print(1)
    else:
        print(1)