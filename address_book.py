import json

address_book_file = 'data.json'     #   file containing your data

with open(address_book_file, 'r') as readfile:
    address_book = json.load(readfile)                   #   Opening of data.json


class AddressBook:

    def __init__(self, name, phone_number):     #   Initialization
        self.name = name
        self.phone_number = phone_number
        self.user = {self.name:self.phone_number}   #   Converting given from user args into dictionary needed to work with .json file

    def UserInfo(self):
        print(self.phone_number)

    def AddNewUser(self):
        address_book[0]['address'].append(self.user)     #   adding new data
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

    def ChangePhoneNumber(self, new_phone_number):
        self.new_phone_number = new_phone_number
        i = 0
        for dictionary in address_book[0]['address']:     #   Loop through address_book
            if self.name in dictionary:
                address_book[0]['address'][i] = {self.name:self.new_phone_number}       #   Changes phone number of [self.name]
            i+=1
        with open('data.json', 'w') as data_file:
            json.dump(address_book, data_file, indent=4)    #   Dumps new data into .json file
        print('Phone number succesfully changed to', new_phone_number)
    





"""CHECKS EITHER GIVEN FROM USER name IS VALID OR NOT"""
def NameValidation(name, ValidName):
    if len(name)>=3:
        for char in name:
            if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):     #   Check if each char is a letter a-z/A-Z
                pass
            else:
                ValidName = False                                                                       #   If not - invalid data

        if ValidName == False:
            print('Name should contain only a-z/A-z chars')

    else:
        ValidName = False
        print('Name length should be at least 3')

    if ValidName == False:
        print('Invalid name')
        
    return ValidName




'''CHECKS EITHER GIVEN FROM USER phone number IS VALID OR NOT'''
def PhoneNumberValidation(phone_number, ValidPhoneNumber):
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
        global user
        user = AddressBook(name, phone_number)  #   Giving to AddressBook class user params

    else:
        print('Invalid phone number')
    
    return ValidPhoneNumber




UserExists = False
ValidName = True
ValidPhoneNumber = True

name = input('Print your name:\n').title()


if NameValidation(name, ValidName) == True:
    for dictionary in address_book[0]['address']:
        if name in dictionary:
            phone_number = dictionary[name]     #   If user exists, give to phone_number value from .json file
            UserExists = True


    if UserExists == False:
        phone_number = input('Print your phone number:\n')    #   If user doesn't exist, request user to create his phone_number

        if PhoneNumberValidation(phone_number, ValidPhoneNumber):
            user.AddNewUser()       #   If user doesn't exist, create new one


    if UserExists == True:      #   If user exists
        user = AddressBook(name, phone_number)

        user.UserInfo()     #   Get user phone number

        choice = input('Input "del" if you want to delete this name from address book:\n"change" to change phone number:\n')

        if choice == 'del':
            user.DeleteUser()   #   delete user
        elif choice == 'change':
            new_phone_num = input('Input new phone number:\n')
            if PhoneNumberValidation(new_phone_num, ValidPhoneNumber):
                user.ChangePhoneNumber(new_phone_num)       #   Change user phone number
