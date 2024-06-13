alphabet = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(plan_text,shift_key):
    cipher_text = ""
    for char in plan_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_key)%26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += char
    print(f"Here's the text after Encryption: {cipher_text}")
    
def decryption(cipher_text,shift_key):
    plane_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_key)%26
            plane_text += alphabet[new_position]
        else:
            plane_text += char
    print(f"Here's the text after Decription: {plane_text}")
    
end = False
while not end:
    what_to_do = input("Type 'encrypt' for Encryption and 'decrypt' for Decription: ")
    text = input("Type your Message:\n").lower()
    shift = int(input("Enter the shift key:"))
    if what_to_do == "encrypt":
        encryption(plan_text=text,shift_key=shift)
    elif what_to_do == "decrypt":
        decryption(text,shift)
    again = input('Type "yes" to Continue and "no" to Exit: ')
    if again == 'no':
        end = True
        print("Have a Nice Day..")