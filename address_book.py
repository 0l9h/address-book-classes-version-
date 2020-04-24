

address_book = [{'Oleh':'dddd'}]

class AddressBook:

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.user = {self.name:self.phone_number}

    def AddNewUser(self):
        address_book.append(self.user)


test = AddressBook('Marshal', '0823789234')

test.AddNewUser()

print(address_book[1])