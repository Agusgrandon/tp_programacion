## 🖥️ Sistema de Diagnóstico y Configuración de Servidor
### *Trabajo Práctico Integrador - Sprint 3 (Persistencia de Datos)*

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![UTN](https://img.shields.io/badge/UTN-Avellaneda-red)
![Materia](https://img.shields.io/badge/Materia-Programacion%201-orange)
![Sprint](https://img.shields.io/badge/Sprint-3-green)
![Estado](https://img.shields.io/badge/Estado-Terminado-brightgreen)

## 📋 Descripción General
[cite_start]Evolución del sistema de monitoreo por consola desarrollado en Python[cite: 14]. El sistema permite procesar las variables técnicas de un servidor, evaluar un motor de micro-reglas lógicas y generar un diagnóstico de salud del entorno. 

[cite_start]Para este tercer sprint, el núcleo del proyecto se transformó para integrar la **organización de la información mediante diccionarios anidados** y la **persistencia de datos en archivos físicos**, permitiendo que la configuración configurada se conserve entre diferentes ejecuciones del programa[cite: 19].

## 💡 Materia
[cite_start]Programación 1 - UTN Avellaneda [cite: 1, 4]

## 👥 Integrantes
* Agustina Grandón
* Xiomara Nicho
* Camila Velásquez

---

## 🗂️ Organización de los Diccionarios
[cite_start]Para cumplir con los requerimientos de la cátedra [cite: 30][cite_start], estructuramos toda la información en un **único diccionario centralizado con sub-diccionarios anidados**[cite: 82, 83]. [cite_start]Esta arquitectura permite segmentar las responsabilidades de los datos de forma lógica[cite: 37]:

```python
servidor = {
    "configuracion": {
        "nombre": str,            # Nombre del servidor
        "administrador": str,     # Administrador responsable
        "sistema_operativo": str, # Linux / Windows Server
        "tipo": str,              # Web / Base de datos / Archivos
        "firewall": str           # Activo / Inactivo
    },
    "recursos": {
        "cpu": float o int,       # % de uso de CPU
        "ram": float o int,       # % de uso de RAM
        "espacio_libre": float,   # GB libres en disco
        "usuarios": int,          # Cantidad de usuarios conectados
        "procesos": int           # Cantidad de procesos activos
    },
    "indicadores": {
        "carga_total": float,         # Promedio CPU y RAM
        "presion_sistema": int,       # Usuarios + procesos
        "recursos_disponibles": float # Espacio libre ajustado por procesos
    },
    "diagnostico": {
        "estado": str             # Reporte del estado del sistema
    }
}

💾 Persistencia de Datos y Formato Elegido
El sistema implementa la persistencia de datos de manera obligatoria para evitar la pérdida de información al cerrar la consola.

- Formato Seleccionado: JSON (.json).

- Justificación Técnica: Se eligió JSON frente a las opciones de TXT o CSV debido a que es el formato nativo ideal para mapear estructuras de datos complejas y anidadas (como los diccionarios de Python). Permite guardar y recuperar la configuración conservando exactamente los tipos de datos (enteros, flotantes y cadenas) y las agrupaciones lógicas sin necesidad de parsear cadenas de texto manualmente.

⚙️ Flujo Esperado del Sistema
El programa sigue estrictamente el ciclo de vida modular exigido por la cátedra:

- Inicio: El sistema busca el archivo data/servidor.json. Si lo encuentra, recupera el estado de la última sesión; si no existe, invoca de forma automática la recolección inicial de datos.

- Interfaz Principal: Despliega un menú interactivo de 6 opciones para administrar las operaciones.

- Validación Exhaustiva: Cada dato modificado o cargado es sanitizado mediante escaneos carácter por carácter.

- Procesamiento y Reglas: Se calculan las métricas derivadas y se evalúan secuencialmente las micro-reglas para inyectar el diagnóstico en la estructura.

- Guardado Manual: La opción 5 escribe el estado actual del diccionario en el archivo JSON de manera definitiva.

📦 Estructura del Proyecto (Módulos)
El proyecto se dividió en archivos independientes para garantizar la modularización y el principio de responsabilidad única:

- main.py: El punto de entrada del programa que simplemente inicializa el sistema.

- menu_principal.py: Controlador central que gestiona el bucle while de la aplicación y conecta las distintas etapas.

- archivos.py: Contiene las funciones de bajo nivel que manejan la apertura, lectura (json.load) y escritura (json.dump) del archivo persistente con la cláusula with.

- inputs.py: Orquesta los procesos de recolección de información inicial y la lógica del menú de modificaciones (match-case).

- validaciones.py: Aloja las funciones algorítmicas de control desarrolladas en el Sprint 2 para números, textos y opciones cerradas.

- calculos.py: Procesa las operaciones matemáticas para hallar la carga, presión y disponibilidad del sistema.

- reglas.py: Contiene las 8 micro-reglas de diagnóstico técnico y la función evaluadora.

- output.py: Encargado exclusivo de las impresiones estéticas, visualización de menús, reportes y formateo con f-strings.

🧠 Restricciones Técnicas Respetadas
Este proyecto mantiene los lineamientos académicos estrictos de la cursada:

- Recorrido manual con bucles for basados en índices e iteraciones explícitas.

- Sin uso de métodos avanzados de filtrado de colecciones.

- Sin comprensiones de listas.

- Funciones parametrizadas y modulares con alcance acotado.

- Documentación mediante tipado de datos (Type Hints) y Docstrings cortos estilo Google en todas las funciones.