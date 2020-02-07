from PythonBasics.classes.credit_card_class import CreditCard


class PredatoryCreditCard(CreditCard):
    def __init__(self, customer, bank, account, limit, apr):
        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        return success

    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1 + self._apr, 1 / 12)
            self._balance *= monthly_factor



