import random
print("Welcome to Password Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','#','$','%','&','(',')',',','*','+','-']

num_of_letters = int(input("How many letters do you want in the password: "))

num_of_numbers = int(input("How many numbers do you want in the password: "))

num_of_symbols = int(input("How many symbols do you want in the password: "))

password_list = []

# +1 so they include the last number

for letter in range(1,num_of_letters + 1):
    password_l = random.choice(letters)
    password_list += password_l

for num in range(1,num_of_numbers + 1):
    password_n = random.choice(numbers)
    password_list += password_n

for symbol in range(1,num_of_symbols+1):
    password_s = random.choice(symbols)
    password_list += password_s


random.shuffle(password_list)


password = ""
for char in password_list:
    password += char


print(password)  
