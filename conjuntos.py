cursos_informatica = {"Programación Datos", "Bases de Datos", "Redes"}
cursos_estudiante = set(["Estructuras de Datos", "Resistenciade Materiales", "Hidráulica", "Concreto Armado"])
#print(cursos_informatica)
cursos_informatica.add("Seguridad informática")
#print(cursos_informatica)
curso1 = {"Hidráulica", "Resistencia de Materiales","Estática II"}
curso2 = {"Hidráulica", "Concreto Armado"}
union1 = curso1.union(curso2)
union2 = curso1 | curso2
interseccion2 = curso1 & curso2
diferencia2 = curso2 - curso1
diferencia_simetrica1 = curso1.symmetric_difference(curso2)


es_subconjunto1 = curso1.issubset(curso2)
es_subconjunto2 = curso1 <= curso2
print(es_subconjunto1)
