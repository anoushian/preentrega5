#Blog por Consola - Preentrega 5
Sistema interactivo por consola para gestionar y consultar publicaciones de un blog, desarrollado en Python con arquitectura modularizada en paquetes.

#Estructura del Proyecto
```text
blog_consola/
├── blog/
│   ├── __init__.py
│   ├── menu.py          # Gestión de opciones y entrada de usuario
│   ├── operaciones.py   # Listado, búsqueda y filtrado de posts
│   └── validaciones.py  # Reglas de validación y control de errores
├── main.py              # Punto de entrada y orquestador del sistema
├── README.md            # Documentación del proyecto
└── .gitignore           # Archivos y carpetas ignorados por Git

# Requisitos y Ejecución
Python 3.10 o superior
Para ejecutar el programa, abrí una terminal en la carpeta principal del proyecto y corré:

bash
python3 main.py

# Funcionalidades
Ver todos los posts: Muestra la lista completa de publicaciones formateadas.
Buscar por título: Filtra publicaciones que contengan una palabra clave en su título.
Filtrar por tag: Lista publicaciones asociadas a una etiqueta específica.
Validar posts: Comprueba la consistencia y validez de la estructura de datos.
Salir: Finaliza la sesión de la consola de forma segura.

#Tecnologías Utilizadas
Python: Manejo de modularización, funciones, colecciones, excepciones y paquetes locales.
Git & GitHub: Control de versiones.



