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

estudiante1.mostrar() #Mostramos los datos del estudiante 1


class ceti_nuevo(ceti): #Creamos la nueva clase la cual guardara la herencia
	pass

estudiante2 = ceti_nuevo('Jose Cruz', 'Torres Palomares', 'Mecatronica', 'sexto', 'Vespertino') #Guardamos cada valor en estudiante 2

estudiante2.mostrar() #Mostramos los datos del estudiante 2  pero ya utilizando la herencia
