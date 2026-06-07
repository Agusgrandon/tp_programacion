def validar_numero(mensaje_solicitud, minimo, maximo):
    """Valida que la entrada sea un número entero o decimal válido dentro del rango."""
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
    Valida cadenas de caracteres reutilizando la misma estructura básica.
    tipo_validacion puede ser: "admin" (solo letras) o "servidor" (letras, números y guiones).
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
    """Valida si el texto ingresado pertenece al conjunto permitido usando índices."""
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