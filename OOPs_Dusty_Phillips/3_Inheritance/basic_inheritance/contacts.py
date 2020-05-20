class Contacts:
    all_contacts = list()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


contact1 = Contacts("rajeev", "email")
print(Contacts.all_contacts[0].email)
print(contact1.all_contacts)


class Supplier(Contacts):
    def order(self, order):
        print("If this were a real system we would send '{}' order to '{}'".format(order, self.name))


supplier1 = Supplier("rahul", "outlook")
supplier1.order("iphone")
print(supplier1.all_contacts)
