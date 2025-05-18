estudiante = {
"codigo": "17150415",
"nombre": "Juan Carlos Huamán",
"edad": 21,
"carrera": "Ingeniería de Sistemas",
"cursos": ["Cálculo III", "Estructuras de Datos", "Geología"]
}

#rint(estudiante["cursos"][0])
profesion = estudiante.get('profesion','No se encontró')
#print(profesion)

estudiante["promedio"] = 15.8
estudiante["cursos"].append("Resistencia de Materiales")
#print(estudiante)

datos_adicionales = {
"dni": "71764255",
"direccion": "Ayacucho",
"sexo": "M",
}
estudiante.update(datos_adicionales)
#print(estudiante)
del estudiante["edad"]
#estudiante= estudiante.popitem()
estudiante.clear()
print(estudiante)
