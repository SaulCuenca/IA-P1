import re #Importamos la libreria que nos ayudara a realizar la busqueda

nombre = "Saul Armando Cuenca Martinez" #Guardamos nuestro nombre en uan variables
print("\nNombre en el que buscara: Saul Armando Cuenca Martinez   \n")

buscar = re.search("a", nombre) #Lo que hacemos es que utilizando search buscara la letra "a" en la variable nombre
print("\n" , buscar) #Mostara el resultado y nos dira en que posicion y en que string se encuentra

buscar2 = re.search("A", nombre) #Lo que hacemos es que utilizando search buscara la letra "A" en la variable nombre
print("\n" ,buscar2) #Mostara el resultado y nos dira en que posicion y en que string se encuentra


buscar3 = re.search("Cuenca", nombre) #Lo que hacemos es que utilizando search buscara la palabra "Cuenca" en la variable nombre
print("\n" , buscar3, "\n") #Mostara el resultado y nos dira en que posicion y en que string se encuentra



