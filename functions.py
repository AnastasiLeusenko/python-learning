""" # Вправа 1 

def greet_user(name):
    print(f"Привіт, {name}!")

greet_user ("Anna")
greet_user ("Sofa")

# Вправа 2 (передбач перед запуском).

def add_numbers(a, b):
    return a + b


result = add_numbers(5, 3)
print(result) #8
print(result + 10) #18

# Вправа 3 — різниця print vs return (важлива пастка).
def multiply(a, b):
    print(a * b) #20


result = multiply(4, 5)
print(result) #none """

# Вправа 4. Напиши функцію calculate_bmi(weight, height) (той самий BMI-калькулятор з домашки, але тепер як функція з return, а не окремі рядки коду). Виклич її з двома різними наборами даних.