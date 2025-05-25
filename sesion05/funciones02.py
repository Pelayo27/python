# Sin funciones: mucho código repetido
def calcular_promedio_curso(lista_notas):
    total_notas = sum(lista_notas)
    cantidad_notas = len(lista_notas)
    if cantidad_notas == 0:
        return 0 # Evitar división por cero
    promedio = total_notas / cantidad_notas
    return promedio

notas_algoritmos = [15, 12, 18, 10, 14]
notas_estructuras = [13, 16, 11, 17, 9]

promedio_notas=calcular_promedio_curso(notas_algoritmos)
promedio_notas_e=calcular_promedio_curso(notas_estructuras)

print(promedio_notas)
print(promedio_notas_e)
