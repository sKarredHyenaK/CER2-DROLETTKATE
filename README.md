# CERTAMEN 2 EIN082B
link repositorio Github: https://github.com/sKarredHyenaK/CER2-DROLETTKATE

### Requisitos previos:
- Python instalado. Verificar:
```bash 
python --version
```
### Instalación y Configuración:
- Descargar o clonar proyecto

- Inicializar entorno virtual
```bash
python -m venv .venv        # Crear el entorno virtual
.venv\Scripts\activate      # Activar el entorno virtual (Windows)
source .venv/bin/activate   # Activar el entorno virtual (macOS/Linux)
```
- Instalar Dependencias
```bash
pip install -r requirements.txt
```
- Configurar Base de Datos
```bash
python manage.py migrate
```
- Ejecutar Aplicación
```bash
python manage.py runserver
```
