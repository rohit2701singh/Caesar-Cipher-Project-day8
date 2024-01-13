from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(plain_text, shift_amount, cipher_direction):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if cipher_direction == "encode":
                new_position = position + (shift_amount % 26)
            elif cipher_direction == "decode":
                new_position = position - (shift_amount % 26)
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter
    print(f"\nThe {cipher_direction} text is {cipher_text}")


restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caesar(plain_text=text, shift_amount=shift, cipher_direction=direction)

    play_again = input("\ndo you want to restart? type 'yes' or 'no' : ").lower()
    if play_again == "no":
        restart = False
print("you chose to stop.\nThank You ")

