from cipher_alphabet import alphabet
repeat  = True
while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))


    def encrypt(p_text,shift_amount):
        cipher = ""
        for letter in p_text:
            if letter in alphabet:
                position  = alphabet.index(letter)
                new_position = position + shift_amount            
                new_letter = alphabet[new_position]
                cipher += new_letter
            else:
                cipher+=letter
        print(f"The encoded text is {cipher}")
    def decrypt(p_text,shift_amount):
        decipher = ""
        for letter in p_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                decipher += new_letter
            else:
                decipher+=letter
        print(f"The decoded text is {decipher}")

    if direction == "encode":
        encrypt( p_text = text,shift_amount = shift)
    elif direction == "decode":
        decrypt(p_text = text,shift_amount = shift)
    elif direction != "encode" or direction != "decode":
        print("Invalid input")
    again = input("Do you want to go again? y or n").lower()
    if again == "n":
        repeat = False
