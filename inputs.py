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
    servidor = validar_opcion_cerrada("Ingrese tipo de servidor (web / base de datos / archivos): ", opciones_servidor)
    
    # Introducción de datos con validación de cadenas de texto
    nombre_servidor = validar_texto("Ingrese el nombre del servidor: ", "servidor")
    nombre_administrador = validar_texto("Ingrese el nombre del administrador responsable: ", "admin")

    servidor = {

        "configuracion": {

            "nombre": nombre_servidor,
            "administrador": nombre_administrador,
            "sistema_operativo": sistema_operativo,
            "tipo": servidor,
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