#Haz una tupla que contenga cuatro colores de tu elecci�n. Tendr�s que poner una condici�n con el condicional
# if para cada color que le avise al usuario que el color est� en la tupla con un mensaje como este: 
# print('El color rojo est� admitido') y una condici�n False para contemplar cualquier color que no est� en
# la tupla con un mensaje como este: print('Color no admitido'). No puedes utilizar el operador ==. Adem�s
# tendr�s que hacer esto con un input() que permita introducir un color al usuario.


color = input("Introduce un Color. ") #Pedimos el color al usuario
tupla = ('negro','azul','rojo','morado') #Creamos la tupla con colores

if color in tupla[0]:
	print('El color negro esta admitido')
elif color in tupla[1]:
	print('El color azul esta admitido')
elif color in tupla[2]:
	print('El color rojo esta admitido')
elif color in tupla[3]:
	print('El color morado esta admitido')
else:
	print('Color no admitido')