curso = ("IS-402", "Estructuras de Datos", 4, "Dr. Manuel Lagos")
sigla_curso = curso[0]
#creditos = curso[2]
sigla, nombre, creditos, docente = curso

horarios_programacion = [
("Lunes", "08:00", "10:00",["P","F"]),
("Miércoles", "10:00", "12:00"),
("Viernes", "14:00", "16:00")
]
primer_data_lista=horarios_programacion[0]
#print(horarios_programacion[0][3][1])

tupla1 = ("Base de datos", "Estructura de datos")
tupla2 = ("Lenguaje", "Matemática")
tupla_combinada = tupla1 + tupla2
#print(tupla_combinada)

promedio_final = (10, 12, 15, 18, 20)
#print(50 in promedio_final) #False
#print(40 not in promedio_final)

print(len(promedio_final)) #5
print(max(promedio_final)) # 20
print(min(promedio_final)) # 10
print(sum(promedio_final)) # 75
