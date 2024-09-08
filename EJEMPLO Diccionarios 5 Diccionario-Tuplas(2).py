#Confeccionar una agenda. Utilizar un diccionario cuya clave sea la fecha.
#Permitir almacenar distintas actividades para la misma fecha (se ingresa la hora y la actividad)
#Implementar las siguientes funciones:
#1) Carga de datos en la agenda.
#2) Listado completo de la agenda.
#3) Consulta de una fecha.

def cargar():
    agenda = {}
    continua1 = "s"
    while continua1.lower() == "s":
        fecha = input("Ingrese la fecha con formato dd/mm/aa: ")
        lista = agenda.get(fecha, [])  
        continua2 = "s"
        while continua2.lower() == "s":
            hora = input("Ingrese la hora de la actividad con formato hh:mm: ")
            actividad = input("Ingrese la descripción de la actividad: ")
            lista.append((hora, actividad))
            continua2 = input("¿Desea ingresar otra actividad para la misma fecha? [s/n]: ")
        agenda[fecha] = lista
        continua1 = input("¿Desea ingresar otra fecha? [s/n]: ")
    return agenda

def imprimir(agenda):
    print("\nListado completo de la agenda")
    if not agenda:
        print("La agenda está vacía.")
    else:
        for fecha in agenda:
            print(f"\nPara la fecha: {fecha}")
            for hora, actividad in agenda[fecha]:
                print(f"  {hora}: {actividad}")

def consulta_fecha(agenda):
    fecha = input("Ingrese la fecha que desea consultar (dd/mm/aa): ")
    if fecha in agenda:
        print(f"\nActividades para la fecha {fecha}:")
        for hora, actividad in agenda[fecha]:
            print(f"  {hora}: {actividad}")
    else:
        print("No hay actividades agendadas para esa fecha.")

# Bloque principal
agenda = cargar()
imprimir(agenda)
consulta_fecha(agenda)

