class CuentaBancaria:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        CuentaBancaria.accounts.append(self)

    def depositar(self, amount):
        self.balance += amount
        return self

    def retirar(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def info_cuenta(self):
        return f"{self.balance}"

    def interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_c(cls):
        for account in cls.accounts:
            account.info_cuenta()


class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : CuentaBancaria(.02,1000),
            "savings" : CuentaBancaria(.05,3000)
        }
        

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_info_cuenta()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_info_cuenta()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


adrien = User("Adrien")

adrien.account['checking'].depositar(100)
adrien.display_user_balance()