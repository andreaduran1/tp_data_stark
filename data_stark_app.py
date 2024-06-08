from funciones import *
from data_stark import lista_personajes

def menu()->str:
    print("\nData Stark.\nInformación a obtener:")
    print("B. Nombre de cada superheroe.")
    print("C. Nombre de cada superheroe y su altura")
    print("D. Superheroe más alto")  
    print("E. Superheroe más bajo")  
    print("F. Altura promedio de los superheroes")
    print("G. Identidad de los superheroes informados en D y E")
    print("H. Superheroe más y menos pesado")
    print("I. Nombre de cada superheroe de género M")
    print("J. Nombre de cada superheroe de género F")
    print("K. Superheroe más alto de género M")
    print("L. Superheroe más alto de género F")
    print("M. Superheroe más bajo de género M")
    print("N. Superheroe más bajo de género F")
    print("O. Altura promedio de los superheroes de género M")
    print("P. Altura promedio de los superheroes de género F")
    print("X. Salir\n")


def data_stark():

    while True:

        menu()
        aux = input("Ingrese la opción de la información a obtener: ")
        opcion = (aux).upper()
        campo = "a"
        
        match opcion:
            case "B":
                nombres_heroes = mapear_lista(lambda heroe: (heroe["nombre"]), lista_personajes)
                print("Los superheroes son: ")
                mostrar_campo(nombres_heroes)
                print()

            case "C":
                print("Superheroe y su altura:")
                mostrar_lista_tuplas(
                mapear_lista(lambda heroe: (heroe["nombre"], heroe["altura"]), lista_personajes)
                )
                print()
                
            case "D":
                heroe_mas_alto = reduce_lista(lambda ant, act: act if ant['altura'] < act['altura'] else ant, lista_personajes)
                print(f"El superheroe más alto es {heroe_mas_alto}")
                print()
            
            case "E":
                heroe_mas_bajo = reduce_lista(lambda ant, act: act if ant['altura'] > act['altura'] else ant, lista_personajes)
                print(f"El superheroe más bajo es {heroe_mas_bajo}")
                print()

            case "F":
                promedio_campo(lista_personajes, campo)
                print()

            case "G":
                print(f"La identidad del heroe más alto es {heroe_mas_alto["identidad"]}")
                print(f"La identidad del heroe más bajo es {heroe_mas_bajo["identidad"]}")
                print()
            case "H":
                heroe_mas_pesado = reduce_lista(lambda ant, act: act if ant['peso'] < act['peso'] else ant, lista_personajes)
                print(f"El heroe más pesado es {heroe_mas_pesado["nombre"]} y pesa {heroe_mas_pesado["peso"]}kg.")
                print()
                heroe_mas_liviano = reduce_lista(lambda ant, act: act if ant['peso'] > act['peso'] else ant, lista_personajes)
                print(f"El heroe más liviano es {heroe_mas_liviano["nombre"]} y pesa {heroe_mas_liviano["peso"]}kg.")
                print()
                                
            case "X":
                break

            case _:
                print("La opción no es válida. Intenta de nuevo.")
                
        

    print("Fin del programa")


data_stark()
