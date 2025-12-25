# While1
a = int(input())
b = int(input())
while a >= b:
    a -= b
print(a)

# While2
a = int(input())
b = int(input())
count = 0
while a >= b:
    a -= b
    count += 1
print(count)

# While3
n = int(input())
k = int(input())
quotient = 0
remainder = n
while remainder >= k:
    remainder -= k
    quotient += 1
print(quotient, remainder)

# While4
n = int(input())
temp = 1
while temp < n:
    temp *= 3
print(temp == n)

# While5
n = int(input())
temp = 1
k = 0
while temp < n:
    temp *= 2
    k += 1
print(k)

# While6
n = int(input())
product = 1.0
temp = n
while temp > 1:
    product *= temp
    temp -= 2
print(product)

# While7
n = int(input())
k = 1
while k * k <= n:
    k += 1
print(k)

# While8
n = int(input())
k = 1
while (k + 1) * (k + 1) <= n:
    k += 1
print(k)

# While9
n = int(input())
k = 0
temp = 1
while temp <= n:
    temp *= 3
    k += 1
print(k)

# While10
n = int(input())
k = 0
temp = 1
while temp * 3 < n:
    temp *= 3
    k += 1
print(k)

# While11
n = int(input())
k = 1
sum_val = 1
while sum_val < n:
    k += 1
    sum_val += k
print(k, sum_val)

# While12
n = int(input())
k = 1
sum_val = 1
while sum_val + (k + 1) <= n:
    k += 1
    sum_val += k
print(k, sum_val)

# While13
a = float(input())
k = 1
sum_val = 1.0
while sum_val <= a:
    k += 1
    sum_val += 1.0 / k
print(k, sum_val)

# While14
a = float(input())
k = 1
sum_val = 1.0
while sum_val + 1.0 / (k + 1) < a:
    k += 1
    sum_val += 1.0 / k
print(k, sum_val)

# While15
p = float(input())
amount = 1000.0
months = 0
while amount <= 1100.0:
    months += 1
    amount *= (1 + p / 100)
print(months, amount)

# While16
p = float(input())
day_distance = 10.0
total_distance = 0.0
days = 0
while total_distance <= 200.0:
    days += 1
    total_distance += day_distance
    day_distance *= (1 + p / 100)
print(days, total_distance)

# While17
n = int(input())
while n > 0:
    digit = n % 10
    print(digit)
    n //= 10

# While18
n = int(input())
count = 0
sum_digits = 0
while n > 0:
    digit = n % 10
    count += 1
    sum_digits += digit
    n //= 10
print(count, sum_digits)

# While19
n = int(input())
reversed_num = 0
while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10
print(reversed_num)

# While20
n = int(input())
has_two = False
while n > 0:
    digit = n % 10
    if digit == 2:
        has_two = True
        break
    n //= 10
print(has_two)

# While21
n = int(input())
has_odd = False
while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        has_odd = True
        break
    n //= 10
print(has_odd)

# While22
n = int(input())
is_prime = True
if n == 1:
    is_prime = False
else:
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            is_prime = False
            break
        divisor += 1
print(is_prime)

# While23
a = int(input())
b = int(input())
while b != 0:
    temp = b
    b = a % b
    a = temp
print(a)