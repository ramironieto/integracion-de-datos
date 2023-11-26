# Integracion de Datos
En este repositorio se tiene un prototipo mínimo viable de la aplicación planteada en la entrega final de Integracion de Datos.

Este proyecto fue creado usando [Django](https://www.djangoproject.com/), un framework sobre Python. Django nos permitió rápidamente tener una aplicación web simple, y una base SQL asociada. Las queries a la base se hicieron mediante el ORM de Django.

Se creó una aplicación llamada `datos_integrados` donde se tiene el comando 
[db_refresh.py](https://github.com/ramironieto/integracion-de-datos/blob/main/integracion_de_datos/datos_integrados/management/commands/db_refresh.py) que es encargado de integrar los datos de las dos fuentes. 

## Como correr el proyecto
Para hacer funcionar este proyecto se tiene que tener instalado Python. Luego, usando pip, el instalador de bibliotecas de Python, se necesita instalar: Django y la version de selenium 3.3.0.
Una vez hecho esto se tienen que correr las migraciones a la base creada. 
Por ultimo ahora ya estamos habilitados a correr el comando: `python manage.py db_refresh`.
