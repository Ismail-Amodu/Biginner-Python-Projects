#Program to decrypt a mesaage

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Caesar Function
def caesar(choice, message_text, shift_amount):
        end_text = ""      
        for letter in message_text:           
            position = alphabet.index(letter)
            if choice == "decode":
                shift_amount *= -1
            new_position = position + shift_amount
            end_text += alphabet[new_position]              
        print(f"The {choice}d text is {end_text}")

caesar(choice=direction, message_text=text, shift_amount=shift)