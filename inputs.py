from validaciones import validar_numero, validar_texto, validar_opcion_cerrada

def recolectar_datos() -> dict:
    """
    Solicita y valida todos los datos de entrada del servidor al usuario.
    Args:
        No recibe parámetros. Los datos se obtienen mediante input() con validación.
    Returns:
        tupled
    """
    # Listas de opciones permitidas
    opciones_so = ["linux", "windows server"]
    opciones_firewall = ["activo", "inactivo"]
    opciones_servidor = ["web", "Web", "base de datos", "archivos"]

    # Introducción de datos con validaciones numéricas
    cpu = validar_numero("Ingrese % de uso de CPU (0-100): ", 0, 100)
    ram = validar_numero("Ingrese % de memoria RAM (0-100): ", 0, 100)
    espacio_libre_gb = validar_numero("Ingrese espacio libre en disco en GB (0-10000): ", 0, 10000)
    us_conectados = validar_numero("Ingrese cantidad de usuarios conectados: ", 0, 100000)
    procesos_activos = validar_numero("Ingrese cantidad de procesos activos: ", 0, 50000)
    
    # Introducción de opciones según las opciones de las listas
    sistema_operativo = validar_opcion_cerrada("Ingrese sistema operativo (linux / windows server): ", opciones_so)
    estado_firewall = validar_opcion_cerrada("Ingrese estado del firewall (activo / inactivo): ", opciones_firewall)
    tipo_servidor = validar_opcion_cerrada("Ingrese tipo de servidor (web / base de datos / archivos): ", opciones_servidor)
    
    # Introducción de datos con validación de cadenas de texto
    nombre_servidor = validar_texto("Ingrese el nombre del servidor: ", "servidor")
    nombre_administrador = validar_texto("Ingrese el nombre del administrador responsable: ", "admin")

    servidor = {

        "configuracion": {

            "nombre": nombre_servidor,
            "administrador": nombre_administrador,
            "sistema_operativo": sistema_operativo,
            "tipo": tipo_servidor,
            "firewall": estado_firewall

        },

        "recursos": {

            "cpu": cpu,
            "ram": ram,
            "espacio_libre": espacio_libre_gb,
            "usuarios": us_conectados,
            "procesos": procesos_activos

        },

        "indicadores": {

            "carga_total": 0,
            "presion_sistema": 0,
            "recursos_disponibles": 0

        },

        "diagnostico": {

            "estado": ""

        }

    }
    
    return servidor

def modificar_configuracion(servidor: dict) -> dict:
    """
    Permite modificar la configuración del servidor.
    El usuario selecciona qué dato desea modificar. Luego se solicita el
    nuevo valor utilizando la validación correspondiente y se actualiza el
    diccionario del servidor.

    Args:
        servidor (dict): Diccionario que contiene la información del servidor.

    Returns:
        dict: Diccionario del servidor con la información actualizada.
    """

    print("\n========== MODIFICAR CONFIGURACIÓN ==========")
    print("1 - Nombre del servidor")
    print("2 - Nombre del administrador")
    print("3 - Sistema operativo")
    print("4 - Tipo de servidor")
    print("5 - Estado del firewall")
    print("6 - CPU")
    print("7 - RAM")
    print("8 - Espacio libre")
    print("9 - Usuarios conectados")
    print("10 - Procesos activos")

    opcion = input("\nIngrese una opción: ")

    opciones_so = ["linux", "windows server"]
    opciones_firewall = ["activo", "inactivo"]
    opciones_servidor = ["web", "Web", "base de datos", "archivos"]

    match opcion:

        case "1":
            servidor["configuracion"]["nombre"] = validar_texto("Ingrese el nuevo nombre del servidor: ", "servidor")

        case "2":
            servidor["configuracion"]["administrador"] = validar_texto("Ingrese el nuevo nombre del administrador: ", "admin")

        case "3":
            servidor["configuracion"]["sistema_operativo"] = validar_opcion_cerrada("Ingrese el sistema operativo: ", opciones_so)

        case "4":
            servidor["configuracion"]["tipo"] = validar_opcion_cerrada("Ingrese el tipo de servidor: ", opciones_servidor)

        case "5":
            servidor["configuracion"]["firewall"] = validar_opcion_cerrada("Ingrese el estado del firewall: ", opciones_firewall)

        case "6":
            servidor["recursos"]["cpu"] = validar_numero("Ingrese el nuevo porcentaje de CPU: ", 0, 100)

        case "7":
            servidor["recursos"]["ram"] = validar_numero("Ingrese el nuevo porcentaje de RAM: ", 0, 100)

        case "8":
            servidor["recursos"]["espacio_libre"] = validar_numero("Ingrese el nuevo espacio libre en GB: ", 0, 10000)

        case "9":
            servidor["recursos"]["usuarios"] = validar_numero("Ingrese la nueva cantidad de usuarios conectados: ", 0, 100000)

        case "10":
            servidor["recursos"]["procesos"] = validar_numero("Ingrese la nueva cantidad de procesos activos: ", 0, 50000)

        case _:
            print("La opción ingresada no es válida.")

    return servidor