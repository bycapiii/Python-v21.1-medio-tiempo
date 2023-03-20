#1
def number_of_food_groups():
    return 5
print(number_of_food_groups()) 
#el print imprimira la declaracion de numeros alimentarios

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#el print va a dar error ya que hay una declaracion que no esta definida 

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#el print imprimira la declaracion 5 veces

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
# se imprimira un print(10) y despues la declaracion 5 veces

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# se imprimira un numero 5 y abajo 


#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#declara la funcion add con los parametros, b y c


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# establece la funcion  contatenante con dos parametros, b y c


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# toma el parametro de la funcion y depues se devuelve el valor 5, consecutivamente imprime el valor 100 y 10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# se imprimira un numero 7, un numero 14 y la suma de las 2 anteriores dando como resultado 21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#se imprimira la suma de b + c = 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# imprimira 500, despues 500, despues 300 porque llama a la foobar y por ultimo 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# imprimira 500, despues 500, despues 300 porque el return lo retorna a 300 y por ultimo 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# imprimira 500 ,despues 500, despues 300 porque el return hace que el valor sea 300 y por ultimo 300 ya que se llama a la foobar 

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#se imprime 1, despues 3 y despues 2 



#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# se imprime 1, despues 3 , despues 5 y despues 10 ya que se llama a la declaracion "y"