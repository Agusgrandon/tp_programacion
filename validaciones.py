def validar_numero(mensaje_solicitud, minimo, maximo):
    """
    Valida que sea un número válido y esté dentro del rango permitido.

    Descarta textos vacíos o con puntos mal ubicados, y recorre la 
    cadena verificando que solo contenga dígitos del 0 al 9, un opcional signo 
    menos inicial y como máximo un punto decimal. Si la estructura es correcta, 
    convierte el texto a entero o flotante y controla que no supere los límites.

    Args:
        mensaje_solicitud (str): El texto que se le muestra en la consola al usuario para pedirle el dato.
        minimo (int o float): El límite más chico permitido para ese número.
        maximo (int o float): El límite más grande permitido para ese número.

    Returns:
        int o float: El número final ya verificado, convertido a su tipo real y listo para usar en los cálculos.
    """    
    estado_validacion = 0
    resultado = 0
    
    digitos_permitidos = "0123456789"
    
    while estado_validacion == 0:
        entrada = input(mensaje_solicitud)
        
        if entrada == "":
            print("❌ Error: Ingrese un número válido (no puede estar vacío).")
        elif entrada[0] == '.' or entrada[len(entrada) - 1] == '.':
            print("❌ Error: Formato numérico incorrecto (no puede empezar ni terminar con punto).")
        else:
            puntos = 0
            es_valido = True
            tiene_menos = False
            
            if entrada[0] == '-':
                tiene_menos = True
                if len(entrada) == 1:
                    es_valido = False
            
            inicio = 0
            if tiene_menos == True:
                inicio = 1
                
            for i in range(inicio, len(entrada)):
                caracter = entrada[i]
                if caracter == '.':
                    puntos += 1
                else:
                    es_un_digito = False
                    for j in range(len(digitos_permitidos)):
                        if caracter == digitos_permitidos[j]:
                            es_un_digito = True
                    
                    if es_un_digito == False:
                        es_valido = False
            
            if es_valido == False or puntos > 1:
                print("❌ Error: Ingrese un número válido (entero o decimal sin letras).")
            else:
                if puntos == 1:
                    numero = float(entrada)
                else:
                    numero = int(entrada)
                
                if numero < minimo or numero > maximo:
                    print(f"❌ Error: El valor debe estar entre {minimo} y {maximo}.")
                else:
                    resultado = numero
                    estado_validacion = 1
                    
    return resultado


def validar_texto(mensaje_solicitud, tipo_validacion, largo_minimo=5):
    """
    Pide un texto por teclado y revisa carácter por carácter que cumpla las reglas
    según si estamos guardando el nombre del administrador o del servidor.

    Usa un while para controlar que la entrada no esté vacía ni tenga solo espacios. Dependiendo 
    del tipo de validación, arma una lista de caracteres permitidos para filtrar símbolos raros 
    y se asegura de que el texto tenga contenido real (letras o números) y pase el largo mínimo.

    Args:
        mensaje_solicitud (str): El texto para pedirle el dato al usuario.
        tipo_validacion (str): Puede ser "admin" (solo letras) o "servidor" (letras, números y guiones).
        largo_minimo (int, opcional): La cantidad mínima de caracteres. Por defecto es 5.

    Returns:
        str: El texto ya verificado y limpio listo para usar.
    """
    estado_validacion = 0
    resultado = ""
    
    # Definimos los caracteres permitidos según el tipo de validación
    if tipo_validacion == "admin":
        caracteres_validos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúÁÉÍÓÚñÑ "
    else:  # si es "servidor"
        caracteres_validos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_ "
        
    while estado_validacion == 0:
        entrada = input(mensaje_solicitud)
        
        if entrada == "":
            print("❌ Error: El campo no puede estar vacío.")
        else:
            solo_espacios = True
            tiene_contenido_real = False
            caracteres_raros = False
            
            for i in range(len(entrada)):
                caracter = entrada[i]
                
                if caracter != " ":
                    solo_espacios = False
                    
                # Chequeo manual contra la lista de caracteres que elegimos arriba
                es_valido = False
                for j in range(len(caracteres_validos)):
                    if caracter == caracteres_validos[j]:
                        es_valido = True
                
                if es_valido == False:
                    caracteres_raros = True
                
                # Definimos qué se considera "contenido real" para no aceptar puros símbolos
                if tipo_validacion == "admin":
                    if es_valido == True and caracter != " ":
                        tiene_contenido_real = True
                else: # para servidor, el contenido real son letras o números (no espacios ni guiones)
                    if es_valido == True and caracter != " " and caracter != "-" and caracter != "_":
                        tiene_contenido_real = True
            
            # Mensajes de error centralizados
            if solo_espacios == True:
                print("❌ Error: El campo no puede contener solo espacios.")
            elif caracteres_raros == True:
                if tipo_validacion == "admin":
                    print("❌ Error: El nombre del administrador solo puede contener letras y espacios.")
                else:
                    print("❌ Error: El nombre del servidor contiene símbolos no permitidos.")
            elif tiene_contenido_real == False:
                if tipo_validacion == "admin":
                    print("❌ Error: El nombre debe contener letras reales.")
                else:
                    print("❌ Error: El nombre del servidor no puede ser solo guiones o símbolos.")
            elif len(entrada) <= largo_minimo:
                print(f"❌ Error: El texto debe tener más de {largo_minimo} caracteres.")
            else:
                resultado = entrada
                estado_validacion = 1
                
    return resultado


def validar_opcion_cerrada(mensaje_solicitud, opciones_validas):
    """
    Pide un dato por teclado y revisa que coincida exactamente con alguna de las
    opciones fijas que le pasamos en una lista.

    Usa un while para insistir hasta que el usuario elija bien. Adentro, recorre la 
    lista de opciones válidas una por una usando sus índices para chequear si lo que 
    se ingresó pertenece al grupo permitido. Si no coincide con ninguna, te tira el error.

    Args:
        mensaje_solicitud (str): El texto para pedirle la opción al usuario.
        opciones_validas (list): La lista de textos válidos (ej: ["activo", "inactivo"]).

    Returns:
        str: La opción ya validada que eligió el usuario.
    """
    estado_validacion = 0
    resultado = ""
    
    while estado_validacion == 0:
        entrada = input(mensaje_solicitud)
        
        pertenece = False
        for i in range(len(opciones_validas)):
            if entrada == opciones_validas[i]:
                pertenece = True
                
        if pertenece == True:
            resultado = entrada
            estado_validacion = 1
        else:
            print("❌ Error: Opción no válida.")
            
    return resultado