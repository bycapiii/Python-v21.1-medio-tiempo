class CuentaBancaria:
    cuentas=[]
    def __init__(self, tasa_interés, balance): 
        self.tasa_interés = tasa_interés
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def depósito(self, amount):
        self.balance +- amount
        return self
    
    def retiro(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print(1000)
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        return (f"{self.balance}")
    
    def generar_interés(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interés)
        return self
    
    def imprime(self):
        print(f"{self.tasa_interés}  monto {self.balance}")
        return self

poto= CuentaBancaria (0.2,1500) 
    
poto.depósito(100)

poto.retiro(100)

poto.mostrar_info_cuenta()

poto.generar_interés()

poto.imprime()