# Case1
day_num = int(input())
if day_num == 1:
    print("понедельник")
elif day_num == 2:
    print("вторник")
elif day_num == 3:
    print("среда")
elif day_num == 4:
    print("четверг")
elif day_num == 5:
    print("пятница")
elif day_num == 6:
    print("суббота")
elif day_num == 7:
    print("воскресенье")

# Case2
k = int(input())
if k == 1:
    print("плохо")
elif k == 2:
    print("неудовлетворительно")
elif k == 3:
    print("удовлетворительно")
elif k == 4:
    print("хорошо")
elif k == 5:
    print("отлично")
else:
    print("ошибка")

# Case3
month = int(input())
if month in [12, 1, 2]:
    print("зима")
elif month in [3, 4, 5]:
    print("весна")
elif month in [6, 7, 8]:
    print("лето")
else:
    print("осень")

# Case4
month = int(input())
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month in [4, 6, 9, 11]:
    print(30)
else:
    print(28)

# Case5
n = int(input())
a = float(input())
b = float(input())
if n == 1:
    result = a + b
elif n == 2:
    result = a - b
elif n == 3:
    result = a * b
elif n == 4:
    result = a / b
print(result)

# Case6
unit = int(input())
length = float(input())
if unit == 1:
    meters = length / 10
elif unit == 2:
    meters = length * 1000
elif unit == 3:
    meters = length
elif unit == 4:
    meters = length / 1000
elif unit == 5:
    meters = length / 100
print(meters)

# Case7
unit = int(input())
mass = float(input())
if unit == 1:
    kg = mass
elif unit == 2:
    kg = mass / 1000000
elif unit == 3:
    kg = mass / 1000
elif unit == 4:
    kg = mass * 1000
elif unit == 5:
    kg = mass * 100
print(kg)

# Case8
d = int(input())
m = int(input())
if d == 1:
    if m == 1:
        d = 31
        m = 12
    elif m in [5, 7, 10, 12]:
        d = 30
        m -= 1
    elif m in [2, 4, 6, 8, 9, 11]:
        d = 31
        m -= 1
    else: # m == 3
        d = 28
        m = 2
else:
    d -= 1
print(d, m)

# Case9
d = int(input())
m = int(input())
if m in [1, 3, 5, 7, 8, 10] and d == 31:
    d = 1
    m += 1
elif m in [4, 6, 9, 11] and d == 30:
    d = 1
    m += 1
elif m == 2 and d == 28:
    d = 1
    m = 3
elif m == 12 and d == 31:
    d = 1
    m = 1
else:
    d += 1
print(d, m)

# Case10
c = input()
n = int(input())
directions = ['С', 'З', 'Ю', 'В']
current_index = directions.index(c)
if n == 1:
    new_index = (current_index + 1) % 4
elif n == -1:
    new_index = (current_index - 1) % 4
else:
    new_index = current_index
print(directions[new_index])

# Case11
c = input()
n1 = int(input())
n2 = int(input())
directions = ['С', 'З', 'Ю', 'В']
current_index = directions.index(c)
for cmd in [n1, n2]:
    if cmd == 1:
        current_index = (current_index + 1) % 4
    elif cmd == -1:
        current_index = (current_index - 1) % 4
    elif cmd == 2:
        current_index = (current_index + 2) % 4
print(directions[current_index])

# Case12
element = int(input())
value = float(input())
pi = 3.14
if element == 1:
    r = value
    d = 2 * r
    l = 2 * pi * r
    s = pi * r * r
elif element == 2:
    d = value
    r = d / 2
    l = 2 * pi * r
    s = pi * r * r
elif element == 3:
    l = value
    r = l / (2 * pi)
    d = 2 * r
    s = pi * r * r
else: # element == 4
    s = value
    r = (s / pi) ** 0.5
    d = 2 * r
    l = 2 * pi * r
print(r, d, l, s)

# Case13
element = int(input())
value = float(input())
if element == 1:
    a = value
    c = a * (2 ** 0.5)
    h = c / 2
    s = c * h / 2
elif element == 2:
    c = value
    a = c / (2 ** 0.5)
    h = c / 2
    s = c * h / 2
elif element == 3:
    h = value
    c = 2 * h
    a = c / (2 ** 0.5)
    s = c * h / 2
else: # element == 4
    s = value
    c = (2 * s) ** 0.5
    h = c / 2
    a = c / (2 ** 0.5)
print(a, c, h, s)

# Case14
element = int(input())
value = float(input())
if element == 1:
    a = value
    r1 = a * (3 ** 0.5) / 6
    r2 = 2 * r1
    s = a * a * (3 ** 0.5) / 4
elif element == 2:
    r1 = value
    a = r1 * 6 / (3 ** 0.5)
    r2 = 2 * r1
    s = a * a * (3 ** 0.5) / 4
elif element == 3:
    r2 = value
    r1 = r2 / 2
    a = r1 * 6 / (3 ** 0.5)
    s = a * a * (3 ** 0.5) / 4
else: # element == 4
    s = value
    a = (4 * s / (3 ** 0.5)) ** 0.5
    r1 = a * (3 ** 0.5) / 6
    r2 = 2 * r1
print(a, r1, r2, s)

# Case15
n = int(input())
m = int(input())
ranks = {6: "шестерка", 7: "семерка", 8: "восьмерка", 9: "девятка", 10: "десятка", 11: "валет", 12: "дама", 13: "король", 14: "туз"}
suits = {1: "пик", 2: "треф", 3: "бубен", 4: "червей"}
print(f"{ranks[n]} {suits[m]}")

# Case16
age = int(input())
decades = {2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят", 6: "шестьдесят"}
units = {0: "", 1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}
dec = age // 10
unit = age % 10
age_str = decades[dec]
if unit != 0:
    age_str += " " + units[unit]

if unit in [1]:
    year_word = "год"
elif unit in [2, 3, 4]:
    year_word = "года"
else:
    year_word = "лет"
print(f"{age_str} {year_word}")

# Case17
n = int(input())
units = {1: "одно", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять", 10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать", 20: "двадцать", 30: "тридцать", 40: "сорок"}
if n <= 20:
    num_str = units[n]
else:
    tens = n // 10 * 10
    unit = n % 10
    num_str = units[tens]
    if unit != 0:
        num_str += " " + units[unit]

if n % 10 == 1 and n != 11:
    task_word = "учебное задание"
elif n % 10 in [2, 3, 4] and n not in [12, 13, 14]:
    task_word = "учебных задания"
else:
    task_word = "учебных заданий"
print(f"{num_str} {task_word}")

# Case18
n = int(input())
hundreds = n // 100
tens_units = n % 100
units = n % 10

hundred_words = {1: "сто", 2: "двести", 3: "триста", 4: "четыреста", 5: "пятьсот", 6: "шестьсот", 7: "семьсот", 8: "восемьсот", 9: "девятьсот"}
teen_words = {10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}
decade_words = {2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят", 6: "шестьдесят", 7: "семьдесят", 8: "восемьдесят", 9: "девяносто"}
unit_words = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}

result = hundred_words[hundreds]

if 10 <= tens_units <= 19:
    result += " " + teen_words[tens_units]
elif tens_units == 0:
    pass
else:
    result += " " + decade_words[tens_units // 10]
    if units != 0:
        result += " " + unit_words[units]

print(result)

# Case19
year = int(input())
offset = year - 1984
cycle_index = offset % 60
color_index = (cycle_index // 12) % 5
animal_index = cycle_index % 12

colors = ["зеленый", "красный", "желтый", "белый", "черный"]
animals = ["крысы", "коровы", "тигра", "зайца", "дракона", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]

color = colors[color_index]
animal = animals[animal_index]
print(f"год {color} {animal}")

# Case20
d = int(input())
m = int(input())

if (m == 1 and d >= 20) or (m == 2 and d <= 18):
    sign = "Водолей"
elif (m == 2 and d >= 19) or (m == 3 and d <= 20):
    sign = "Рыбы"
elif (m == 3 and d >= 21) or (m == 4 and d <= 19):
    sign = "Овен"
elif (m == 4 and d >= 20) or (m == 5 and d <= 20):
    sign = "Телец"
elif (m == 5 and d >= 21) or (m == 6 and d <= 21):
    sign = "Близнецы"
elif (m == 6 and d >= 22) or (m == 7 and d <= 22):
    sign = "Рак"
elif (m == 7 and d >= 23) or (m == 8 and d <= 22):
    sign = "Лев"
elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
    sign = "Дева"
elif (m == 9 and d >= 23) or (m == 10 and d <= 22):
    sign = "Весы"
elif (m == 10 and d >= 23) or (m == 11 and d <= 22):
    sign = "Скорпион"
elif (m == 11 and d >= 23) or (m == 12 and d <= 21):
    sign = "Стрелец"
else:
    sign = "Козерог"
print(sign)