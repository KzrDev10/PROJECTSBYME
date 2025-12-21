 #if divisible by 4 its leap year
#if divisible by 100 not leap year but if divisible by 400 it is


try:
    # collects year from user
    c_year = int(input("Enter a year: "))
    #conditions remember python stops at first true condition so order matters
    if c_year % 400 == 0:
            print("This a leap year")
    elif c_year % 100 == 0:
            print("Not leap year")
    elif c_year % 4 == 0:
            print("This leap year")
    else:
            print("Not leap year")
# if user inputs string or other invalid input            
except ValueError:
    print("Put number")