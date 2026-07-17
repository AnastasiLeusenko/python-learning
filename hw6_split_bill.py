total_bill = 1240.0
tip_percent = 10
number_of_people = 4
tip_amount = total_bill * tip_percent / 100
total_with_tip = total_bill + tip_amount
per_person = total_with_tip / 4

print(round(per_person, 2))
