issue_type = "технічна"  # варіанти: "оплата", "технічна", "інше"
is_urgent = True  # терміново чи ні
customer_tier = "standart"  # варіанти: "premium", "standard"

if issue_type == "оплата" and is_urgent:
    print("Пріоритет: КРИТИЧНИЙ — передати негайно")
elif customer_tier == "premium":
    print("Пріоритет: ВИСОКИЙ — відповісти протягом години")

elif issue_type == "технічна":
    print("Пріоритет: СЕРЕДНІЙ — відповісти сьогодні")
else:
    print("Пріоритет: НИЗЬКИЙ — відповісти протягом 3 днів")
