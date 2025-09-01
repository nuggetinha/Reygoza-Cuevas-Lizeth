#declarar un array 
alumnos = ["juan", "pedro", "maria", "luis"]

#datos abstractos
class Alumno:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def __str__(self):
        return f"{self.nombre}: {self.calificacion}"
alumnos = [
    Alumno("juan", 8),
    Alumno("pedro", 7),
    Alumno("maria", 9),
    Alumno("luis", 6)
]
for alumno in alumnos:
    print(alumno)

#datos simples
calificaciones = [8, 7, 9, 6]
print(calificaciones)
