price = 800
discount_percent = 25

discount_amount = price * discount_percent / 100
print(str("Знижка:"), discount_amount)
total = price - discount_amount
print(str("До сплати:"), total)