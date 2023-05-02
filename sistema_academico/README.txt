# Proyecto de Registro de sistema_academico por Leonardo Viudez

Este es un proyecto de ejemplo de Django para registrar y buscar sistema_academico. Incluye las siguientes funcionalidades:

- Un modelo de `Alumno` con campos como nombre, apellido, correo electrónico y fecha de nacimiento.
- Un modelo de `Profesor` con campos como nombre, apellido, correo electrónico y asignatura.
- Vistas para ver una lista de todos los sistema_academico registrados, así como para insertar nuevos registros.
- Un formulario para buscar registros en la base de datos.

## Configuración del proyecto

Para utilizar este proyecto, sigue los siguientes pasos:

1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual utilizando `python -m venv env` y actívalo con `source env/bin/activate` (en Linux/Mac) o `env\Scripts\activate` (en Windows).
3. Instala las dependencias utilizando `pip install -r requirements.txt`.
4. Crea la base de datos utilizando `python manage.py migrate`.
5. Carga algunos datos de prueba utilizando `python manage.py loaddata registros.json`.
6. Ejecuta el servidor de desarrollo con `python manage.py runserver`.
7. Visita `http://localhost:8000/` en tu navegador para ver la página principal del proyecto.

## Estructura del proyecto

El proyecto sigue la estructura típica de Django, con los siguientes archivos y directorios relevantes:


- `registro/models.py`: Define los modelos de `Alumno` y `Profesor`.
- `registro/views.py`: Define las vistas que manejan las solicitudes HTTP y renderizan las plantillas HTML.
- `registro/templates/`: Contiene las plantillas HTML utilizadas por las vistas.
- `registro/forms.py`: Define los formularios utilizados para insertar y buscar registros.
- `registro/urls.py`: Define las rutas URL para cada vista.




## Para el profesor

Profe aprobame por favor no tuve tiempo!
Sino se puede bueno, se entiende...
Prometo hacer una entrega decente.
No entiendo que estoy haciendo mal,
pude replicar lo de la clase pero con el proyecto propio me perdi..



Necesito feedback ya que me tira el siguiente error:

Request Method:	GET
Request URL:	http://localhost:8000/registro/insertar
Using the URLconf defined in sistema_academico.urls, Django tried these URL patterns, in this order:

admin/
The current path, registro/insertar, didn’t match any of these.

You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.



## ERROR EN EL CMD :

Not Found: /registro/insertar
[01/May/2023 07:59:32] "GET /registro/insertar HTTP/1.1" 404 2139
[01/May/2023 08:01:04] "GET / HTTP/1.1" 200 10731
[01/May/2023 08:01:04] "GET /static/admin/css/fonts.css HTTP/1.1" 404 1816