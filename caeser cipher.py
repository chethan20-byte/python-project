alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Don't change the code above ⬆️



def encrypt(plain_text,shift_amount):
    cipher=""
    for letter in plain_text:
        position=alphabet.index(letter)
        newpositon=position+shift_amount
        new_letter=alphabet[newpositon]
        cipher+=new_letter
    print(f"the encoded text is {cipher}")    
 

def decrypt(cipher,shift_amount):
    deciphered=""
    for letter  in cipher:
        cipher_position=alphabet.index(letter)
        new_cipher=cipher_position-shift_amount
        decrypt_letter=alphabet[new_cipher]
        deciphered+=decrypt_letter
    print(f"the decrypted message is {deciphered}")
    

if direction=="encode":
    encrypt(plain_text=text,shift_amount=shift)    
elif direction=="decode":
    decrypt(cipher=text,shift_amount=shift)    
