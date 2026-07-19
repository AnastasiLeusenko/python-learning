passwords = ["12345", "qwerty123", "MyStr0ng!Pass", "abc", "password1"]
for password in passwords:
    print(password)
    length = len(password)
    if length < 6:
        print("СЛАБКИЙ: занадто короткий")
    elif password == "12345" or password == "password1":
        print("СЛАБКИЙ: занадто популярний")
    else:
        print("OK: прийнятний пароль")



