def guardar_alumnos(alumnos):
    with open ("alumnos.txt", "w") as archivo:
        for nombre, cal in alumnos.items():
            archivo.write (f"{nombre},{cal}\n")

def leer_alumnos():
    alu = {}

    try:    
        with open ("alumnos.txt", "r") as archivo:
            for linea in archivo:
                nombre, cal = linea.strip().split(",")
                alu[nombre] = float(cal)
    except FileNotFoundError:
        pass
    return alu