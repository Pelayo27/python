# Crae listas

estudiantes=["Ana","Leonel","Rolando"]

estudiantes.append("Fernando")
estudiantes.append("Alex")
estudiantes.append("Angel")
estudiantes.append("Cristian")
estudiantes.append("23")
estudiantes.append("2")
estudiantes.insert(1,"Aldo Marcos")
# Eliminar
##estudiantes.remove("Ana")

#Eliminar de una posición
estudiantes.pop(0)
print(estudiantes)
estudiantes.sort(reverse=False)
print(estudiantes)
notas=[1,45,230,1.5]
notas.sort()

lista_combinada=estudiantes+notas
print(lista_combinada)
