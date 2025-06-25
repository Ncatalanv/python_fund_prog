datos = {
    "estudiantes": [
        {
            "nombre": "nicolas",
            "edad": 25,
            "genero": "masculino",
            "codigo": "est123",
            "promedio": 3.5
        }
    ]
}

def validar_nombre(mensaje:str):
    """Válida si el nombre está repetido"""
    while True:
        nombre = input(mensaje)

        for i in datos["estudiantes"]:
            if nombre != i["nombre"]:
                return nombre
            else:
                print("Este nombre ya existe, intentelo nuevamente.")
        continue
        
def validar_edad(mensaje:str):
    """Verifica que la edad esté dentro del rango estimado"""
    while True:
        edad = int(input(mensaje))
        
        if edad >= 12 and edad <= 80:
            return edad
        else:
            print("Error, la edad debe ser entre 12 y 80 años.")
            continue

def valida_numero_entero_positivo(mensaje:str):
    """Válida que sea un número entero y positivo"""
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero
            else:
                print("Debe ser un número positivo.")
        except ValueError:
            print("Debe ser un número entero.")
            continue

def validar_genero(mensaje:str):
    """Válida que solo retorne M o F"""
    while True:
        genero = input(mensaje)

        if genero.lower() == "f" or genero.lower() == "m":
            return genero.upper()
        else:
            print("Opción no válida.")
            continue 


def validar_codigo_letra(codigo:str):
    """Válida que el código contenga letras"""

    letras = "abcdefghijklmnñopqrstuivwxyz"

    for i in codigo:
        for j in letras:
            if i == j:
                return True        
    return False
        
def validar_codigo_numero(codigo:str):
    """Válida que el código contenga números"""

    lista_numeros = "0123456789"

    for i in codigo:
        for j in lista_numeros:
            if i == j:
                return True
    return False

def validar_digitos(codigo:str):
    """Válida que sea un código de 6 carácteres"""

    if len(codigo) == 6 :
        return True
    else:
        return False 


def codigo_unico(codigo:str):
    """Válida que el código sea único"""
    for i in datos["estudiantes"]:
        if codigo != i["codigo"]:
            return i
    return False


def validar_promedio_rango(promedio:str):
    """Válida que el promedio esté dentro del rango (1 - 7)"""
    while True:
        if promedio >= 1 and promedio <= 7:
            return True
        return False

def validar_promedio_decimal(mensaje:str):
    """Válida que el promedio sea un número."""
    while True:
        try:
            promedio = float(input(mensaje))
            return promedio
        except ValueError:
            print("Debe ser un número.")
            continue

def valida_texto(mensaje:str):
    """Válida que el texto no esté vacío"""
    while True:
        texto = input(mensaje)

        if len(texto) == 0:
            print("Texto no debe estár vacío.")
            continue
        return texto

def registrar_estudiante(nombre:str, edad:int, genero:str, codigo:str, promedio:float):
     registrar = {
                    "nombre": nombre,
                    "edad": edad,
                    "genero": genero,
                    "codigo": codigo,
                    "promedio": promedio
                }
     
     datos["estudiantes"].append(registrar)

def buscar_estudiante(codigo_nombre):
    for i in datos["estudiantes"]:
        if codigo_nombre == i["nombre"] or codigo_nombre == i["codigo"]:
            return i
    return False


def modificar_estudiante(codigo:str, edad:int, genero:str, promedio:float):
    estudiante_encontrado = buscar_estudiante(codigo)

    if estudiante_encontrado == False:
        print("No se ha encontrado un estudiante con este código.")
    else:
        estudiante_encontrado["edad"] = edad
        estudiante_encontrado["genero"] = genero
        estudiante_encontrado["promedio"] = promedio
        print("Estudiante modificado exitosamente.")


def eliminar_estudiante(codigo:str):
    estudiante = buscar_estudiante(codigo)

    if estudiante == False:
        print("No se ha podido encontrar estudiante.")
    else:
        datos["estudiantes"].remove(estudiante)
        print("Se ha eliminado el estuddiante correcatamente.")

def menu():
    while True:
        print(" *** Menú *** ")
        print("[1] - Registrar estudiante")
        print("[2] - Buscar estudiante")
        print("[3] - Modificar datos de estudiante")
        print("[4] - Eliminar estudiante")
        print("[5] - Mostrar todos los estudiantes")
        print("[6] - Salir")
        opc = valida_numero_entero_positivo("Ingrese una opción 1 - 6: ")

        if opc == 1:
            print(" --- Registro de estudiante --- ")

            nombre_agregar = validar_nombre("Ingrese nombre del estudiante: ")
            edad_agregar = validar_edad("Ingrese edad del estudiante: ")
            genero_agregar = validar_genero("Ingrese género del estudiante (F - M): ")

            while True:
                codigo_agregar = valida_texto("Ingresa el código del alumno (6 carácteres): ")

                if validar_codigo_numero(codigo_agregar) == False:
                    print("Debe contener números")
                    continue
                elif validar_codigo_letra(codigo_agregar) == False:
                    print("Debe contener letras")
                    continue
                elif validar_digitos(codigo_agregar) == False:
                    print("Debe ser de 6 dígitos")
                    continue
                elif codigo_unico(codigo_agregar) == False:
                    print("Este código ya está registrado.")
                    continue
                break
                
            while True:
                promedio_agregar = validar_promedio_decimal("Ingrese promedio del alumno: ")

                if validar_promedio_rango(promedio_agregar) == False:
                    print("No está dentro del rango de notas.")
                    continue
                break

            registrar_estudiante(nombre_agregar, edad_agregar, genero_agregar, codigo_agregar, promedio_agregar)
            print("Se ha agregado exitosamente.")

        elif opc == 2:
            print(" --- Búsqueda de estudiante --- ")
            while True:
                buscar = valida_texto("Ingrese id o nombre del estudiante a buscar: ")
                estudiante_encontrado = buscar_estudiante(buscar)
                if estudiante_encontrado == False:
                    print("Código de estudiante no encontrado.")
                    continue
                else:
                    print(f"Nombre: {estudiante_encontrado['nombre']} - Edad: {estudiante_encontrado['edad']} - Género: {estudiante_encontrado['genero']} - Código: {estudiante_encontrado['codigo']} - Promedio: {estudiante_encontrado['promedio']}")
                break

        elif opc == 3:
            print(" --- Modificar estudiante --- ")

            buscar = valida_texto("Ingrese código del estudiante a modificar: ")


            edad_agregar = validar_edad("Ingrese edad del estudiante: ")
            genero_agregar = validar_genero("Ingrese género del estudiante (F - M): ")
            while True:
                promedio_agregar = validar_promedio_decimal("Ingrese promedio del alumno: ")

                if validar_promedio_rango(promedio_agregar) == False:
                    print("No está dentro del rango de notas.")
                    continue
                break

            modificar_estudiante(buscar, edad_agregar, genero_agregar, promedio_agregar)
        
        elif opc == 4:
            print(" --- Eliminar estudiante --- ")
            
            buscar = valida_texto("ingrese código del estudiante a eliminar: ")

            eliminar_estudiante(buscar)

        elif opc == 5:

            if len(datos["estudiantes"]) == 0:
                print("No hay registros")
            else:
                for i in datos["estudiantes"]:
                    print(f"[{i['codigo']}] - [{i['nombre']}] - (Promedio: {i['promedio']})")
        
        elif opc == 6:
            print("Saliendo del programa....")
            break
        else:
            print("Opción no válida. Vuelva a intentarlo.")


menu()


#print(validar_promedio_decimal("Hola: "))
#print(codigo_unico("hola: "))
#print(validar_digitos("hola"))
#print(validar_codigo_numero("Ingresa codigo: "))
#print(validar_codigo_letra("Ingrese código: "))
#print(validar_genero("Ingrese su género: "))
#print(valida_numero_entero_positivo("Ingresa un número"))
#print(validar_edad("Ingrese su edad: "))
#print(validar_nombre("Ingrese su nombre"))
