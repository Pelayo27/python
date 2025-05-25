# Sin funciones: mucho código repetido
notas_algoritmos = [15, 12, 18, 10, 14]
suma_algoritmos = 0
for nota in notas_algoritmos:
    suma_algoritmos += nota
    promedio_algoritmos = suma_algoritmos / len(notas_algoritmos)
print(f"Promedio de Algoritmos: {promedio_algoritmos:.2f}")

notas_estructuras = [13, 16, 11, 17, 9]
suma_estructuras = 0
for nota in notas_estructuras:
    suma_estructuras += nota
    promedio_estructuras = suma_estructuras /len(notas_estructuras)
print(f"Promedio de Estructura de Datos:{promedio_estructuras:.2f}")
