def calcular_indicadores(cpu, ram, us_conectados, procesos_activos, espacio_libre_gb):
    """Calcula los indicadores derivados para el motor de decisiones."""
    carga_total = (cpu + ram) / 2
    presion_sistema = us_conectados + procesos_activos
    recursos_disponibles = espacio_libre_gb - (procesos_activos * 0.3)
    
    return carga_total, presion_sistema, recursos_disponibles