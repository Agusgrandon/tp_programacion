def mostrar_configuracion(servidor: dict) -> None:
    """
    Muestra la configuración actual del servidor.

    Args:
        servidor (dict): Diccionario con la información del servidor.

    Returns:
        None.
    """

    print("\n" + "=" * 50)
    print("CONFIGURACION DEL SERVIDOR")
    print("=" * 50)

    print(f"Nombre del servidor: {servidor['configuracion']['nombre']}")
    print(f"Administrador: {servidor['configuracion']['administrador']}")
    print(f"Sistema operativo: {servidor['configuracion']['sistema_operativo']}")
    print(f"Tipo de servidor: {servidor['configuracion']['tipo']}")
    print(f"Firewall: {servidor['configuracion']['firewall']}")

    print("-" * 50)

    print(f"CPU: {servidor['recursos']['cpu']} %")
    print(f"RAM: {servidor['recursos']['ram']} %")
    print(f"Espacio libre: {servidor['recursos']['espacio_libre']} GB")
    print(f"Usuarios conectados: {servidor['recursos']['usuarios']}")
    print(f"Procesos activos: {servidor['recursos']['procesos']}")

    print("=" * 50 + "\n")

def mostrar_diagnostico(servidor:dict):
    """Muestra el reporte final combinando el Estado General.

    Args:
        servidor (dict): Diccionario con la información del servidor.

    Returns:
        None. 
    """
    nombre_servidor = servidor["configuracion"]["nombre"]
    nombre_administrador = servidor["configuracion"]["administrador"]

    cpu = servidor["recursos"]["cpu"]
    ram = servidor["recursos"]["ram"]
    espacio_libre_gb = servidor["recursos"]["espacio_libre"]
    estado_firewall = servidor["configuracion"]["firewall"]
    procesos_activos = servidor["recursos"]["procesos"]

    estado_de_la_computadora = servidor["diagnostico"]["estado"]
    
    print("\n" + "="*50)
    print(f"💻 Diagnóstico del Servidor: {nombre_servidor}")
    print(f"👤 Administrador responsable: {nombre_administrador}")
    print(f"📊 Estado general: {estado_de_la_computadora}")
    print("-" * 50)
    print("Problemas detectados:")

    hay_problemas = False

    if cpu > 85:
        print(" - Uso de CPU elevado")
        hay_problemas = True

    if ram > 80:
        print(" - Uso de memoria RAM elevado")
        hay_problemas = True

    if estado_firewall == "inactivo":
        print(" - Firewall desactivado")
        hay_problemas = True

    if espacio_libre_gb < 10:
        print(" - Poco espacio en disco")
        hay_problemas = True

    if procesos_activos > 50:
        print(" - Sobrecarga de procesos activos")
        hay_problemas = True

    if hay_problemas == False:
        print(" - Ninguno. El sistema opera con normalidad. 🎉")

    print()

    print("Recomendaciones:")

    hay_recomendaciones = False

    if cpu > 85 or procesos_activos > 50:
        print(" ✓ Reiniciar servicios innecesarios")
        print(" ✓ Evaluar ampliación de recursos")
        hay_recomendaciones = True

    if estado_firewall == "inactivo":
        print(" ✓ Activar firewall")
        hay_recomendaciones = True

    if espacio_libre_gb < 10:
        print(" ✓ Liberar almacenamiento")
        hay_recomendaciones = True

    if hay_recomendaciones == False:
        print(" ✓ El servidor funciona correctamente. 🎉")

    print("=" * 50 + "\n")

def mostrar_menu_principal():
    print("\n" + "=" * 50)
    print(" SISTEMA DE DIAGNÓSTICO DE SERVIDORES ")
    print("=" * 50)
    print("1 - Mostrar configuración")
    print("2 - Modificar configuración")
    print("3 - Ejecutar diagnóstico")
    print("4 - Mostrar diagnóstico")
    print("5 - Guardar configuración")
    print("6 - Salir")

def mostrar_ejecutar_diagnostico(servidor: dict):
    print("\nDiagnóstico realizado correctamente.")
    print("\nIndicadores calculados:")
    print(f"Carga total: {servidor['indicadores']['carga_total']}")
    print(f"Presión del sistema: {servidor['indicadores']['presion_sistema']}")
    print(f"Recursos disponibles: {servidor['indicadores']['recursos_disponibles']}")
    print(f"\nEstado obtenido: {servidor['diagnostico']['estado']}")

def mostrar_modificar_configuración():
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