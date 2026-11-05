# CERTAMEN 2 EIN082B

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

## USUARIOS REGISTRADOS PARA PRUEBAS:

#### Superusuario
Superususario: admin
contraseña: admin1234

#### Usuario con permisos limitados:
usuario: user
contraseña: User1234