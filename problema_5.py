# Nombre: Carlos Alberto González Portela
# Grupo: 213022
# Programa: Ingeniería de Sistemas
# Fase 5 - Evaluación Final POA
# Problema 5: Control de horas trabajadas por recurso

# Función para calcular el total de horas semanales y clasificar la jornada
def calcular_horas(horas):
    total = 0
    for h in horas:
        total += h

    if total > 40:
        estado = "Sobretiempo"
    else:
        estado = "Horario Estándar"

    return total, estado

# Matriz con los datos: [Nombre, Lunes, Martes, Miercoles, Jueves, Viernes]
empleados = [
    ["Juan",   8, 8, 9, 7,  8],
    ["Maria",  9, 9, 8, 8,  9],
    ["Carlos", 7, 6, 8, 7,  6],
    ["Ana",   10, 9, 10, 9, 10]
]

# Recorrer la matriz y mostrar resultados
print("=== Reporte de horas trabajadas ===\n")

for empleado in empleados:
    nombre = empleado[0]
    horas  = empleado[1:]  # toma solo las horas (sin el nombre)

    total, estado = calcular_horas(horas)

    print("Empleado    :", nombre)
    print("Total horas :", total)
    print("Clasificación:", estado)
    print("-----------------------------")