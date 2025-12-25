# For1
k = int(input())
n = int(input())
for i in range(n):
    print(k)

# For2
a = int(input())
b = int(input())
count = 0
for i in range(a, b + 1):
    print(i)
    count += 1
print(count)

# For3
a = int(input())
b = int(input())
count = 0
for i in range(b - 1, a, -1):
    print(i)
    count += 1
print(count)

# For4
price = float(input())
for i in range(1, 11):
    cost = price * i
    print(cost)

# For5
price = float(input())
for i in range(1, 11):
    weight = i * 0.1
    cost = price * weight
    print(cost)

# For6
price = float(input())
for i in range(6, 11):
    weight = 1.0 + i * 0.2
    cost = price * weight
    print(cost)

# For7
a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
    total += i
print(total)

# For8
a = int(input())
b = int(input())
product = 1
for i in range(a, b + 1):
    product *= i
print(product)

# For9
a = int(input())
b = int(input())
total = 0
for i in range(a, b + 1):
    total += i * i
print(total)

# For10
n = int(input())
total = 0
for i in range(1, n + 1):
    total += 1 / i
print(total)

# For11
n = int(input())
total = 0
for i in range(n, 2 * n + 1):
    total += i * i
print(total)

# For12
n = int(input())
product = 1
for i in range(1, n + 1):
    product *= 1.0 + i * 0.1
print(product)

# For13
n = int(input())
total = 0
sign = 1
for i in range(1, n + 1):
    term = 1.0 + i * 0.1
    total += sign * term
    sign = -sign
print(total)

# For14
n = int(input())
total = 0
for i in range(1, n + 1):
    odd = 2 * i - 1
    total += odd
    print(f"{i}^2 = {total}")

# For15
a = float(input())
n = int(input())
result = 1
for i in range(n):
    result *= a
print(result)

# For16
a = float(input())
n = int(input())
power = 1
for i in range(1, n + 1):
    power *= a
    print(power)

# For17
a = float(input())
n = int(input())
total = 1
power = 1
for i in range(1, n + 1):
    power *= a
    total += power
print(total)

# For18
a = float(input())
n = int(input())
total = 1
power = 1
sign = -1
for i in range(1, n + 1):
    power *= a
    total += sign * power
    sign = -sign
print(total)

# For19
n = int(input())
factorial = 1.0
for i in range(1, n + 1):
    factorial *= i
print(factorial)

# For20
n = int(input())
total = 0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += factorial
print(total)

# For21
n = int(input())
total = 1.0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    total += 1.0 / factorial
print(total)

# For22
x = float(input())
n = int(input())
total = 1.0
term = 1.0
factorial = 1
for i in range(1, n + 1):
    factorial *= i
    term = x ** i / factorial
    total += term
print(total)

# For23
x = float(input())
n = int(input())
total = x
term = x
factorial = 1
for i in range(1, n + 1):
    factorial *= (2 * i) * (2 * i + 1)
    term = (-1) ** i * (x ** (2 * i + 1)) / factorial
    total += term
print(total)

# For24
x = float(input())
n = int(input())
total = 1.0
term = 1.0
factorial = 1
for i in range(1, n + 1):
    factorial *= (2 * i) * (2 * i - 1)
    term = (-1) ** i * (x ** (2 * i)) / factorial
    total += term
print(total)

# For25
x = float(input())
n = int(input())
total = x
term = x
for i in range(2, n + 1):
    term = (-1) ** (i - 1) * (x ** i) / i
    total += term
print(total)