# Передбач результат кожного рядка окремо, перш ніж запускати:

a = "25"
b = int(a) + 5 #30
c = str(b) + " років" #30 років
d = float(b) #30.0
e = b + int(True) #30 - mistake (correct answer -31)

print(b)
print(c)
print(d)
print(e)
print(type(a), type(b), type(c), type(d), type(e))
