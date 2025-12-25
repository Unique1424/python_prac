# String41
s = input()
words = s.split()
print(len(words))

# String42
s = input()
words = s.split()
count = 0
for word in words:
    if word[0] == word[-1]:
        count += 1
print(count)

# String43
s = input()
words = s.split()
count = 0
for word in words:
    if 'А' in word:
        count += 1
print(count)

# String44
s = input()
words = s.split()
count = 0
for word in words:
    if word.count('А') == 3:
        count += 1
print(count)

# String45
s = input()
words = s.split()
min_len = len(words[0])
for word in words:
    if len(word) < min_len:
        min_len = len(word)
print(min_len)

# String46
s = input()
words = s.split()
max_len = len(words[0])
for word in words:
    if len(word) > max_len:
        max_len = len(word)
print(max_len)

# String47
s = input()
words = s.split()
result = '.'.join(words)
print(result)

# String48
s = input()
words = s.split()
result = []
for word in words:
    first_char = word[0]
    new_word = first_char
    for i in range(1, len(word)):
        if word[i] == first_char:
            new_word += '.'
        else:
            new_word += word[i]
    result.append(new_word)
print(' '.join(result))

# String49
s = input()
words = s.split()
result = []
for word in words:
    last_char = word[-1]
    new_word = ''
    for i in range(len(word) - 1):
        if word[i] == last_char:
            new_word += '.'
        else:
            new_word += word[i]
    new_word += last_char
    result.append(new_word)
print(' '.join(result))

# String50
s = input()
words = s.split()
reversed_words = words[::-1]
result = ' '.join(reversed_words)
print(result)

# String51
s = input()
words = s.split()
words.sort()
result = ' '.join(words)
print(result)

# String52
s = input()
result = ""
word_start = True
for c in s:
    if c.isalpha():
        if word_start:
            result += c.upper()
            word_start = False
        else:
            result += c.lower()
    else:
        result += c
        if c == ' ':
            word_start = True
print(result)

# String53
s = input()
punctuation = ".,;:!?-"
count = 0
for c in s:
    if c in punctuation:
        count += 1
print(count)

# String54
s = input()
vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
count = 0
for c in s:
    if c in vowels:
        count += 1
print(count)

# String55
s = input()
punctuation = " .,;:!?-"
current_word = ""
longest_word = ""
for c in s:
    if c not in punctuation:
        current_word += c
    else:
        if len(current_word) > len(longest_word):
            longest_word = current_word
        current_word = ""
if len(current_word) > len(longest_word):
    longest_word = current_word
print(longest_word)

# String56
s = input()
punctuation = " .,;:!?-"
current_word = ""
shortest_word = None
for c in s:
    if c not in punctuation:
        current_word += c
    else:
        if current_word:
            if shortest_word is None or len(current_word) < len(shortest_word):
                shortest_word = current_word
            elif len(current_word) == len(shortest_word):
                shortest_word = current_word  # последнее из одинаковых
        current_word = ""
if current_word:
    if shortest_word is None or len(current_word) < len(shortest_word):
        shortest_word = current_word
    elif len(current_word) == len(shortest_word):
        shortest_word = current_word
print(shortest_word)

# String57
s = input()
words = s.split()
result = ' '.join(words)
print(result)