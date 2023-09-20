class ceti:
	def __init__(self, nombre, apellidos, carrera, grado, turno): #Creamos los elementos que tenfra nuestra clase
		self.nombre = nombre 
		self.apellidos = apellidos
		self.carrera = carrera            #Les brindamos una variable en la cual se guardaran nuestros datos
		self.grado = grado
		self.turno = turno


	def mostrar(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos, '\nCarrera:', self.carrera, '\nGrado:', self.grado, '\nTurno:', self.turno) #Aqui solo es lo que msotraremos en pantalla usando self
		


estudiante1 = ceti('Saul Armando', 'Cuenca Martinez', 'Mecatronica', 'sexto', 'Vespertino\n\n') #Guardamos cada valor en estudiante 1


estudiante2 = ceti('Jose Cruz', 'Torres Palomares', 'Mecatronica', 'sexto', 'Vespertino') #Guardamos cada valor en estudiante 2

del estudiante2 #Lo que hacemos aqui es eliminar el registro del estudiante 2

estudiante1.mostrar() #Mostramos los datos del estudiante 1
estudiante2.mostrar() #Mostramos los datos del estudiante 2 pero es solo rectificar que no dara nada por que lo hemos elimado antes

