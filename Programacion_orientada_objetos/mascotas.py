class Pet:
    def __init__(self, name , type, noise):
        self.name = name
        self.type = type
        self.health = 100
        self.energy = 50
        self.noise = noise
    def dormir(self):
        self.energy += 25
        return self
    
    def comer(self):
        self.energy += 5
        self.health += 10
        return self
    def jugar(self):
        self.health += 5
        self.energy -= 15
        return self
class ola:
    def __init__(self, first_name, last_name , treats, comida_perro, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = comida_perro
        self.pet = pet
    def caminar(self):
        self.pet.jugar()
        return self
    def dar_comida(self):

        if len(self.dar_comida) > 0:
            food = self.dar_comida.pop()
            print(f"Feeding {self.pet.name} {comida}!")
            self.pet.comer()
        else:
            print("Nececita mas comida!")
        return self

comida = ['pan','comida']

nibbles = Pet("capi")

elian = ola("elian",comida, )

elian.feed();
elian.feed();
elian.feed();