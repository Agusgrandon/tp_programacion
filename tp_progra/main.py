def procesar_datos(cpu, ram, espacio_libre_gb, us_conectados, procesos_activos, estado_firewall, servidor, nombre_servidor, administrador):
    
    #calculos
    carga_total = (cpu + ram) / 2
    presion_sistema = us_conectados + procesos_activos
    recursos_disponibles = espacio_libre_gb - (procesos_activos * 0.3)
    
    if cpu > 85 and ram > 80 and estado_firewall == "inactivo":
        estado_de_la_computadora = "estado critico"
    elif us_conectados > 1000 or procesos_activos > 1000:
        estado_de_la_computadora = "sistema saturado"
    elif (servidor == "web" or servidor == "Web") and us_conectados > 100 and cpu > 75:
        estado_de_la_computadora = "alta demanda"
    elif espacio_libre_gb < 10 or procesos_activos > 50:
        estado_de_la_computadora = "el disco esta casi lleno"
    elif presion_sistema > 1000 and recursos_disponibles < 20 and ram < 10:
        estado_de_la_computadora = "sistema muy bajo"
    elif carga_total > 60 or presion_sistema > 100: 
        estado_de_la_computadora = "riesgo alto"
    elif not (servidor == "web" or servidor == "Web") and us_conectados < 50:
        estado_de_la_computadora = "baja demanda"
    else:
        estado_de_la_computadora = "computadora bien"

    match estado_de_la_computadora:
        case "estado critico":
            mensaje = (f"-- Diagnostico del servidor {nombre_servidor} --\n"
                       f"Administrador: {administrador}\n"
                       f"Estado general: {estado_de_la_computadora}\n"
                       f"Problemas detectados: el firewall esta inactivo, te sugerimos activarlo de inmediato")
        case "eistema saturado":
            mensaje = (f"-- Diagnostico del servidor {nombre_servidor} --\n"
                       f"Administrador: {administrador}\n"
                       f"Estado general: {estado_de_la_computadora}\n"
                       f"Problemas detectados: el sistema esta saturado, te sugerimos aguardar")
        case "elta demanda":
            mensaje = (f"-- Diagnostico del servidor {nombre_servidor} --\n"
                       f"Administrador: {administrador}\n"
                       f"Estado general: {estado_de_la_computadora}\n"
                       f"Problemas detectados: hay alta demanda en el servidor, intentalo mas tarde")
        case "el disco esta casi lleno":
            mensaje = (f"-- Diagnostico del servidor {nombre_servidor} --\n"
                       f"Administrador: {administrador}\n"
                       f"Estado general: {estado_de_la_computadora}\n"
                       f"Problemas detectados: el disco se encuentra lleno, te sugerimos liberar espacio")
        case "sistema muy bajo":
            mensaje = (f"-- Diagnostico del servidor {nombre_servidor} --\n"
                       f"Administrador: {administrador}\n"
                       f"Estado general: {estado_de_la_computadora}\n"
                       f"Problemas detectados: sobrecarga, te sugerimos monitorear cada una hora")
        case "riesgo alto":
            mensaje = (f"-- Diagnostico del servidor {nombre_servidor} --\n"
                       f"Administrador: {administrador}\n"
                       f"Estado general: {estado_de_la_computadora}\n"
                       f"Problemas detectados: riesgo alto")
        case "baja demanda":
            mensaje = (f"-- Diagnostico del servidor {nombre_servidor} --\n"
                       f"Administrador: {administrador}\n"
                       f"Estado general: {estado_de_la_computadora}\n"
                       f"Hay poca demanda, podes usar con normalidad tu compu!")
        case _:
            mensaje = (f"-- Diagnostico del servidor {nombre_servidor} --\n"
                       f"Administrador: {administrador}\n"
                       f"Estado general: {estado_de_la_computadora}\n"
                       f"Problemas detectados: tu compu esta ok, la podes usar!")

    return mensaje

cpu = int(input("Ingrese % de uso de CPU: "))
while cpu < 0:
    cpu = int(input("Error, el numero ingresado no es correcto, reingresalo: "))

ram = int(input("Ingrese % de memoria RAM: "))
while ram < 0:
    ram = int(input("Error, el numero ingresado no es correcto, reingresalo: "))

espacio_libre_gb = int(input("Espacio libre en disco: "))
while espacio_libre_gb < 0:
    espacio_libre_gb = int(input("Error, el numero ingresado no es correcto, reingresalo: "))

us_conectados = int(input("Informe los usuarios conectados: "))
while us_conectados < 0:
    us_conectados = int(input("Error, el numero ingresado no es correcto, reingresalo: "))

procesos_activos = int(input("Ingrese cantidad de procesos activos: "))
while procesos_activos < 0:
    procesos_activos = int(input("Error, el numero ingresado no es correcto, reingresalo: "))

sistema_operativo = input("informe el sistema operativo, Linux/Windows Server: ")
while sistema_operativo != "linux" and sistema_operativo != "windows server":
    sistema_operativo = input("Error, reingresa el sistema operativo (linux / windows server): ")

estado_firewall = input("Estado Firewall: Activo/Inactivo: ")
while estado_firewall != "activo" and estado_firewall != "inactivo":
    estado_firewall = input("Error, informa nuevamente el estado del firewall (activo / inactivo): ")

servidor = input("Informe el servidor: Web / Base de datos / Archivos: ")
while servidor != "web" and servidor != "Web" and servidor != "base de datos" and servidor != "archivos":
    servidor = input("Error, informa nuevamente el tipo de servidor (web / base de datos / archivos): ")

nombre_servidor = input("Nombre del servidor: ")
while nombre_servidor == "":
    nombre_servidor = input("Error, ingresa nuevamente el nombre del servidor: ")

nombre_administrador = input("Nombre del administrador responsable: ")
while nombre_administrador == "":
    nombre_administrador = input("Error, ingresa nuevamente el nombre del administrador: ")

variable_a = procesar_datos(cpu, ram, espacio_libre_gb, us_conectados, procesos_activos, estado_firewall, servidor, nombre_servidor, nombre_administrador)
print(variable_a)



