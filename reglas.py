def regla_sobrecarga(cpu, ram, estado_firewall):
    return cpu > 85 and ram > 80 and estado_firewall == "inactivo"

def regla_saturado(us_conectados, procesos_activos):
    return us_conectados > 1000 or procesos_activos > 1000

def regla_muy_bajo(presion_sistema, recursos_disponibles, ram):
    return presion_sistema > 1000 and recursos_disponibles < 20 and ram < 10

def regla_alta_demanda(servidor, us_conectados, cpu):
    return (servidor == "web" or servidor == "Web") and us_conectados > 100 and cpu > 75

def regla_riesgo_alto(carga_total, presion_sistema):
    return carga_total > 60 or presion_sistema > 100

def regla_disco_lleno(espacio_libre_gb, procesos_activos):
    return espacio_libre_gb < 10 or procesos_activos > 50

def regla_baja_demanda(servidor, us_conectados):
    return not (servidor == "web" or servidor == "Web") and us_conectados < 50

def regla_firewall_alerta(estado_firewall, us_conectados):
    return estado_firewall == "inactivo" and us_conectados > 0

def evaluar_sistema(servidor:dict) -> dict:
    """Evalúa las micro-reglas.
        
    Args: 
        servidor (dict): Diccionario con la información del servidor.
    
    Returns:
        dict. 
    """
    cpu = servidor["recursos"]["cpu"]
    ram = servidor["recursos"]["ram"]
    espacio_libre_gb = servidor["recursos"]["espacio_libre"]
    us_conectados = servidor["recursos"]["usuarios"]
    procesos_activos = servidor["recursos"]["procesos"]

    estado_firewall = servidor["configuracion"]["firewall"]
    tipo_servidor = servidor["configuracion"]["tipo"]

    carga_total = servidor["indicadores"]["carga_total"]
    presion_sistema = servidor["indicadores"]["presion_sistema"]
    recursos_disponibles = servidor["indicadores"]["recursos_disponibles"]
    
    if regla_sobrecarga(cpu, ram, estado_firewall):
        estado_de_la_computadora = "Esta computadora esta en estado critico"
        
    elif regla_saturado(us_conectados, procesos_activos):
        estado_de_la_computadora = "Esta computadora esta en estado saturado"
        
    elif regla_muy_bajo(presion_sistema, recursos_disponibles, ram):
        estado_de_la_computadora = "Esta computadora esta con un sistema muy bajo"
        
    elif regla_alta_demanda(tipo_servidor, us_conectados, cpu):
        estado_de_la_computadora = "Esta computadora esta con alta demanda"
        
    elif regla_riesgo_alto(carga_total, presion_sistema):
        estado_de_la_computadora = "Esta computadora tiene alto riesgo"
        
    elif regla_disco_lleno(espacio_libre_gb, procesos_activos):
        estado_de_la_computadora = "Esta computadora tiene el disco lleno"
        
    elif regla_baja_demanda(tipo_servidor, us_conectados):
        estado_de_la_computadora = "Esta computadora tiene baja demanda"

    elif regla_firewall_alerta(estado_firewall, us_conectados):
        estado_de_la_computadora = "Esta computadora tiene el firewall inactivo, te recomendamos activarlo"     
    else:
        estado_de_la_computadora = "La compu esta bien"
    
    servidor["diagnostico"]["estado"] = estado_de_la_computadora

    return servidor
    
