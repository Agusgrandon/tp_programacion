def calcular_indicadores(servidor:dict) -> dict:
    """Calcula los indicadores derivados para el motor de decisiones.
    
    Args:
        servidor (dict): Diccionario con la información completa del servidor. 
                         Debe contener la clave 'recursos' con los datos de 
                         cpu, ram, espacio_libre, usuarios y procesos.
                         
    Returns:
        dict: El mismo diccionario recibido, pero con la clave 'indicadores' 
              actualizada con los tres nuevos valores calculados.
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