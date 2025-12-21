height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight/height**2,2)
answer = f'Your BMI is {bmi}'

if bmi < 18.5:
    print(f'{answer}, you are underweight')
elif bmi > 18.5 and bmi < 25:
    print(f'{answer}, you have normal weight')
elif bmi > 25 and bmi < 30:
    print(f'{answer}, you are overweight')
elif bmi > 30 and bmi < 35:
    print(f'{answer}, you are obese')
elif bmi > 35:
    print(f'{answer}, you are clinically obese')
else:
    print(f'{answer}, Bro how are you alive')