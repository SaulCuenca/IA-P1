#Crea un bucle while con las siguientes caracter�sticas:
#El valor inicial de la variable x ser� de 0.
#El valor de incremento ser� 1.
#La condici�n de salida del bucle ser� mayor o igual a 30.
#La ejecuci�n se deber� romper cuando x valga 15.
#Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#En cada salto de ejecuci�n, deber�s mostrar los valores saltado con este mensaje: 'Se salt� el valor ' + x ' de x'.
#Cuando se rompa la ejecuci�n del bucle deber�s mostrar un mensaje indic�ndolo: 'Se rompi� la ejecuci�n del bucle cuando x val�a ' + x.

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
