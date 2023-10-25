#Prudhvi Chalasani

def menu():
    print('Menu')
    print('-' * 13)
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

def encode(password):
    encoded = ''
    for i in range(len(password)):
        if password[i] == '7':
            encoded += '0'
        elif password[i] == '8':
            encoded += '1'
        elif password[i] == '9':
            encoded += '2'
        else:
            new = int(password[i]) + 3
            encoded += str(new)
    return encoded

if __name__ == '__main__':
    while True:
        menu()
        option = input("Please enter an option: ")
        if option == '1':
            password = input("Please enter your password to encode: ")
            encoded_new = encode(password)
            print("Your Password has been encoded and stored!")

        if option == '2':
            print(f"The encoded password is {encoded_new} and the original password is {password}.")

        if option == '3':
            break
