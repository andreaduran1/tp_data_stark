from funciones import *
from data_stark import lista_personajes

# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #01 los siguientes puntos,
# utilizando un menú que permita acceder a cada uno de los puntos por separado.
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
try:
    heroe_m = filtrar_lista(lambda heroe: heroe["genero"] == "M", lista_personajes)
    mostrar_heroes(heroe_m)
    print()

except ValueError as ex:
    print(ex)
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
try:
    heroe_f = filtrar_lista(lambda heroe: heroe["genero"] == "F", lista_personajes)
    mostrar_heroes(heroe_f)
    print()

except ValueError as ex:
    print(ex)
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
mas_alto_masculino= reduce_lista(lambda ant, act: act if ant['altura'] < act['altura'] else ant, heroe_m)
mostrar_heroe(mas_alto_masculino)
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
mas_alto_femenino= reduce_lista(lambda ant, act: act if ant['altura'] < act['altura'] else ant, heroe_f)
mostrar_heroe(mas_alto_femenino)
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
mas_bajo_masculino= reduce_lista(lambda ant, act: act if ant['altura'] > act['altura'] else ant, heroe_m)
mostrar_heroe(mas_bajo_masculino)
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
mas_bajo_femenino= reduce_lista(lambda ant, act: act if ant['altura'] > act['altura'] else ant, heroe_f)
mostrar_heroe(mas_bajo_femenino)
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
campo = "a"
promedio_campo(heroe_m, campo)
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
campo = "a"
promedio_campo(heroe_f, campo)
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
print(mas_alto_masculino["nombre"])
print(mas_alto_femenino["nombre"])
print(mas_bajo_masculino["nombre"])
print(mas_bajo_femenino["nombre"])
print()
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
conteo_color_ojos = contar_elementos_por_clave(lista_personajes, "color_ojos")
print("Conteo por color de ojos:")
mostrar_lista_tuplas(conteo_color_ojos)
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
conteo_color_pelo = contar_elementos_por_clave(lista_personajes, "color_pelo")
print("Conteo por color de pelo:")
mostrar_lista_tuplas(conteo_color_pelo)

# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
conteo_inteligencia = contar_elementos_por_clave(lista_personajes, "inteligencia")
print("Conteo por inteligencia:")
mostrar_lista_tuplas(conteo_inteligencia)
# M. Listar todos los superhéroes agrupados por color de ojos.
agrupacion_color_ojos = agrupar_elementos_por_clave(lista_personajes, "color_ojos")
for valor in agrupacion_color_ojos:
    print(f"Agrupación por color de ojos: {valor[0]}")
    mostrar_heroes(valor[1])
    print()
# N. Listar todos los superhéroes agrupados por color de pelo.
agrupacion_color_pelo = agrupar_heroes_por_clave(lista_personajes, "color_pelo")
for valor in agrupacion_color_pelo:
    print(f"Agrupación por color de pelo: {valor[0]}")
    mostrar_heroes(valor[1])
    print()

# O. Listar todos los superhéroes agrupados por tipo de inteligencia
agrupacion_inteligencia = agrupar_heroes_por_clave(lista_personajes, "inteligencia")
for valor in agrupacion_inteligencia:
    print(f"Agrupación por inteligencia: {valor[0]}")
    mostrar_heroes(valor[1])
    print()


