from archivo import guardar_alumnos, leer_alumnos
from utilidades import (

mostrar_alumnos,
pedir_calificacion,
mostrar_ordenados,
buscar_alumno,
mostrar_estadistica,
mostrar_menu,
continuar,
eliminar,
editar
)

def main():
    data_alu = leer_alumnos()

    while True:
        mostrar_menu()
        entrada = input("Seleccione Una Opcion: ").strip().lower()
        
        if entrada in ("1", "agregar alumno"):
            nombre = input("\nIngrese el nombre del alumno:\n").strip().title()
            cal = pedir_calificacion()
            data_alu[nombre] = cal
            guardar_alumnos(data_alu)
            continuar()

        elif entrada in ("2", "ver alumnos"):
            mostrar_alumnos(data_alu)
            continuar()

        elif entrada in ("3", "editar alumno"):
            if not data_alu:
                print("\nNo hay alumnos registrados.\n")
            else:
                editar(data_alu)
                continuar()

        elif entrada in ("4", "eliminar alumno"):
            if not data_alu:
                print ("\nNo hay alumnos registrados.\n")
            else:
                eliminar(data_alu)
                continuar()

        elif entrada in ("5", "buscar alumno"):
            buscar_alumno(data_alu)
            continuar()
            
        elif entrada in ("6", "ver ordenados"):
            mostrar_ordenados(data_alu)
            continuar()

        elif entrada in ("7", "mostrar estadisticas"):
            mostrar_estadistica(data_alu)
            continuar()
            
        elif entrada in ("8", "salir"):
            print ("\nEl programa a finalizado.\n")
            break

        else:
            print ("\nEntrada Invalida, Intentalo de Nuevo.\n")



if __name__ == "__main__":
    main()