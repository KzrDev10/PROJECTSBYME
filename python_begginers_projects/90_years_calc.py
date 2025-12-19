#90 Days, Weeks, Months Left Calculator

#we assume everypone lives till 90

#collect age inpiut
age = int(input("Whats your age: "))

#defining limit 
days_to_live = 90*365
months_to_live = 90*12
weeks_to_live = 90*52

#calc lived time
days_lived = age *365
weeks_lived = age *52
months_lived = age *12

#output
time_left =f"You have {days_to_live - days_lived} days, {weeks_to_live - weeks_lived} weeks and {months_to_live - months_lived} months"
print(time_left)