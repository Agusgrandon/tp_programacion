import json

def cargar_json(nombre_archivo, key) -> dict:
    """Carga la informacion almacenada en un archivo JSON.

    Args:
        nombre_archivo (str): Nombre del archivo JSON que se desea abrir.
        key (str): Clave principal del diccionario que se desea obtener.

    Returns:
        dict: Diccionario con los datos almacenados bajo la clave indicada.
    """
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)
    return(data[key])

def guardar_datos(alumnos:dict) -> None:
    """Guarda los datos de los alumnos en el archivo JSON.

    Args:
        alumnos (dict): Diccionario que contiene la información de los alumnos.
    
    Returns:
        None: La función no devuelve ningún valor.
    """
    with open("data/alumnos.json", "w", encoding="utf-8") as archivo:
        json.dump({"alumnos": alumnos}, archivo, indent=4)