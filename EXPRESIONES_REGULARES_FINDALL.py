import re #Importamos la libreria que nos ayudara a realizar la busqueda

traba = "como quieres que te quiera si el que quiero no me quiere como quiero que me quiera" #Guardamos el trabalenguas en una variables

print("El trabalenguas que utilizaremos es: \n\n como quieres que te quiera si el que quiero no me quiere como quiero que me quiera\n")

buscar = re.findall("e", traba) #Lo que hacemos es que utilizando search buscara la letra "e" en la variable traba
print(buscar) #Mostara el resultado y nos dira todas las "e" que hay

buscar1 = re.findall("q", traba) #Lo que hacemos es que utilizando search buscara la letra "q" en la variable traba
print("\n",buscar1) #Mostara el resultado y nos dira todas las "q" que hay

buscar2 = re.findall("qui", traba) #Lo que hacemos es que utilizando search buscara nuestras palabras "qui" en la variable traba
print("\n",buscar2, "\n") #Mostara el resultado y nos dira todas las "qui" que hay


