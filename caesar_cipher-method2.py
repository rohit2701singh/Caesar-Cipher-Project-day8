ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
             'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']

code_dict = {
    "encode": 1,
    "decode": -1,
}

encrypt_decrypt = {
    "encode": "encrypted",
    "decode": "decrypted",
}

finished = False
while not finished:
    direction = input("\ntype 'encode' to encrypt or 'decode' to decrypt: ").lower()
    text = input("type your message: ").lower()
    shift = int(input("type the shift number: "))


    def code_decode(input_direction, text_input, shift_number):
        code = ""
        for letter in text_input:
            if letter in ALPHABETS:
                shift_index = ALPHABETS.index(letter) + code_dict[input_direction] * (shift_number % 26)
                shifted_letter = ALPHABETS[shift_index]
                code += shifted_letter
            else:
                code += letter
        return code


    coded_word = code_decode(direction, text, shift)
    print(f"your {encrypt_decrypt[direction]}_code is: {coded_word}\n")

    user_input = input("do you want to continue? type 'y' or 'n': ").lower()
    if user_input == "y":
        finished = False
    else:
        finished = True


