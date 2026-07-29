"""def say_hi(name):
    print(f"Привіт, {name}!")


say_hi("Анастасія")
say_hi("Іван")"""

"""def introduce(name, age):
    print(f"Мене звати {name}, мені {age} років")


introduce("Анастасія", 25)
introduce("Наталія", 5)"""

"""def add_numbers(a, b):
   return a + b
result = add_numbers(5, 3)

print(result)"""

"""def greet(name, greeting="Привіт"):
    print(f"{greeting}, {name}!")


greet("Анастасія")
greet("Іван", "Доброго ранку")
greet("Євгеній")
greet("Катерина")
greet("Світлана", "Добрий вечір")"""

"""def describe_pet(name, animal_type="кіт"):
    print(f"{name} - це {animal_type}!")

describe_pet("Василіса", "кішка")
describe_pet("Тошик")
describe_pet("Рудий")
describe_pet("Аріша", "собака")
describe_pet("Стьопа", "хомяк")"""

def check_age(age):
    if age < 18:
        return "Неповнолітній"
    else:
        return "Дорослий"


result = check_age(15)
print(result)