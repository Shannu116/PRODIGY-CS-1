letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)
def Encryption(plaintext, key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
    return ciphertext

def decryption(ciphertext, key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
    return plaintext

print()
print("############################################### CAESAR CIPHER TOOL #####################################################")
print()
print('Enter the option to encrypt or decrypt ?')
user_input= input('encrypt/decrypt: ').lower()
print()
if user_input == 'encrypt':
    print('You have selected the Encryption')
    print()
    key = int(input('Enter the Key (1 to 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = Encryption(text, key)
    print(f'CIPHERTEXT : {ciphertext}')
elif user_input == 'decrypt':
    print('You have selected the decryption')
    print()
    key = int(input('Enter the key (1 to 26): '))
    text = input('Enter the encrypted text to decrypt: ')
    plaintext = decryption(text, key)
    print(f'PLAINTEXT : {plaintext}')
