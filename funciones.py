
def validar_lista(lista: list) -> None:
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista.")
    
def validar_texto(texto:str)->None:
    if not isinstance(texto,str):
        raise TypeError("Se esperaba un caracter")
    
def convertir_valores_a_float(diccionario:dict, claves:str)->None:
    for clave in claves:
        valor = diccionario.get(clave)
        if valor:
            try:
                # Intenta convertir el valor a float
                valor_convertido = float(valor)
                # Actualiza el valor en el diccionario
                diccionario[clave] = valor_convertido
            except ValueError:
                # Si no se puede convertir mantener el valor original
                valor_convertido = valor

def convertir_valores_a_entero(diccionario:dict, claves:str)->None:
    for clave in claves:
        valor = diccionario.get(clave)
        if valor:
            try:
                # Intenta convertir el valor a float
                valor_convertido = int(valor)
                # Actualiza el valor en el diccionario
                diccionario[clave] = valor_convertido
            except ValueError:
                # Si no se puede convertir mantener el valor original
                valor_convertido = valor

def validar_campo(campo:str)->str:

    match campo:
        case "a": retorno = "altura"
        case "n": retorno = "nombre"
        case "g": retorno = "genero"
        case "p": retorno = "peso"
        case "co": retorno = "color_ojos"
        case "cp": retorno = "color_pelo"
        case _: raise ValueError("Campo inválido")

    return retorno


def sumar_lista(lista: list) -> int:
    suma = 0
    validar_lista(lista)
    for i in lista:
        suma += i

    return suma


def calcular_promedio(lista: list) -> float:
    validar_lista(lista)

    if len(lista) != 0:
        promedio = sumar_lista(lista) / len(lista)
        return promedio
    else:
        return "No se puede dividir por 0"


def mostrar_heroes(heroes: list) -> None:
    validar_lista(heroes)

    print("         ***Lista de Superheroes***             ")
    print("            Nombre                   Identidad           Empresa    Altura   Peso    Genero       Color de ojos          Color de pelo     Fuerza  Inteligencia")
    print("----------------------------------------------------------------------")

    for i in range(len(heroes)):
        mostrar_heroe(heroes[i])


def mostrar_heroe(heroe: dict) -> None:

    print(
        f"{heroe["nombre"]:>22} {heroe["identidad"]:>30} {heroe["empresa"]:>10} {float(heroe['altura']):>6.2f} {float(heroe['peso']):>6.2f} {heroe["genero"]:>8} {heroe["color_ojos"]:>26} {heroe["color_pelo"]:>20} {heroe["fuerza"]:>4} {heroe["inteligencia"]:>12}"
    )


def mapear_lista(procesadora, lista: list)->list:
    validar_lista(lista)

    lista_retorno = []
    for el in lista:
        lista_retorno.append(procesadora(el))
    
    return lista_retorno

def filtrar_lista(filtradora, lista: list)->list:
    validar_lista(lista)

    lista_filtrada = []
    for el in lista:
        if filtradora(el):
            lista_filtrada.append(el)
    return lista_filtrada


def mostrar_lista_tuplas(lista:list)->None:
    validar_lista(lista)

    for tupla in lista:
        for elemento in tupla:
            print(f"{elemento:24}",end="")
        print()

def mostrar_campo(lista:list)->None:
    validar_lista(lista)

    for el in lista:
        print(f"{el}",end="")
        print()


def reduce_lista(funcion, lista, valor_inicial = None):
    validar_lista(lista)
    tam = len(lista)
    if tam == 0:
        raise ValueError("Error. Lista vacia")
    
    for heroe in lista:
        convertir_valores_a_float(heroe, ["altura"]) # Convertir altura a float
        convertir_valores_a_float(heroe, ["peso"]) # Convertir peso a float
        convertir_valores_a_entero(heroe, ["edad"]) #Convertir edad a int
    
    if valor_inicial:
        ant = valor_inicial
        indice = 0
    else:
        ant = lista[0]
        indice = 1

    for act in lista[indice:]:
        ant = funcion(ant,act)
    
    return ant


def swap_lista(lista: list, i: int, j: int) -> None:
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def mapear_campo(lista:list, campo:str)->None:
    validar_lista(lista)
    campo = validar_campo(campo)
    lista_retorno = []

    for heroe in lista:
        lista_retorno.append(heroe[campo])

    return lista_retorno


def ordenar_lista(comparator, lista: list) -> None:
    validar_lista(lista)
    tam = len(lista)

    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if comparator(lista[i], lista[j]):
                swap_lista(lista, i, j)


def promedio_campo(lista:list, campo:str):
    validar_lista(lista)
    resultado = mapear_campo(lista,campo)
    campo = validar_campo(campo)
        
    print(f"El promedio de {campo} es {calcular_promedio(resultado):.2f}")


def contar_elementos_por_clave(lista, clave)->list:
    validar_lista(lista)
    conteo = {}
    for heroe in lista:
        valor = heroe.get(clave)
        if not valor:
            valor = "No tiene"
        if valor in conteo:
            conteo[valor] += 1
        else:
            conteo[valor] = 1
    return list(conteo.items())


def agrupar_heroes_por_clave(lista, clave):
    validar_lista(lista)
    agrupacion = {}
    for heroe in lista:
        valor = heroe.get(clave)
        if not valor:
            valor = "No tiene"
        if valor in agrupacion:
            agrupacion[valor].append(heroe)
        else:
            agrupacion[valor] = [heroe]
    return list(agrupacion.items())


