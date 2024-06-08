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
    print("Q. Nombre del superheroe asociado a cada uno de los indicadores anteriores ítems K a N)")
    print("R. Determinar cuántos superheroes tienen cada tipo de color de ojos)")
    print("S. Determinar cuántos superhéroes tienen cada tipo de color de pelo")
    print("T. Determinar cuántos superhéroes tienen cada tipo de inteligencia")
    print("U. Listar todos los superhéroes agrupados por color de ojos")
    print("V. Listar todos los superhéroes agrupados por color de pelo")
    print("W. Listar todos los superhéroes agrupados por tipo de inteligencia")
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
                print(f"El superheroe más alto es: ")
                mostrar_heroe(heroe_mas_alto)
                print()
            
            case "E":
                heroe_mas_bajo = reduce_lista(lambda ant, act: act if ant['altura'] > act['altura'] else ant, lista_personajes)
                print(f"El superheroe más bajo es: ")
                mostrar_heroe(heroe_mas_bajo)
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

            case "I":
                try:
                    heroe_m = filtrar_lista(lambda heroe: heroe["genero"] == "M", lista_personajes)
                    mostrar_heroes(heroe_m)
                    print()

                except ValueError as ex:
                    print(ex)     

            case "J":
                try:
                    heroe_f = filtrar_lista(lambda heroe: heroe["genero"] == "F", lista_personajes)
                    mostrar_heroes(heroe_f)
                    print()

                except ValueError as ex:
                    print(ex)

            case "K":
                mas_alto_masculino= reduce_lista(lambda ant, act: act if ant['altura'] < act['altura'] else ant, heroe_m)
                mostrar_heroe(mas_alto_masculino)

            case "L":
                mas_alto_femenino= reduce_lista(lambda ant, act: act if ant['altura'] < act['altura'] else ant, heroe_f)
                mostrar_heroe(mas_alto_femenino)

            case "M":
                mas_bajo_masculino= reduce_lista(lambda ant, act: act if ant['altura'] > act['altura'] else ant, heroe_m)
                mostrar_heroe(mas_bajo_masculino)

            case "N":
                mas_bajo_femenino= reduce_lista(lambda ant, act: act if ant['altura'] > act['altura'] else ant, heroe_f)
                mostrar_heroe(mas_bajo_femenino)

            case "O":
                campo = "a"
                promedio_campo(heroe_m, campo)

            case "P":
                campo = "a"
                promedio_campo(heroe_f, campo)

            case "Q":
                print(mas_alto_masculino["nombre"])
                print(mas_alto_femenino["nombre"])
                print(mas_bajo_masculino["nombre"])
                print(mas_bajo_femenino["nombre"])
                print()

            case "R":
                conteo_color_ojos = contar_elementos_por_clave(lista_personajes, "color_ojos")
                print("Conteo por color de ojos:")
                mostrar_lista_tuplas(conteo_color_ojos)

            case "S":
                conteo_color_pelo = contar_elementos_por_clave(lista_personajes, "color_pelo")
                print("Conteo por color de pelo:")
                mostrar_lista_tuplas(conteo_color_pelo)

            case "T":
                conteo_inteligencia = contar_elementos_por_clave(lista_personajes, "inteligencia")
                print("Conteo por inteligencia:")
                mostrar_lista_tuplas(conteo_inteligencia)

            case "U":
                agrupacion_color_ojos = agrupar_heroes_por_clave(lista_personajes, "color_ojos")
                for valor in agrupacion_color_ojos:
                    print(f"Agrupación por color de ojos: {valor[0]}")
                    mostrar_heroes(valor[1])
                    print()

            case "V":
                agrupacion_color_pelo = agrupar_heroes_por_clave(lista_personajes, "color_pelo")
                for valor in agrupacion_color_pelo:
                    print(f"Agrupación por color de pelo: {valor[0]}")
                    mostrar_heroes(valor[1])
                    print()

            case "W":
                agrupacion_inteligencia = agrupar_heroes_por_clave(lista_personajes, "inteligencia")
                for valor in agrupacion_inteligencia:
                    print(f"Agrupación por inteligencia: {valor[0]}")
                    mostrar_heroes(valor[1])
                    print()

            case "X":
                break

            case _:
                print("La opción no es válida. Intenta de nuevo.")
                
        

    print("Fin del programa")


data_stark()
