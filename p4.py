#Tuplas
#las tuplas son como listas pero más restringidas, ya que sus valores no cambian
tupla1="Tengo",16,3,20
#en las tuplas se pueden guardar valores para almacenarse en variables
nombre,dia,mes,an=tupla1

tupla2=("Hola",)

lista1=["mucho","sueñoo", "tengo"]
#acceder a elemento
print(tupla1[:])

#cambiar tupla a lista
listaa=list(tupla1)
print(listaa)

#convertir lista en tupla
tuplaa=tuple(lista1)
print(tuplaa)
print("Tengo" in tupla1)

#count
print(tupla1.count(3))

#lenght longitud de la tupla
print(len(tupla1))
print(len(tupla2))
print(nombre)
print(an)
print(mes)
print(dia)