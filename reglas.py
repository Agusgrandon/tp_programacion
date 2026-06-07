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


def evaluar_sistema(cpu, ram, espacio_libre_gb, us_conectados, procesos_activos, estado_firewall, servidor, carga_total, presion_sistema, recursos_disponibles):
    """Evalúa las micro-reglas."""
    
    if regla_sobrecarga(cpu, ram, estado_firewall):
        return "ESTADO CRÍTICO"
        
    elif regla_saturado(us_conectados, procesos_activos):
        return "SISTEMA SATURADO"
        
    elif regla_muy_bajo(presion_sistema, recursos_disponibles, ram):
        return "SISTEMA MUY BAJO"
        
    elif regla_alta_demanda(servidor, us_conectados, cpu):
        return "ALTA DEMANDA"
        
    elif regla_riesgo_alto(carga_total, presion_sistema):
        return "RIESGO ALTO"
        
    elif regla_disco_lleno(espacio_libre_gb, procesos_activos):
        return "EL DISCO ESTA CASI LLENO"
        
    elif regla_baja_demanda(servidor, us_conectados):
        return "BAJA DEMANDA"
        
    else:
        return "COMPUTADORA BIEN"