# Вправа 1

age = 25
if age >= 18:
    print("Можна голосувати")
else:
    print("Зарано голосувати")

# Вправа 2
number = 7

if number % 2 == 0:
    print("Парне")
else:
    print("Непарне") #Непарне

# Вправа 3

age = 20

if age >= 18:
    print("Дорослий")

# Вправа 4

weather = "мряка"
if weather == "сонячно":
    print("Візьми окуляри")

elif weather == "дощ":
    print ("Візьми парасольку")

elif weather == "сніг":
    print("Одягни шапку")

else:
    print("Перевір прогноз ще раз")

# Вправа A. Створи password = "12345". Якщо password == "12345" — вивести "Доступ дозволено", інакше — "Невірний пароль".

password = "12345"
if password == "12345":
    print("Доступ дозволено")
else:
    print("Неправильний пароль")

# Вправа B. Створи number. Перевір, чи воно позитивне, негативне чи нуль (три варіанти через if/elif/else).

number = 2
if number > 0:
    print("Число позитивне")
elif number < 0:
    print("Числе негативне")
else:
    print("Нуль")

# Вправа C. 

hour = 12
if hour < 12:
    print("Доброго ранку")
elif 12 <= hour < 18:
    print("Добрий день")
else:
    print("Добрий вечір")

# Вправа D. Створи x = 10 і y = 20. Виведи, яке число більше, використовуючи if/elif/else (врахуй випадок, коли вони рівні).

x = 10
y = 20

if x > y:
    print("Число", x, "> за число", y)
elif x < y:
    print("Число", x, "< за число", y)
else:
    print(x, "=", y)

# Вправа E (передбач).

a = 5
b = 10
c = 15

if a > b or c > b:
    print("Умова істинна")
else:
    print("Умова хибна") # answer - умова істинна

    

