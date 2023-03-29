class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0
        
    def hacer_deposito(self, amount):
        self.amount += amount
        return self
    def hacer_retiro(self,amount):
        self.amount -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self
    def transferir_dinero(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

elian = User("elian")
agustin = User("agustin")
pato = User("pato")

elian.hacer_deposito(500).hacer_deposito(100).hacer_deposito(150).hacer_retiro(900).display_user_balance()

agustin.hacer_deposito(1000).hacer_deposito(100).hacer_retiro(900).hacer_retiro(50).display_user_balance()

pato.hacer_deposito(3000).hacer_retiro(1000).hacer_retiro(2000).hacer_retiro(1000).display_user_balance()

agustin.transferir_dinero(700, elian)










