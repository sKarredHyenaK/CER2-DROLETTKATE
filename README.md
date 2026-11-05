# CERTAMEN 2 EIN082B

### Requisitos previos:
- Python instalado 
    verificar: python --version

### Instalación y Configuración:
1. Descargar o clonar proyecto

2. Inicializar entorno virtual
comandos:
    python -m venv .venv        # Crear el entorno virtual
    .venv\Scripts\activate      # Activar el entorno virtual (Windows)
    source .venv/bin/activate   # Activar el entorno virtual (macOS/Linux)

3. Instalar dependencias:
comandos: 
    pip install -r requirements.txt

4. Configurar base de datos:
comandos:
    python manage.py migrate

5. Ejecutar aplicación:
comandos:
    python manage.py runserver