#Crea un bucle while con las siguientes características:
#El valor inicial de la variable x será de 0.
#El valor de incremento será 1.
#La condición de salida del bucle será mayor o igual a 30.
#La ejecución se deberá romper cuando x valga 15.
#Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
#Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo: 'Se rompió la ejecución del bucle cuando x valía ' + x.

x = 0
while x < 30: #Hacemos que el siclo siga si el resultado sea menor a 30
    x += 1 #Aque va sumando de 1 en 1 hasta llegar al numero deseado 
    if x == 4 or x == 6 or x == 10: #Si nuestro numero valga 4 o 6 o 10 empezara nuestra proxima condicion
        print("Se salto el valor " + str(x)) #Aqui empieza a saltar los numeros  y te mandara un mesaje que se salta
        continue #Se regresa al ciclo
    if x == 15:
        print("se rompio la ejecucion del bucle cuando x valia " + str(x)) 
        break #Aqui ya termino de llegar y termina el ciclo
    print("El valor del bucle es: " + str(x)) #Musetra en pantalla que los numeros son diferente de 4,6,10,15
