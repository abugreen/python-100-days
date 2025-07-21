import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']





    # new_text =""
    # if direction == "encode":
    #     for i in range(0, len(text)):
    #         pos = alphabet.index(text[i])
    #         new_text += alphabet[pos+shift]
    #     print(new_text)
    # if direction == "decode":
    #     for i in range(0, len(text)):
    #         pos = alphabet.index(text[i])
    #         new_text += alphabet[pos-shift]
    #     print(new_text)

# hello ,2
# def encrypt(original_text , shift_mount):
#     cipher_text =""
#     for letter in original_text:
#         shifted_pos = alphabet.index(letter)+shift_mount
#         shifted_pos %= len(alphabet) #0-25
#         cipher_text += alphabet[shifted_pos]  
#     print(f"Here is encode result : {cipher_text}")
    

# def dencrypt(original_text , shift_mount):
#     decode_text = ""
#     for letter in original_text:
#         shifted_pos = alphabet.index(letter)-shift_mount
#         shifted_pos %= len(alphabet)
#         decide_text += alphabet[shifted_pos]
#     print(f"Here is dencode result : {dencrypt_text}")
    
def caesar (original_text, shift_mount, encode_or_decode):
    output_text =""
    if encode_or_decode == "decode":
        shift_mount *= -1
    for letter in original_text:
        if letter.isalpha():
            shifted_pos = alphabet.index(letter)+shift_mount
            shifted_pos %= len(alphabet) #0-25
            output_text += alphabet[shifted_pos] 
        else :
             output_text += letter
    print(f"Here is {encode_or_decode} : {output_text}")    

# caesar(text,shift,direction)

run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)

    choice = input("Do you want to run this program again?\nType 'yes' or 'no': ")
    if choice == "no":
        run = False
        print("Good Bye")

    
