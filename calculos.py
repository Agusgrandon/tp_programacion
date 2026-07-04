def calcular_indicadores(servidor:dict) -> dict:
    """Calcula los indicadores derivados para el motor de decisiones.
    Args:
        cpu              (float): Uso de CPU en porcentaje (0-100).
        ram              (float): Uso de RAM en porcentaje (0-100).
        us_conectados    (int)  : Cantidad de usuarios conectados al servidor.
        procesos_activos (int)  : Cantidad de procesos corriendo en el sistema.
        espacio_libre_gb (float): Espacio libre en disco en gigabytes.
    Returns:
        carga_total          (float): Promedio entre CPU y RAM.
        presion_sistema      (int)  : Suma de usuarios y procesos. 
        recursos_disponibles (float): Espacio libre ajustado por el consumo estimado de procesos.
    """
    cpu = servidor["recursos"]["cpu"]
    ram = servidor["recursos"]["ram"]
    espacio_libre_gb = servidor["recursos"]["espacio_libre"]
    us_conectados = servidor["recursos"]["usuarios"]
    procesos_activos = servidor["recursos"]["procesos"]

    carga_total = (cpu + ram) / 2
    presion_sistema = us_conectados + procesos_activos
    recursos_disponibles = espacio_libre_gb - (procesos_activos * 0.3)

    servidor["indicadores"]["carga_total"] = carga_total
    servidor["indicadores"]["presion_sistema"] = presion_sistema
    servidor["indicadores"]["recursos_disponibles"] = recursos_disponibles
    
    return servidor