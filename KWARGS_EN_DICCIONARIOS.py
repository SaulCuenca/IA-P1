def alumno(**kwargs):
   for registro in kwargs.items():
      print(registro)
      
estudiante = {"nombre":"saul" , "carrera":"mecatronica", "edad":"22"}

alumno(**estudiante)

