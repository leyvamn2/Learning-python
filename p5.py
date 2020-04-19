#práctica if
print("evaluacion de notas")

notas=input("Introduce la nota del alumno: \n")

def evaluacion (nota):
	valoracion="aprobado"
	if nota<5:
		valoracion="suspenso"
		
	return valoracion
print(evaluacion (int(notas)))


