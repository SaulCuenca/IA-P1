#Elimina de la siguiente lista los elementos 'azul' y 'blanco' utilizando el método pop(). 
#Además, tendrás que guardar esos dos colores en una nueva lista.

colores = ['rojo', 'azul', 'verde', 'amarillo', 'marron', 'lila', 'negro', 'rosa', 'blanco', 'naranja']#Creamos una lista con los colores mencionados

color1 = colores.pop(1) #Eliminamos de la lista el color azul y lo guardamos en color1
color2 = colores.pop(-2) #Eliminamos de la lista el color blanco y lo guardamos en color2

print(colores) #Mostramos en pantalla que nustros colores se eliminaron

colores2 =[color1 , color2] #Creamos la nueva lista con LOS COLORES ELIMINADOS
print(colores2) #Mostramos en pantalla la nueva lista
