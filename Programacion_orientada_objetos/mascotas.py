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

    def __init__(self, first_name, last_name , treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    
    def caminar(self):
        self.pet.jugar()
        return self

    def feed(self):

        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.comer()
        else:
            print("Oh no!!! you need more pet food!")
        return self
    
    def bathe(self):
        self.pet.noise()

my_treats = ['Snausage','Bacon',"Trash Bag"]
my_pet_food = ['Pizza','Burger']

nibbles = Pet("Mr. Nibbles","Horse",['nibbles on things','is invisible'],"Hey Hey")

elian = ola("elian","Dion",my_treats,my_pet_food, nibbles)

elian.feed();
elian.feed();
elian.feed();