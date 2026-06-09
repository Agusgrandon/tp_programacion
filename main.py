from inputs import recolectar_datos
from calculos import calcular_indicadores
from reglas import evaluar_sistema
from output import mostrar_diagnostico

def ejecutar_sistema():

    # Solicitud y validación de datos
    
    cpu, ram, espacio_libre, usuarios, procesos, firewall, tipo_srv, nom_srv, admin = recolectar_datos()
    
    # Cálculos
    carga, presion, recursos = calcular_indicadores(cpu, ram, usuarios, procesos, espacio_libre)
    
    # Evaluación de reglas
    estado = evaluar_sistema(cpu, ram, espacio_libre, usuarios, procesos, firewall, tipo_srv, carga, presion, recursos)
    
    # Generación de alertas y visualización del diagnóstico
    mostrar_diagnostico(nom_srv, admin, estado, cpu, ram, espacio_libre, firewall, usuarios, procesos)
    
ejecutar_sistema()

