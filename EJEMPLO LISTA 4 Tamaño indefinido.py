#Realizar la carga de valores enteros por teclado,
#almacenarlos en una lista. Finalizar la carga de enteros al ingresar el cero. 
#Mostrar finalmente el tamaño de la lista.
lista=[]
valor=int(input("Ingresar valor (0 para finalizar):"))
while valor!=0:
    lista.append(valor)
    valor=int(input("Ingresar valor (0 para finalizar):"))
print("Tamano de la lista:")
print(len(lista))
