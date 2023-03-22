#Jevan Tenaglia
#iterate through password and add by 3 to each digit
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

encode("00009962")