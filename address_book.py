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

UserExists = False

name = input('Print your name:\n')
for dictionary in addresses:
    if name in dictionary:
        phone_number = dictionary[name]     #   If user exists, give to phone_number value from .json file
        UserExists = True


if UserExists == False:
    phone_number = input('Print your phone number:\n')    #   If user doesn't exist, request user to create his phone_number


test = AddressBook(name, phone_number)  #   Giving to AddressBook class user params

if UserExists == True:      #   If user exists, get data about him
    test.UserInfo()
else:
    test.AddNewUser()       #   If user doesn't exist, create new one

