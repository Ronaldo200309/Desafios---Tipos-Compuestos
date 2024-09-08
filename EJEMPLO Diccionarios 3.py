#Desarrollar una aplicación que nos permita crear un diccionario 
#ingles/castellano. La clave es la palabra en ingles y el valor 
#es la palabra en castellano.
#Crear las siguientes funciones:
#1) Cargar el diccionario.
#2) Listado completo del diccionario.
#3) Ingresar por teclado una palabra en ingles y si existe en el diccionario

def cargar():
    diccionario={}
    continua="s"
    while continua=="s":
        caste=input("Ingrese palabra en castellano:")
        ing=input("Ingrese palabra en ingles:")
        diccionario [ing]=caste
        continua=input("Quiere cargar otra palabra: [s/n]")
    return diccionario

def imprimir(diccionario):
    print("Listado completo del diccionario")
    for ingles in diccionario:
        print (ingles, diccionario[ingles])
        
def consulta_palabra(diccionario):
    pal=input("Ingrese la palabra en ingles a consultar:")
    if pal in diccionario:
        print("En castellano significa:",diccionario[pal])
        
#bloque principal
diccionario=cargar()
imprimir(diccionario)
consulta_palabra (diccionario)
