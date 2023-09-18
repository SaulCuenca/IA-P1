#De la lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'.
#Debes utilizar al menos una vez las posiciones negativas para eliminar un color. 
#Después, imprime la lista para ver los colores que se han eliminado.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#Creamos la lista con los colores anteriores


del colores[1] #Utilizamos del para eliminar el color azul
del colores[4] #Utilizamos del para eliminar el marron
del colores[-4] #Utilizamos del para eliminar negro
del colores[-3] #Utilizamos del para eliminar rosa

print(colores)#Mostramos en pantalla para comprobar los colores que nos quedan
