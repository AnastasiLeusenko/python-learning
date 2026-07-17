weight_kg = 65.0
height_m = 1.70
bmi = weight_kg / (height_m * height_m)
print(round(bmi, 1))
bmi_is_normal = bmi < 25
print(type(bmi_is_normal))