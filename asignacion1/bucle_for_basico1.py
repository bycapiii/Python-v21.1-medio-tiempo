#Basico
for i in range (151):
    print(i)
#Multiplos de 5
for i in range (0,1001,5):
    print(i)

#Contar a la manera del dojo

for i in range(101):
     if i % 10 == 0:
        print("coding dojo")
     elif i % 5 == 0:
          print("coding")
     else:
        print(i)
#whaoo, es un gran idiota
sum = 0
for i in range(1,500001,2):
    sum += i
print (sum)

#cuenta regresiva de a 4
for i in range(2018, 0, -4):
    print(i)

#contador flex
Lownum = 2
Highnum = 9
mult = 3
for i in range(Lownum, Highnum + 1):
    if i % mult == 0:
        print(i)
    