def encode(password):
    result =""
    for i in range (len(password)):
        if int(password[i])<=6:
            result += str(int(password[i]) + 3)
        elif int(password[i]) == 7:
            result += "0"
        elif int(password[i]) == 8:
            result += "1"
        elif int(password[i]) == 9:
            result += "2"
    print(f'"{password}" will become "{result}" after encoding')

def decode(password):
    str_password = str(password)
    dencoded_string = ""
    for num in str_password:
        dencoded_value = str((int(num) - 3) % 10)
        dencoded_string += dencoded_value
    return dencoded_string

if __name__ == '__main__':
    password =""
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        selection = int(input("Please enter an option:"))
        if selection == 1:
            password = input("Please enter your password to encode:")
            password = encode(password)
            print("Your password has been encoded and stored!")
        if selection == 2:
            decode_pass = decode(password)
            print(f"The encoded password is {password}, and the original password is {decode_pass}")
        if selection == 3:
            quit()
