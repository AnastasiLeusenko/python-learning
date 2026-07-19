# Вправа 1 — числа від 1 до 10 через for + range()
for number in range (1,11):
    print(number)


# Вправа 2 — вже передбачила, тепер запусти й підтверди
for i in range(3, 8):
    print(i)

# Вправа 3 — while, зворотній відлік від 10 до 1
count = 10

while count > 0:
    print(count)
    count = count - 1

# Вправа 4 — навмисний нескінченний цикл, зупини через Ctrl + C
temp_count = 1
while temp_count <= 5:
    print(temp_count)