## 🖥️ Sistema de Diagnóstico y Configuración de Servidor
### *Trabajo Práctico Integrador - Sprint 2*

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![UTN](https://img.shields.io/badge/UTN-Avellaneda-red)
![Materia](https://img.shields.io/badge/Materia-Programacion%201-orange)
![Sprint](https://img.shields.io/badge/Sprint-2-green)
![Estado](https://img.shields.io/badge/Estado-Terminado-brightgreen)

## 📋 Descripción
Sistema por consola desarrollado en Python que analiza variables 
de configuración de un servidor, evalúa reglas lógicas y genera 
alertas y recomendaciones técnicas automáticas.

## 💡Materia
Programación 1 - UTN Avellaneda

## 🗂️ Datos que solicita el sistema
El sistema solicita los siguientes parámetros al administrador del servidor:
#DatoTipo1Porcentaje de uso de CPUNumérico (0–100)2Porcentaje de uso de RAMNumérico (0–100)3Espacio libre en discoNumérico en GB4Cantidad de usuarios conectadosEntero5Cantidad de procesos activosEntero6Sistema operativolinux / windows server7Estado del firewallactivo / inactivo8Tipo de servidorweb / base de datos / archivos9Nombre del servidorTexto10Nombre del administrador responsableTexto

⚙️ Funcionamiento
1. El usuario ingresa los datos del servidor por consola
2. El módulo de validaciones verifica que cada valor sea correcto
3. El módulo de reglas evalúa combinaciones lógicas sobre los datos
4. El módulo de cálculos procesa métricas adicionales si corresponde
5. El módulo de output imprime el diagnóstico final con alertas y recomendaciones

🧠 Restricciones técnicas aplicadas
Este proyecto fue desarrollado bajo las siguientes restricciones de la cursada:

Recorrido de listas exclusivamente con while e índice manual
Sin uso de métodos de lista (.append(), .remove(), etc.)
Sin comprensiones de listas
Sin sorted() ni .sort()
Funciones cortas, con una única responsabilidad
Uso de f-strings para toda la construcción de cadenas
Docstrings y type hints en todas las funciones

## 👥 Participantes: 
- Agustina Grandón
- Xiomara Nicho
- Camila Velásquez
