# Вправа 7
city1 = "Дніпро"
city2 = "Львів"

temp = city1
city1 = city2
city2 = temp

print(city1)  # має вивести: Львів
print(city2)  # має вивести: Дніпро

# Вправа 8
score1 = 15
score2 = 42

temp = score1
score1 = score2
score2 = temp

print(score1)  # має вивести: 42
print(score2)  # має вивести: 15

# Вправа 11
a = "перший"
b = "другий"
c = "третій"
temp = b
b = a
a = c
c = temp

print(a)  # має вивести: третій
print(b)  # має вивести: перший
print(c)  # має вивести: другий
