from biblioteca import *

datos = []
ordenados = []
bandera = 0

{
        "id_servicio": "50",
        "descripcion": "ruedo pantalon",
        "tipo": "1",
        "precioUnitario": "250",
        "cantidad": "2",
        "totalServicio": "0"
    },

while True:
    opcion = mostrar_menu()
    if opcion == "1":
        # nombre_archivo = input("Ingrese el nombre del archivo")
        datos = cargar_archivo("data.json")
        print(datos)
        bandera = 1
    elif opcion == "2":
        if bandera == 1:
            limpiar_pantalla()
            imprimir_encabezado("Id", "Descripcion", "Tipo", "Precio Unitario", "Cantidad", "Total Servicio")
            for dato in datos:
                imprimir_lista(dato["id_servicio"], dato["descripcion"], dato["tipo"], dato["precioUnitario"], 
                            dato["cantidad"], dato["totalServicio"])
            presionar_tecla()
        else:
            print("Primero debe cargar los datos")
    elif opcion == "3":
        if bandera == 1:
            totales = asignar_totales(datos)
            print(datos[0])
        else:
            print("Primero debe cargar los datos")
    elif opcion == "4":
        if bandera == 1:
            tipo = pedir_numero_con_rango(1, 3)
            tipo = str(tipo)
            filtrados = filtrar_por_tipo(datos, tipo)
            crear_archivo_json("filtrados.json", ordenados)
        else:
            print("Primero debe cargar los datos")
    elif opcion == "5":
        if bandera == 1:
            ordenados = ordenamiento(datos, "descripcion", False)
            limpiar_pantalla()
            imprimir_encabezado("Id", "Descripcion", "Tipo", "Precio Unitario", "Cantidad", "Total Servicio")
            for ordenado in ordenados:
                imprimir_lista(ordenado["id_servicio"], ordenado["descripcion"], ordenado["tipo"], ordenado["precioUnitario"], 
                            ordenado["cantidad"], ordenado["totalServicio"])
            presionar_tecla()
            bandera = 2
        else:
            print("Primero debe cargar los datos")    
    elif opcion == "6":
        if bandera == 2:
            crear_archivo_json("datos.json", ordenados)
        else:
            print("Primero debe cargar y ordenador los datos")    
    elif opcion == "7":
        print("salir")
        break
    else:
        print("Error. Elije un opcion correcta")