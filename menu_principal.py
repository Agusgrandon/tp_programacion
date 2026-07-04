from inputs import recolectar_datos, modificar_configuracion
from calculos import calcular_indicadores
from reglas import evaluar_sistema
from output import mostrar_diagnostico, mostrar_configuracion, mostrar_menu_principal, mostrar_ejecutar_diagnostico
from archivos import cargar_json, guardar_datos



def ejecutar_sistema() -> None:
    """
    Ejecuta el menú principal del sistema de diagnóstico de servidores.

    Al iniciar el programa intenta cargar la configuración almacenada en el
    archivo JSON. Si no existe información, solicita al usuario el ingreso
    de una nueva configuración.

    Luego mantiene un menú interactivo que permite visualizar, modificar,
    diagnosticar y guardar la información del servidor.
    """

    servidor = cargar_json("data/servidor.json", "servidor")

    if servidor == {}:
        print("No existe una configuración guardada.")
        print("Debe ingresar los datos del servidor.\n")

        servidor = recolectar_datos()

        guardar_datos(servidor)

    continuar = True

    while continuar == True:

        mostrar_menu_principal()

        opcion = input("\nIngrese una opción: ")

        match opcion:

            case "1":
                mostrar_configuracion(servidor)
            case "2":
                modificar_configuracion(servidor)
            case "3":
                servidor = calcular_indicadores(servidor)
                servidor = evaluar_sistema(servidor)
                mostrar_ejecutar_diagnostico(servidor)
            case "4":
                mostrar_diagnostico(servidor)
            case "5":
                guardar_datos(servidor)
                print("\nConfiguración guardada correctamente.")
            case "6":
                continuar = False
                print("\nHasta luego.")
            case _:
                print("\nLa opción ingresada no es válida.")
