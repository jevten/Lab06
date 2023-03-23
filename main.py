def encode(string):
    password = ""
    for num in range(len(string)):
        if int(string[num]) == 0:
            password += "3"
        elif int(string[num]) == 1:
            password += "4"
        elif int(string[num]) == 2:
            password += "5"
        elif int(string[num]) == 3:
            password += "6"
        elif int(string[num]) == 4:
            password += "7"
        elif int(string[num]) == 5:
            password += "8"
        elif int(string[num]) == 6:
            password += "9"
        elif int(string[num]) == 7:
            password += "0"
        elif int(string[num]) == 8:
            password += "1"
        elif int(string[num]) == 9:
            password += "2"

def decode(string):
    string_value = ""
    password = str(string)
    for num in password:
        result = str(int(num) - 3)
        string_value += result
        if result == "0":
            string_value += "7"
        elif result == "1":
            string_value += "8"
        elif result == "2":
            string_value += "9"
    return string_value



if __name__ == '__main__':
    string = ""
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option = int(input('Please enter an option:'))
        if option == 1:
            string = input('Please enter your password to encode:')
            string = encode(string)
            print('Your password has been encoded and stored!')
        if option == 2:
            dec_string = decode(string)
            print(f'The encoded password is {string}, and the original password is {dec_string}')
        if option == 3:
            break










