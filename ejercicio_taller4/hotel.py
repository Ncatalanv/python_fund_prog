datos=      {
    "reserva": [
                    {
                        "id_reserva":"re01",
                        "nombre_huesped":"Nicolás",
                        "numero_habitacion":105,
                        "tipo_habitacion":"Individual",
                        "cantidad_dias":3,
                        "costo_total": 2500
                    },
                    {
                        "id_reserva":"re02",
                        "nombre_huesped":"Juan",
                        "numero_habitacion":106,
                        "tipo_habitacion":"Doble",
                        "cantidad_dias":9,
                        "costo_total": 12990
                    },
                    {
                        "id_reserva":"re03",
                        "nombre_huesped":"Hugo",
                        "numero_habitacion":110,
                        "tipo_habitacion":"Suite",
                        "cantidad_dias":15,
                        "costo_total": 17990
                    }
                ]
            }



def buscar_reserva(id_reserva:str):
    """Buscar una reserva por su identificador único."""
    for i in datos["reserva"]:
        if id_reserva == i["id_reserva"]:
            return i
    return False


def valida_numero_entero_positivo(mensaje:str):
    while True:
        try:
            numero = int(input(mensaje))
            if numero < 0:
                print("Error, debes ingresar un número positivo.")
                continue
            return numero
        except ValueError:
            print("Error, debes ingresar un número entero.")
            continue

def valida_texto(mensaje:str):
    """Válida que el texto no esté vacío"""
    while True:
        texto = input(mensaje)
        if len(texto) == 0:
            print("No puede estar vacío.")
            continue
        else:
            return texto

def valida_tipo_habitacion():
    while True:
        tipo_habitacion = input("Ingrese el tipo de habitación (individual - doble - suite): ")
        if tipo_habitacion == "individual" or tipo_habitacion == "doble" or tipo_habitacion == "suite":
            return tipo_habitacion
        else:
            print("No existe este tipo de habitación.")
            continue


def calcula_costo_habitacion(tipo_habitacion:str, cantidad_dias:int):
    #individual 50
    #doble 80
    #suite 120/dia
    if tipo_habitacion == "individual":
        return cantidad_dias * 50
    elif tipo_habitacion == "doble":
        return cantidad_dias * 80
    #Pongo else, porque tengo una función que me válida ya el tipo de habitación!
    else:
        return cantidad_dias * 120
    

#Funciones para válidar que el código sea númerico y tenga letras

def valida_numero_id_reserva(id_reserva:str):
    #id_reserva = "abc1"
    numero = "0123456789"

    #Va a recorrer el id_reserva (i), y por cada valor de id_reserva recorrerá "numero" (j) completo
    for i in id_reserva:
        for j in numero:
            if i == j:
                return True
    return False

def valida_letra_id_reserva(id_reserva:str):
    letra = "abcdefghijklmnñopqrstuvwxyz"
    for i in id_reserva:
        for j in letra:
            if i == j:
                return True
    return False


def agregar_reserva(id_reserva:str, nombre:str, numero_habitacion:int, tipo_habitacion:str, cantidad_dias:int):
    reserva_generada =  {
                            "id_reserva": id_reserva,
                            "nombre_huesped":nombre,
                            "numero_habitacion":numero_habitacion,
                            "tipo_habitacion":tipo_habitacion,
                            "cantidad_dias":cantidad_dias,
                            #Llama función que calcula costo habitación
                            "costo_total": calcula_costo_habitacion(tipo_habitacion, cantidad_dias)
                        }

    datos["reserva"].append(reserva_generada)


def buscar_habitacion(numero_habitacion:int):
    for i in datos["reserva"]:
        if i["numero_habitacion"] == numero_habitacion:
            return True
    return False


def modificar_reserva(id_reserva:int, cantidad_dias:int, tipo_habitacion:str):
    reserva_encontrada = buscar_reserva(id_reserva)
    if reserva_encontrada == False:
        print("Reserva no encontrada.")
    else:
        reserva_encontrada['cantidad_dias'] = cantidad_dias
        reserva_encontrada['tipo_habitacion'] = tipo_habitacion
        reserva_encontrada['costo_total'] = calcula_costo_habitacion(tipo_habitacion, cantidad_dias)
        print("Reserva modificada exitosamente!")


def menu():
    while True:
        print(" ***** Hotel ***** ")
        print("[1] - Agregar reserva")
        print("[2] - Buscar reserva")
        print("[3] - Modificar reserva")
        print("[4] - Cancelar reserva")
        print("[5] - Mostrar todas las reservas")
        print("[6] - Salir")

        opc = valida_numero_entero_positivo("Ingresa tu opción 1 - 6: ")

        if opc == 1:
            print("Opción 1")
            print(" --- Agregar reserva --- ")
            while True:
                id_reserva = valida_texto("Ingrese el id ded la reserva: ")

                if buscar_reserva(id_reserva) != False:
                    print("El id ya se encuentra registrado")
                    continue
                elif valida_letra_id_reserva(id_reserva) == False:
                    print("Debe tener un número.")
                    continue
                elif valida_numero_id_reserva(id_reserva) == False:
                    print("Debe tener una letra.")
                    continue
                break
            
            nombre = valida_texto("Ingrese el nombre del húesped: ")

            while True:
                numero_habitacion = valida_numero_entero_positivo("Ingrese número de habitación: ")

                if numero_habitacion < 101 or numero_habitacion > 999:
                    print("Habitación debe estar entre 101 y 999.")
                    continue

                if buscar_habitacion(numero_habitacion) == True:
                    print("Esta habitación ya está reservada")
                    continue
                break

            tipo_habitacion = valida_tipo_habitacion()
            dias_instancia = valida_numero_entero_positivo("Ingrese cantidad de días a reservar: ")

            agregar_reserva(id_reserva, nombre, numero_habitacion, tipo_habitacion, dias_instancia)
            print("Reserva agregada exitosamente!")
                
        elif opc == 2:
            print(" --- Buscar reserva --- ")

            id_reserva = valida_texto("Ingrese id de reserva: ")

            id_encontrada = buscar_reserva(id_reserva)

            if id_encontrada == False:
                print("No se ha encontrado una reserva con ese id.")
            else:
                print(f"ID: {id_encontrada["id_reserva"]}, Húesped: {id_encontrada['nombre_huesped']}, Habitación: {id_encontrada['numero_habitacion']}, Días: {id_encontrada['cantidad_dias']}, Total: {id_encontrada['costo_total']}")


        elif opc == 3:
            print(" --- Modificar reserva --- ")
            id_reserva = valida_texto("Ingrese id de la reserva a modificar: ")
            cantidad_dias = valida_numero_entero_positivo("Ingrese cantidad de días: ")
            tipo_habitacion = valida_tipo_habitacion()

            modificar_reserva(id_reserva, cantidad_dias, tipo_habitacion)

        elif opc == 4:
            print(" --- Cancelar reserva --- ")
            id_reserva = valida_texto("Ingrese id de reserva a cancelar: ")
            reserva_encontrada = buscar_reserva(id_reserva)

            if reserva_encontrada == False:
                print("No se ha encontrado una reserva con ese id.")
            else:
                datos["reserva"].remove(reserva_encontrada)
                print("Reserva cancelada exitosamente.")

        elif opc == 5:
            print(" --- Mostrar todas las reservas --- ")
            for i in datos["reserva"]:
                print(f"ID: {i["id_reserva"]}, Húesped: {i['nombre_huesped']}, Habitación: {i['numero_habitacion']}, Días: {i['cantidad_dias']}, Total: {i['costo_total']}")
        elif opc == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")


menu()
#print(buscar_habitacion(110))
#print(valida_letra_id_reserva("2323r32"))
#print(valida_numero_id_reserva("qweqwe2"))
#print(valida_tipo_habitacion())
#print(datos["reserva"][1])