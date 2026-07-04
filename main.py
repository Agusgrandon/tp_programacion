from inputs import recolectar_datos
from calculos import calcular_indicadores
from reglas import evaluar_sistema
from output import mostrar_diagnostico
from archivos import cargar_json

servidor = cargar_json("servidor.json", "servidor")

def ejecutar_sistema():
    """Esta es la función principal que maneja todo el flujo del programa.
    
    Básicamente, lo que hace es organizar y llamar en orden a las demás etapas:
    1. Primero te pide y valida todos los datos del servidor (como la CPU, RAM, etc.).
    2. Después, con esos datos, hace las cuentas matemáticas para sacar los indicadores.
    3. Con esos números listos, pasa toda la info por el sistema de reglas para ver el estado de salud del servidor.
    4. Por último, arma las alertas en pantalla y le muestra el diagnóstico completo al administrador.

    Llama a estas funciones:
        - recolectar_datos()
        - calcular_indicadores()
        - evaluar_sistema()
        - mostrar_diagnostico()
    """
    


    # Solicitud y validación de datos
    cpu, ram, espacio_libre, usuarios, procesos, firewall, tipo_srv, nom_srv, admin = recolectar_datos()
    
    # Cálculos
    carga, presion, recursos = calcular_indicadores(cpu, ram, usuarios, procesos, espacio_libre)
    
    # Evaluación de reglas
    estado = evaluar_sistema(cpu, ram, espacio_libre, usuarios, procesos, firewall, tipo_srv, carga, presion, recursos)
    
    # Generación de alertas y visualización del diagnóstico
    mostrar_diagnostico(nom_srv, admin, estado, cpu, ram, espacio_libre, firewall, usuarios, procesos)
    
ejecutar_sistema()

