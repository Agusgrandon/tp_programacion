def mostrar_diagnostico(nombre_servidor, nombre_administrador, estado_de_la_computadora, cpu, ram, espacio_libre_gb, estado_firewall, us_conectados, procesos_activos):
    """Muestra el reporte final combinando el Estado General.

    Args:
        nombre_servidor (str): Nombre del servidor.
        nombre_administrador (str): Nombre del administrador.
        estado_de_la_computadora (str): Estado general de la computador.
        cpu (float): Porcentaje de uso del procesador.
        ram (float): Porcentaje de uso de la memoria RAM.
        espacio_libre_gb (float): Espacio libre disponible en disco, en GB.
        estado_firewall (str): Estado del firewall ("activo" o "inactivo").
        us_conectados (int): Cantidad de usuarios conectados al servidor.
        procesos_activos (int): Cantidad de procesos activos en ejecución.

    Returns:
        None. La función únicamente muestra información por pantalla.
    """
    
    print("\n" + "="*50)
    print(f"💻 Diagnóstico del Servidor: {nombre_servidor}")
    print(f"👤 Administrador responsable: {nombre_administrador}")
    # Este toma el texto en mayúscula que calculó tu reglas.py (ej: "ESTADO CRÍTICO")
    print(f"📊 Estado general: {estado_de_la_computadora}")
    print("-" * 50)
    
    # ACÁ MUESTRA TODOS LOS PROBLEMAS DETECTADOS
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
        
    print("") 
    
    # ACÁ MUESTRA LAS RECOMENDACIONES
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
        print(" ✓ Tu compu esta ok, la podes usar! 🎉")
        
    print("="*50 + "\n")