# Вправа 1. Виведи всі числа від 1 до 100, які діляться на 7.

for i in range(1, 101):
    if i % 7 == 0:
        print(i)

# Вправа 2. Пораховуй суму чисел від 1 до 20 через while (створи total = 0, у циклі додавай кожне число до total, в кінці виведи результат).

total = 0
number = 1
while number <= 20:
    total = total + number
    number +=1
print(total)



# Вправа 3 (передбач).
for i in range(10):
    if i == 4:
        continue
    if i == 7:
        break
    print(i) # 0, 1, 2, 3, 5, 6



# Вправа 4. Створи список температур: temperatures = [15, 22, -3, 30, 0, 18, -10]. Пройдись циклом for, і для кожної температури виведи: < 0 → "Морозно" 0-15 → "Прохолодно" > 15 → "Тепло"

temperatures = [15, 22, -3, 30, 0, 18, -10]

for temperature in temperatures:
    if temperature >15:
        print("Тепло")
    elif 0 <= temperature <= 15:
        print("Прохолодно")
    else:
        print("Морозно")


# Вправа 5. Виведи таблицю множення числа 7 (від 7×1 до 7×10), у форматі 7 x 1 = 7, використовуючи for і range().
n = 7
for i in range (1, 11):
    n_mult = n * i
    print(n,"*", i, "=", n_mult)

# Вправа 6 (пастка на подумати). Порахуй, скільки разів виконається цей цикл, перш ніж запускати:
i = 0
while i < 20:
    i = i + 2
print(i) #answer 20

# Вправа 7. Створи список слів: words = ["кіт", "слон", "жираф", "миша", "кит"]. Виведи тільки ті слова, довжина яких більше 3 символів (len()).


words = ["кіт", "слон", "жираф", "миша", "кит"]
for word in words:
    length = len(word)
    if length <=3:
        continue
    print(word)

# Вправа 8 — FizzBuzz повний варіант (класика). Числа від 1 до 30:

for numb in range (1, 31):
    if numb % 3 == 0 and numb % 5 == 0:
        print("FizzBuzz") 
    elif numb % 5 == 0:
        print("Buzz")
    elif numb % 3 == 0:
        print("Fizz")
    else:
        print(numb)

# Вправа 9. Порахуй, скільки парних чисел є в діапазоні від 1 до 50 (створи лічильник count = 0, збільшуй його на 1 кожен раз, коли число парне, в кінці виведи count).

count = 0
for x in range(1, 51):
    if x % 2 ==0:
        count = count + 1
print(count)

# Вправа 10 — міні-задача. Створи attempts = 0 і password = "sunshine". Симулюй "спроби входу" — цикл while attempts < 3, кожен раз збільшуй attempts на 1 і виводь "Спроба входу №", attempts. Якщо attempts досягає 3 — вивести "Забагато спроб, доступ заблоковано".


attempts = 0
password = "sunshine"
while attempts <3:
    attempts = attempts + 1
    print("Спроба №", attempts)

print("Забагато спроб, доступ заблоковано")