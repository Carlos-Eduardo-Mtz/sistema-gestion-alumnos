from archivo import guardar_alumnos

def mostrar_menu():
    print("\n" + "="*40)
    print("      SISTEMA DE GESTIÓN DE ALUMNOS")
    print("="*40)
    print("1. Agregar alumno")
    print("2. Ver alumnos")
    print("3. Editar alumno")
    print("4. Eliminar alumno")
    print("5. Buscar alumno")
    print("6. Ver ordenados")
    print("7. Mostrar estadísticas")
    print("8. Salir")
    print("="*40)


def estado(calificacion):
    if calificacion >= 6:
        return "Aprobado"
    else:
        return "Reprobado"


def mostrar_alumnos(data_alu):
    if not data_alu:
        print("\nNo hay alumnos registrados.\n")
        return

    for nombre, cal in data_alu.items():
        print(
            f"Alumno: {nombre} - Calificación: {cal} - Estado: {estado(cal)}"
            )


def pedir_calificacion():
    while True:
        try:
            cal = float(input("Ingrese la calificacion (0-10):\n"))
            if 0<= cal <= 10:
                return cal
            
            else:
                print("\nLa calificacion debe estar entre 0 y 10.\n")

        except ValueError:
            print ("\nIngrese solo numeros.\n")


def mostrar_ordenados(data_alu):
    if not data_alu:
        print ("\nNo hay alumnos registrados.\n")
        return
    
    ordenados = sorted(data_alu.items(), key=lambda x: x[1], reverse=True)

    for nombre, cal in ordenados:
        print (f"{nombre} - {cal} - {estado(cal)}")


def buscar_alumno(data_alu):
    if not data_alu:
        print ("\nNo hay alumnos registrados.\n")
        return

    nombre = input("\nNombre a buscar:\n").strip().title()

    if nombre in data_alu:
        cal = data_alu[nombre]
        print (f"{nombre} - {cal} - {estado(cal)}")

    else:
        print ("\nAlumno no encontrado.\n")


def mostrar_estadistica(data_alu):
    if not data_alu:
        print ("\nNo hay alumnos registrados.\n")
        return
    
    calificaciones = data_alu.values()
    promedio = sum(calificaciones) / len(calificaciones)

    mejor = max(data_alu, key=data_alu.get)

    peor = min(data_alu, key=data_alu.get)

    print (f"\nPromedio del grupo: {promedio:.2f}\n")
    print (f"Mejor alumno: {mejor} ({data_alu[mejor]})\n")
    print (f"Alumno con menor calificacion: {peor} ({data_alu[peor]})\n")

 
def continuar():
    input("\nPresione ENTER para continuar...")

def eliminar(data_alu):
    mostrar_alumnos(data_alu)
    nombre_eliminar = input("\nIngrese el alumno a eliminar:\n").strip().title()

    if nombre_eliminar in data_alu:
        del data_alu[nombre_eliminar]
        guardar_alumnos(data_alu)
        print (
            f"\nEl alumno '{nombre_eliminar}' se ha eliminado correctamente.\n")
    else:
        print (f"\nAlumno no encontrado.\n")

def editar(data_alu):
    mostrar_alumnos(data_alu)
    nombre_editar = input("\nIngrese el alumno a editar:\n").strip().title()

    if nombre_editar in data_alu:
        n_cal = pedir_calificacion()
        data_alu[nombre_editar] = n_cal
        guardar_alumnos(data_alu)
    else:
        print("\nAlumno no encontrado.\n")