# main.py
from mi_clase import MiClase
from claseAlumno import claseAlumno

# Crear una instancia de la clase
mi_objeto = MiClase("Juan")

# Llamar al metodo

print(mi_objeto.saludar())


# Diccionario global para almacenar alumnos
registro_alumnos = {}

# Capturar 3 registros
for i in range(3):
    alumno = claseAlumno()
    alumno.set_nombre(input("Introduce el nombre: "))
    alumno.set_apellido_paterno(input("Introduce el apellido paterno: "))
    alumno.set_apellido_materno(input("Introduce el apellido materno: "))
    alumno.set_no_control(input("Introduce el número de control: "))
    alumno.set_semestre(int(input("Introduce el semestre: ")))

    registro_alumnos[i] = alumno

# Mostrar los nombres completos de los registros
for i in range(3):
    print(f"Nombre completo: {registro_alumnos[i].get_Nombre_Completo()}")
