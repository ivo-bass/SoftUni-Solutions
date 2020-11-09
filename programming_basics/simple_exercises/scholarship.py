income = float(input())
gpa = float(input())
min_salary = float(input())

social_scholarship = 0.35 * min_salary
gpa_scholarship = gpa * 25
scholarship = 0

if income < min_salary and gpa > 4.5:
    scholarship = social_scholarship

if gpa >= 5.5 and gpa_scholarship >= scholarship:
    scholarship = gpa_scholarship

if scholarship == social_scholarship:
    print(f"You get a Social scholarship {int(scholarship)} BGN")
elif scholarship == gpa_scholarship:
    print(f"You get a scholarship for excellent results {int(scholarship)} BGN")
else:
    print("You cannot get a scholarship!")