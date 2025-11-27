weight = int(input('Weight: '))
unit = input('L(lbs) or K(kg): ')
if unit.upper() == "L":
    c = weight*0.45
    print(f'You are {c} kilos')
else:
    c = weight/0.45
    print(f'You are {c} pounds')

def add(x,y):
    x = x-y
    return x
print(add(6,4))