#if number is divisible by 3 print "fizz"
#if number is divisible by 5 print "buzz"
#if number is divisible by both 3 and 5 print "fizzbuzz"

#collect input
#check if fiz , buzz or fizzbuzz




try:
    while(True):
        num = int(input("Whats your number(0 to exit):  "))
        if num % 3 == 0:
            print("fizz")
        if num % 5 == 0:
            print("buzz")
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        else:
            break
except ValueError:
    print("Put a num bro")
