has_ticket = True
has_id = True
is_adult = False

can_enter = has_ticket and has_id and is_adult
print(can_enter)

can_enter_v2 = has_ticket and has_id
print(can_enter_v2)
