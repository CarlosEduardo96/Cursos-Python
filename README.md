# Cursos-Python
## Python principiante - avanzado

## Crear Ambiente Virtual
### para importar la biblioteca de ambiente virtual 
Cabe amencionar que el ambiente virtualizados permite crear proyectos con diferentes versiones de librerias.
Es decir; se puede tener una version diferente de alguna libreria como por ejemplo: django 3.0.0 y en otro ambiente vitualizado estar trabajando con django 4.0.0

## Pasos para crear un ambiente virtualizado
para crear un ambiente virtulizado hay que seguir los sigientes pasos
### Crea un ambiente virtualizado cono el siguiente comando:
```python -m venv Nombre-del-ambiente-virtualizado```
### crear una carpeta con nombre primer_proyecto_django

## Configurar el entorno virtual.

### Activar el entorno virtual ejemplo: 
para ello hayq eu ejecutar el archivo `Activate.ps1`  dentro de la carpeta de nuestro ambiente virtual creado.

### Dentro de la capeta del ambiente virtual ejecutar el siguiente comando: 
```python -m pip install django```

### Actualizar la libreria pip.
```python -m pip install --upgrade pip ```

### Instalar django en el proyecto primer_proyecto_django
```django-admin startproject primer_proyecto_django```

Al finalizar los pasos tendras dos carpetas una con el ambiente vistual y otra donde estaras
trabajando en el proyecto.

### instalar django para el ambiente virtualizado
`python -m pip install django~=4.0.0`


### Correr el servidor con el comando:
Para poder correr el servidor hay que ir a la ruta donde esta el archivo `manage.py` y ejecutar el siguiente comando:
```python manage.py runserver```

### Activar virtualizacion
Ejecutar el archivo `activate.ps1` dentro de la carpeta scripts

### Desactivar el embiente vistual con el siguiente comando:
`deactivate`
