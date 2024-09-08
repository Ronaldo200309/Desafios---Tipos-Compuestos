#Definir una tupla con tres valores enteros. Convertir el contenido de
#la tupla a tipo lista. Modificar la lista y luego convertir la lista en tupla. 
fechatupla1=(25, 12, 2016)
print("Imprimimos la primer tupla")
print (fechatupla1)
#copiamos la tupla en una lista
fechalista=list (fechatupla1)
print("Imprimimos la lista que se le copio la tupla anterior")
print (fechalista)
#modificamos la lista
fechalista [0]=31
print("Imprimimos la lista ya modificada")
print (fechalista)
#copiamos la lista modificada a una tupla
fechatupla2=tuple (fechalista)
print("Imprimimos la segunda tupla que se le copio la lista")
print (fechatupla2)
