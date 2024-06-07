import json
from copy import deepcopy

def mostrar_menu():
    '''Muestra el menu'''
    print("1-Cargar archivo")
    print("2-Imprimir lista")
    print("3-Asignar totales")
    print("4-Filtrar por tipo")
    print("5-Mostrar servicios ordenados")
    print("6-Guardar servicios en un archivo JSON")
    print("7-Salir")
    opcion = input("Opcion: ")
    return opcion

def limpiar_pantalla():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def presionar_tecla():
    import msvcrt
    print("Pulsa una tecla para volver al menú")
    msvcrt.getch()  # Espera a que el usuario presione una tecla

# Punto 1
def cargar_archivo(nombre_archivo:str):
    '''
    Recibe el nombre del archivo de donde va a cargar los datos
    Carga los datos y retorna los datos obetenidos
    Si hay algun error con la lectura del archivo, arrogara un msj error
    '''
    try:
        with open(nombre_archivo, 'r') as file:
            datos = json.load(file)
            return datos
        
    except FileNotFoundError:
        print("Error. No se encontro el archivo")
    except json.JSONDecodeError:
        print("Error. No se pudo decodificar el archivo JSON")
    except KeyError:
        print("Error. No se encontro esa key")
    except TypeError:
        print("Error. El tipo de dato ingresado es incorrecto")
    except Exception as e:
        print(f"Error inesperado {e}")


# Punto 2
def imprimir_encabezado(col1:str, col2:str, col3:str, col4:str, col5:str, col6:str):
    print(f"{col1:<5} {col2:<30} {col3:<5} {col4:<20} {col5:<10} {col6:<20}")


def imprimir_lista(id:int, descripcion:str, tipo:int, precio:int, cantidad:int, totalServicio:int):
    print(f"{id:<5} {descripcion:<30} {tipo:<5} {precio:<20} {cantidad:<10} {totalServicio:<20}")


# Punto 3
def asignar_totales(datos: list):
    '''
    Recibe la lista de datos
    Con una funcion lambda saca el total de servicios, y con un for modifica el valor de la key totalServicio
    '''
    totalServicio = list(map(lambda x: float(x["cantidad"]) * float(x["precioUnitario"]), datos))
    for i in range(len(datos)):
        datos[i]["totalServicio"] = totalServicio[i]
    return totalServicio


# Punto 4
def  filtrar_por_tipo(datos:list, tipo:int)->list:
    '''
    Recibe la lista de datos, y el tipo que se quiere filtrar
    Crea una lista con todos los datos filtrado por los tipo
    Devuelve una lista con los filtrados 
    '''
    filtrados = list(filter(lambda x: x["tipo"] == tipo, datos))
    print(filtrados)
    return filtrados


def pedir_numero_con_rango(desde:int, hasta:int):
    '''recibe dos parametros, desde y hasta, valida en ese rango y devuelve el numero'''
    numero = int(input("Ingrese un numero'1, 2 o 3': "))
    while numero < desde or numero > hasta:
        numero = int(input("Error. Ingrese un numero: "))
    return numero


# Punto 5
def ordenamiento(lista:list, ordenar_por:str, sentido:bool)-> list:
    '''
    Recibe la lista que se va a ordenar, recibe el nombre de la key que se va a ordenar y recibe un bool dependiendo el sentido que se ordene
    True para ordenar descendente, False para ordenar ascendente
    Retorna una copia de la lista ordenada
    '''
    copia_lista = deepcopy(lista)
    copia_lista.sort(key = lambda x: x[ordenar_por], reverse = sentido)
    return copia_lista


# Punto 6
def crear_archivo_json(nombre_archivo:str , datos:list):
    '''
    Recibe el nombre del archivo que se va a crear y la lista de datos que se va a guardar
    Crea un archivo json con los datos pasados por parametro
    '''
    try:
        with open(nombre_archivo, 'w+') as file:
            json.dump(datos, file, indent=4) 

            print(f"Archivo '{nombre_archivo}' creado exitosamente.")

    except FileNotFoundError:
        print("Error. No se encontro el archivo")
    except json.JSONDecodeError:
        print("Error. No se pudo decodificar el archivo JSON")
    except KeyError:
        print("Error. No se encontro esa key")
    except TypeError:
        print("Error. El tipo de dato ingresado es incorrecto")
    except Exception as e:
        print(f"Error inesperado {e}")