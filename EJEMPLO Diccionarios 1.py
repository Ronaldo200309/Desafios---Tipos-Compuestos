#En el bloque principal del programa definir un diccionario que almacene 
#los nombres de paises como clave y como valor la cantidad de habitantes.
#Implementar una función para mostrar cada clave y valor.
def imprimir (paises):
    for clave in paises:
        print (clave, paises[clave])
        
# bloque principal
paises={"argentina": 40000000, "españa": 46000000, "brasil":190000000, "uruguay": 3400000}
imprimir(paises)
