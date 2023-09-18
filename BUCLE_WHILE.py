#Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.
print("primer ciclo")
x = 0
while x <= 15: #Empieza el ciclo y termina hasta que sea 15
    print(x)
    x += 5 #Suma de 5 en 5 
print("\n\n")

#Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
print("segundo ciclo")
x = 0
while x >= -100: #Empieza el ciclo y termina hasta que sea igual a -100
    print(x)
    x -= 20 #Se resta de 20 en 20
print("\n\n")

#Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que muestre en cada
#ejecución esta frase con el valor de ejecución correspondiente: 'El valor del bucle es 10'
print("tercer ciclo")
x = 10
while x >= 0:
    print('El valor del bucle es ' + str(x)) #Mostramos en pantalla el valor del bucle
    x -= 1 #Se resta de 1 en 1
