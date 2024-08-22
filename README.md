# Control de Ingreso de Empleados

## Descripción

Desarrollar una aplicación de control de ingreso de empleados con las siguientes funcionalidades:

- **Registrar hora de ingreso y salida** de los empleados.
- **Crear, modificar y eliminar proveedores o invitados** registrando nombre y documento de identidad.
- **Registrar hora de ingreso y salida** de los invitados o proveedores.
- **Generar reportes** de las horas trabajadas por cada empleado.
- **Generar reportes** de las horas trabajadas por áreas (sistemas, mercadeo, producción, etc.).
- **Generar reporte** de la cantidad de personas que se encuentran dentro de la empresa para controlar las evacuaciones en caso de emergencia.

## Criterios de Aceptación

- La aplicación debe permitir **filtrar** por fechas, empleados, invitados, proveedores o centro de costos.
- Si un empleado ingresa y sale varias veces en el mismo día, se deberá calcular el **tiempo total** que permaneció dentro de las instalaciones.
- Si un empleado se retira antes de las 16:00, se deberá pedir el **motivo de retiro** de acuerdo con las siguientes opciones: Cita médica, calamidad o diligencia personal.
- Los **reportes** deben ser construidos en SQL.

## Instalación y Configuración

### 1. Crear un Entorno Virtual

Para asegurar que todas las dependencias se manejen adecuadamente, crea un entorno virtual. Abre tu terminal y ejecuta:

```bash
python -m venv env
env\Scripts\activate
source env/bin/activate
pip install -r requirements.txt

Configurar la Base de Datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_base_de_datos',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

4. Crear las Migraciones
python manage.py makemigrations
python manage.py migrate

Finalmente 

python manage.py runserver



Este archivo `README.md` proporciona una guía completa y clara para configurar, ejecutar y entregar tu proyecto.
