num1 = 42 #variable declaration
num2 = 2.3 #variable declaration
boolean = True #variable declaration
string = 'Hello World' #variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration
fruit = ('blueberry', 'strawberry', 'banana')#variable declaration
print(type(fruit)) # print to console, type check
print(pizza_toppings[1])# print to console, type check
pizza_toppings.append('Mushrooms')#variable declaration
print(person['name']) # print to console, Dictionary access value
person['name'] = 'George'#variable declaration
person['eye_color'] = 'blue'#variable declaration
print(fruit[2])
# Conditional if, evaluation, print to console, Conditional else, print to console
if num1 > 45: 
    print("It's greater")
else:
    print("It's lower")
# Conditional if - elif - else, print to console.
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# For Loop start at 0 and goes up to until 5
for x in range(5):
    print(x) 
for x in range(2,5): # For Loop start at 0 and goes up to until 5
    print(x)
for x in range(2,10,3): # For loop start at 2 goes up to until 10, increments by 3
    print(x)
x = 0
while(x < 5): # For loop start at 2 goes up to until 10, increments by 3
    print(x)
    x += 1

pizza_toppings.pop() # List delete value at end
pizza_toppings.pop(1) # List delete value at index

print(person)  # print to console of dictionary
person.pop('eye_color') Dictionary delete value
print(person) # print to console of dictionary
# for loop through a list
for topping in pizza_toppings:    #Conditional if
    if topping == 'Pepperoni':
        continue       # Conintues
    print('After 1st if statement')
    if topping == 'Olives':
        break         # stops the loop
 
def print_hello_ten_times():  # For Loop start at 0 and goes up to until 5
    for num in range(10): 
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):# For Loop start at 0 and goes up to until 5
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): # For Loop start at 0 and goes up to until 5
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)