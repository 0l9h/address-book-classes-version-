import json

address_book_file = 'data.json'     #   file containing your data

with open(address_book_file, 'r') as readfile:
    address_book = json.load(readfile)                   #   Opening of data.json

addresses = address_book[0]['address']      #   Taking from .json file only adresses

class AddressBook:

    def __init__(self, name, phone_number):     #   Initialization
        self.name = name
        self.phone_number = phone_number
        self.user = {self.name:self.phone_number}   #   Converting given from user args into dictionary needed to work with .json file

    def UserInfo(self):
        print(self.phone_number)

    def AddNewUser(self):
        addresses.append(self.user)     #   adding new data
        with open(address_book_file, 'w') as writefile:
            json.dump(address_book, writefile, indent=4)    #   dumping new data to .json file
        print('New user was succesfully added')

    def DeleteUser(self):
            i = 0
            for dictionary in address_book[0]['address']:     #   Loop through address_book
                if self.name in dictionary:
                    del address_book[0]['address'][i]       #   Deletes data about [self.name]
                i+=1

            with open('data.json', 'w') as data_file:
                json.dump(address_book, data_file, indent=4)    #   Dumps new data into .json file

            print('User succesfully deleted')

UserExists = False

ValidName = True
ValidPhoneNumber = True

name = input('Print your name:\n')


"""CHECKS EITHER GIVEN FROM USER name IS VALID OR NOT"""

if len(name)>=3:
    for char in name:
        if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):     #   Check if each char is a letter a-z/A-Z
            pass
        else:
            ValidName = False                                                                       #   If not - invalid data

else:
    ValidName = False
    print('Name length should be at least 3')

if ValidName == False:
    print('Invalid name')
    


if ValidName == True:
    for dictionary in addresses:
        if name in dictionary:
            phone_number = dictionary[name]     #   If user exists, give to phone_number value from .json file
            UserExists = True


    if UserExists == False:
        phone_number = input('Print your phone number:\n')    #   If user doesn't exist, request user to create his phone_number


        '''CHECKS EITHER GIVEN FROM USER phone number IS VALID OR NOT'''
        if len(phone_number) == 10:
            for digit in phone_number:
                if ord(digit) >= 48 and ord(digit) <= 57:
                    pass
                else:
                    ValidPhoneNumber = False
            if ValidPhoneNumber == False:
                print('Phone number should contain only 0-9 chars')
        else:
            ValidPhoneNumber = False
            print('Phone number should contain 10 chars')

        if ValidPhoneNumber == True:
            user = AddressBook(name, phone_number)  #   Giving to AddressBook class user params
        else:
            print('Invalid phone number')


    if UserExists == True:      #   If user exists, get data about him
        user.UserInfo()
        delete = input('Input "del" if you want to delete this name from address book:\n')
        if delete == 'del':
            user.DeleteUser()

    elif ValidPhoneNumber == True:
        user.AddNewUser()       #   If user doesn't exist, create new one
