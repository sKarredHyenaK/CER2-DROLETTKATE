# CERTAMEN 2 EIN082B

### Requisitos previos:

Python instalado
verificar: python --version

### Instalación y Configuración:
- Descargar o clonar proyecto

- Inicializar entorno virtual
comandos:

python -m venv .venv        # Crear el entorno virtual
.venv\Scripts\activate      # Activar el entorno virtual (Windows)
source .venv/bin/activate   # Activar el entorno virtual (macOS/Linux)

- Instalar Dependencias
comandos:

pip install -r requirements.txt

- Configurar Base de Datos
comandos:

python manage.py migrate

- Ejecutar Aplicación
comandos:

python manage.py runserver
