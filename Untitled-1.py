class Category:
    def __init__(self, name):
        self.ledger = []
        self.name = name

    def deposit(self, amount, description=None):
       self.ledger.append({'amount': int(amount), 'description': description}) 
    
    def withdraw(self, amount, description=''):
        if self.check_funds(amount)==True:
            self.ledger.append({'amount': int(amount), 'description': description})
            return True
        else:
            return False
    
    def check_funds(self, amount, funds=0):
        for payment in self.ledger:
            funds += payment['amount']
            if funds>=amount:
                return True
            else:
                return False

    def get_balance(self):
        return self.ledger[0]['amount']

    def transfer(self, amount, category):
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self}')
        return self.ledger


def create_spend_chart(categories):
    pass
c = Category('food')
d= Category('dog')
print(c.deposit(555))
print(c.withdraw(4))
print(c.get_balance())
print(c.transfer(4,d))