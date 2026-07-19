# Вправа 5 (передбач).

for i in range(1, 10):
    if i == 6:
        break
    print(i) # 1, 2, 3, 4, 5

# Вправа 6 (передбач).

for i in range(1, 8):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7 

# Вправа 7. Виведи всі числа від 1 до 50, які діляться на 3 (використай if + % всередині for).

for number in range (1, 51):
    if number % 3 == 0:
        print(number)

# Вправа 8 — комбінація. Виведи числа від 1 до 30, але: якщо число ділиться на 3 і на 5 одночасно — вивести "Fizz Buzz" інакше просто вивести число


for n in range (1, 31):
    if n % 3 == 0 and n % 5 == 0:
        print("Fizz Buzz")
    else:
        print(n)
