class CreditCard:
    """ Consumer credit card"""

    # __new__() is always called before __init__().
    # First argument is the class itself which is passed implicitly.
    # Always return a valid object from __new__(). Not mandatory, but that's the whole point.

    def __new__(cls, *args, **kwargs):
        print("From new")
        print(cls)
        print(args)
        print(kwargs)
        # create our object and return it
        obj = super().__new__(cls)
        return obj

    def __init__(self, customer, bank, account, limit):
        """Create a new credit card instance .

        Initial balance is zero.
        customer : Name od the customer
        bank : Name of the bank
        account : Account number
        limit : limit in dollars
        """
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0



    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank

    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment that reduces balance."""
        self._balance -= amount

    @staticmethod
    def get_details():
        return "this is static method"


credit_object = CreditCard(customer="rajeev", bank="sc", account=123, limit=100)

print(type(CreditCard.get_account))  # returns function
print(type(credit_object.get_account))  # returns method

print(CreditCard.get_account(credit_object))  # Equivalent to credit_object.get_account()

# So, anything like obj.method(args) becomes Class.method(obj, args).

print(credit_object.get_details())
print(type(CreditCard.get_details))  # returns function
print(type(credit_object.get_details))  # returns function
