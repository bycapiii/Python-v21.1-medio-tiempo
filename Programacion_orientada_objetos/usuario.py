class Usuario:      
    name_bank= "Primer Dojo Nacional"

    def __init__(self, name, balance_cuenta):
        self.name = name
        self.balance_cuenta = balance_cuenta

    def hacer_depósito(self, amount):
        self.balance_cuenta += amount

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
    def hacer_transferencia(self,name , amount):
        self.balance_cuenta += amount


name = "agustin"

balance_cuenta =1000


agustin = Usuario(name,balance_cuenta)

agustin.hacer_retiro(100)

agustin.hacer_depósito(500)

agustin.hacer_retiro(900)


name = "Elian"

balance_cuenta =1000

Elian = Usuario(name,balance_cuenta)

Elian.hacer_depósito(1000)
Elian.hacer_depósito(100)
Elian.hacer_retiro(900)


name = "pato"

balance_cuenta =1000

pato = Usuario(name,balance_cuenta)

pato.hacer_depósito(3000)
pato.hacer_retiro(1000)
pato.hacer_retiro(1000)
pato.hacer_retiro(2000)


print(f"Usuario:{agustin.name,agustin.balance_cuenta}")

print(f"Usuario:{pato.name,pato.balance_cuenta}")

print(f"Usuario:{Elian.name,Elian.balance_cuenta}")