cpu = int(input("Ingrese % de uso de CPU: "))
ram = int(input("Ingrese % de memoria RAM: "))
espacio_libre_gb = int(input("Espacio libre en disco: "))
us_conectados = int(input("Us. conectados"))
procesos_activos = int(input("Ingrese cantidad de procesos activos: "))

sistema_operativo = input("Linux / Windows Server")
estado_firewall = input("Activo / Inactivo")
servidor = input("(Web / Base de datos / Archivos")

nombre_servidor = input("Nombre del servidor: ")
nombre_administrador = input("Nombre del administrador responsable: ")

#8 condiciones minimos

#regla 1: carga total
carga_total = (cpu + ram) / 2

#regla 2: nivel estimado de riesgo