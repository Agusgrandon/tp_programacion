def procesar_datos(cpu, ram, espacio_libre_gb, us_conectados, procesos_activos, estado_firewall):
    #8 condiciones minimas
    #calculo 1: carga total
    carga_total = (cpu + ram) / 2

    #calculo 2: nivel estimado de riesgo
    presion_sistema = us_conectados + procesos_activos

    #calculo 3:
    recursos_disponibles = espacio_libre_gb - (procesos_activos * 0.3)
    
    #regla 1
    if not estado_firewall == "Inactivo": #aca faltarian 2 variables más?
        print("Computadora segura")

    #regla 2
    if cpu > 85 and ram > 80 and estado_firewall == "Inactivo":
        print("Estado critico")

    #regla 3
    if us_conectados > 1000 or procesos_activos > 1000:
        print("Sistema saturado")

    #regla 4
    if servidor == "Web" and us_conectados > 100 and cpu > 75:
        print("Alta demanda")

    return procesar_datos

cpu = int(input("Ingrese % de uso de CPU: "))
while cpu < 0:
    cpu = int(input("Error, el numero ingresado no es correcto, reingresalo: "))

ram = int(input("Ingrese % de memoria RAM: "))
while ram < 0:
    ram = int(input("Error, el numero ingresado no es correcto, reingresalo: "))

espacio_libre_gb = int(input("Espacio libre en disco: "))
while espacio_libre_gb < 0:
    espacio_libre_gb = int(input("Error, el numero ingresado no es correcto, reingresalo: "))

us_conectados = int(input("Us. conectados"))
while us_conectados < 0:
    us_conectados = int(input("Error, el numero ingresado no es correcto, reingresalo: "))

procesos_activos = int(input("Ingrese cantidad de procesos activos: "))
while procesos_activos < 0:
    procesos_activos = int(input("Error, el numero ingresado no es correcto, reingresalo: "))

sistema_operativo = input("Linux / Windows Server")
while sistema_operativo != "linux" and sistema_operativo != "windows server":
    sistema_operativo = input("Error, reingresa el sistema operativo (linux / windows server): ")

estado_firewall = input("Activo / Inactivo")
while estado_firewall != "activo" and estado_firewall != "inactivo":
    estado_firewall = input("Error, informa nuevamente el estado del firewall (activo / inactivo): ")

servidor = input("(Web / Base de datos / Archivos")
while servidor != "web" and servidor != "base de datos" and servidor != "archivos":
    servidor = input("Error, informa nuevamente el tipo de servidor (web / base de datos / archivos): ")

nombre_servidor = input("Nombre del servidor: ")
while nombre_servidor == "":
    nombre_servidor = input("Error, ingresa nuevamente el nombre del servidor: ")

nombre_administrador = input("Nombre del administrador responsable: ")
while nombre_administrador == "":
    nombre_administrador = input("Error, ingresa nuevamente el nombre del administrador: ")

variable_a = procesar_datos ()



