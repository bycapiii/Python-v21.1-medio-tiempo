local_val = "unicornios mágicos"
def square(x):
    return x * x
class Usuario:
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hola"
    print(square(5))
user = Usuario("Anna")
print(usuario.name)
print(usuario.di_hola())
print(locals())