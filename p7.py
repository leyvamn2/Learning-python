# condicionales y concatenacion de comparaciones

"""#concatenar comparativos

print("Validacion de edad \n")
edad=int(input("Escriba la edad a validar:\n"))

if 0< edad <100:
	print("Edad correcta")

else:
	print("Edad incorrecta")"""

"""
#Validacion de salario

print("Validador de salarios")


salario_presidente=int(input("El salario del presidente es: \n$"))

salario_director=int(input("El salario del director es: \n$"))

salario_jarea=int(input("Escriba el salario de jefe de area: \n$ "))

salario_admin=int(input("Escriba el salario de administrativo: \n$ "))

if salario_admin<salario_jarea<salario_director<salario_presidente:
		print("Los salarios se encuentran valdidados")
else:
	print("Error. Validar salarios nuevamente")
"""

#In
print("Menú: \n Hoy se sirven tacos y antojitos. \nTacos: tacos de tripa, tacos de chorizo, tacos de asada, tacos de arrachera. \n Antojitos: enchiladas, pozole, flautas.")

orden=input("Escriba lo que desea ordenar")

if orden in ("enchiladas", "pozole", "flautas","tacos de tripa", "tacos de chorizo", "tacos de asada", "tacos de arrachera"):
	
	cant= int(input("Escriba la cantidad de "+ orden +" que desee: \n")
		if cant>1:
		print("orden capturada, su orden fue"+ str(cant)+ orden)
		else:
		print("Error en captura de orden. Intente de nuevo")

else:
	print("Opcion no disponible en el menú del día. \n")
	print(" Pedido pendiente.")	