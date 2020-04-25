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
"""
print("Asignaturas optativas Año 2017")
print("Asignaturas disponibles:")
asignaturas={1:"Informática gráfica",2:"Pruebas de Software",3:"Usabilidad y Accesabilidad"}
print("1.- Informática Gráfica.")
print("2.- Pruebas de software")
print("3.- Usabilidad y accesabilidad")
eleccion=int(input("Digita el número de la asignatura escogida: "))
if eleccion in (1,2,3):
 print("La asignatura escogida es "+ asignaturas[eleccion])
else:
 print("La asignatura escogida no está disponible.")
 """
import time
print("Menú: \n Hoy se sirven tacos y antojitos. \n  ")
comida=["tacos de tripa", "tacos de chorizo", "tacos de asada", "tacos de arrachera", "enchiladas","pozole", "flautas"]
print("Tacos: 1.tacos de tripa, 2.tacos de chorizo, 3.tacos de asada, 4.tacos de arrachera.\n")
print("Antojitos: 5.enchiladas, 6.pozole, 7. flautas.\n")
orden=input("Escriba lo que desea ordenar: \n")
if orden in (comida):
 print("Escriba la cantidad de "+ orden +" que desea ordenar:\n")
 num=int(input())
 if num >0:
  print("Orden tomada, por favor espere")
  print("...")
  time.sleep(3)
  print("Orden recibida, pedido en proceso")
 else:
  print("Error en número, intente de nuevo")
else:
 print("Opcion no disponible en el menú del día. \n")
 print(" Pedido pendiente.")	


#if cantidad < 0 :
#		print("orden capturada, su orden fue"+ str(cant)+"de"+ orden)
#else:
#		print("Error en captura de orden. Intente de nuevo")


