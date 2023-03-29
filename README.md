# Temas

Este proyecto es un sistema CRUD de temas implementados en Django. Se trata de una aplicación web de una agenda de estudio que permite a los usuarios organizar sus temas de estudio de manera efectiva. Los usuarios pueden registrar sus temas de estudio y marcarlos como completados cuando los hayan terminado. También pueden ver una lista de todos los temas que han completado, con el fin de realizar un seguimiento del progreso de estudio.

## Requisitos previos

Python 3.7 o superior
Django 3.2 o superior
pip (el manejador de paquetes de Python)

## Instalación

1. Descarga el código fuente del proyecto desde el repositorio en GitHub y extrae los archivos en una carpeta local.
2. Abre una terminal o línea de comandos y navega hasta la carpeta del proyecto: Django_proyecto.
3. Crea un entorno virtual de Python para instalar las dependencias del proyecto sin afectar a otros proyectos de Python en tu sistema: venv y activalo.
4. Ejecuta las migraciones para crear la base de datos: python manage.py migrate
5. Inicia el servidor de desarrollo

## Uso
Después de haber iniciado el servidor de desarrollo, puedes acceder al proyecto desde tu navegador. 
1. Regístrate para crear una cuenta.
2. Inicia sesión con tus credenciales.
3. Agrega temas de estudio a tu lista.
4. Completa los temas de estudio cuando los hayas terminado.
5. Ve una lista de todos los temas que has completado.

El proyecto consta de las siguientes páginas:

1. Inicio (http://localhost:8000/): una página simple de inicio que muestra un saludo de bienvenida.
2. Registrarse (http://localhost:8000/registro/): una página donde los usuarios pueden registrarse para obtener una cuenta.
3. Iniciar sesión (http://localhost:8000/iniciar_sesion/): una página donde los usuarios pueden iniciar sesión con su cuenta.
4. Temas (http://localhost:8000/temas/): una página donde los usuarios pueden ver una lista de temas pendientes. Desde aquí, pueden crear nuevos temas o hacer clic en un tema para ver más detalles.

5. Temas completados (http://localhost:8000/temas_completados/): una página donde los usuarios pueden ver una lista de temas que ya han completado.
6. Crear tema (http://localhost:8000/crear_tema/): una página donde los usuarios pueden crear un nuevo tema.

7. Detalle del tema (http://localhost:8000/temas/{id}/): una página que muestra los detalles de un tema en particular. Desde aquí, los usuarios pueden actualizar o eliminar el tema, o marcarlo como completado.
El número máximo de ID de tema que puedes acceder dependerá del número de temas que se tenga en la base de datos. Si se tiene temas con IDs desde 1 hasta N, donde N es el último ID de tema en tu base de datos, entonces podrás acceder a URLs como http://localhost:8000/temas/1/, http://localhost:8000/temas/2/, ..., http://localhost:8000/temas/N/.

Sin embargo, debemos tomar en cuenta que si intentamos acceder a una URL para un ID de tema que no existe en tu base de datos, se producirá un error 404.

8. Cerrar sesión (http://localhost:8000/cerrar_sesion/): una página que permite a los usuarios cerrar sesión de su cuenta.

Además de estas páginas, el proyecto también incluye un panel de administración de Django (http://localhost:8000/admin/) donde se pueden gestionar los temas y los usuarios del sistema.
# Estructura del proyecto (se documento el proyecto usando Sphinx)
Django_proyecto>/
├── Temas/
│   ├──__init__.py
│   ├──migrations/
│   ├──admin.py
│   ├──apps.py
│   ├──forms.py
│   ├──models.py
│   ├──test.py
│   ├──views.py
│   ├──templates.py
│   │  ├──barra_navegacion.html
│   │  ├──base.html
│   │  ├──crear_tema.html
│   │  ├──detalle_tema.html
│   │  ├──iniciar_sesion.html
│   │  ├──inicio.html
│   │  ├──registro.html
│   │  └──temas.html
│   └── static/
│       ├── css/estilos.css
│       └── imagenes/imagen1, imagen2, imagen3, imagen4
│       
├── Django_proyecto/
│   ├── __init__.py
│   ├── asgi.py
│   ├── urls.py
│   ├── wsgi.py
│   └── settings.py
│
├── build/
├── docs/
├── README.md
├──db.sqlite3
├── manage.py
└── venv/

