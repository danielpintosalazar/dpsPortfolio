# Portafolio Daniel Pinto Salazar

Portafolio web de Daniel Pinto Salazar.

## Instalación

Para correr el proyecto debe contar en el equipo con los siguiente recursos:

_*Los programas mencionados deben estar ejecutandose en su equipo_

* Docker
* Git


### Clonar repositorio

_*En caso de no tener acceso para clonar el repositorio debe solicitarlas al desarrollador o al encargado de gestionar el sitio_

`git clone url`

### Correr el proyecto

Se debe crear un archivo .env en la carpeta raiz del proyecto e indicar las siguientes variables de entorno secretas:

_*En caso de no conocer las variables de entorno debe solicitarlas al desarrollador o al encargado de gestionar el sitio_

_*Por defecto el docker-compose guardará la información en la siguiente ruta con nombre **/data/db/** esta debe ser creada en el directorio raiz_


| Variable                 | Descripción                                                         |
| --------------------     |:----------------------------------------------------------:         |
| SECRET_KEY               | Llave secreta de Django                                             |
| DJANGO_DEBUG             | Booleano para la muestra de errores                                 |
| ALLOWED_HOSTS            | Direcciones permitidas para hacer solicitudes al sitio              |
| POSTGRES_HOST            | Host de PostgreSQL                                                  |
| POSTGRES_PORT            | Puerto de ejecución de Base de datos PostgreSQL                     |
| POSTGRES_DB              | Nombre de la base de datos                                          |
| POSTGRES_USER            | Usuario de acceso a la base de datos                                |
| POSTGRES_PASSWORD        | Contraseña de acceso a base de datos                                |

Para construir las imagenes web y de base de datos para el proyecto en Docker:

`docker-compose -f docker-compose.yml build`

Para desplegar el contenedor:

`docker-compose up`

Para hacer las migraciones de los modelos de datos al sitio:

`docker-compose -f .\docker-compose.yml run --rm web python manage.py makemigrations`

`docker-compose -f .\docker-compose.yml run --rm web python manage.py migrate`

Para ejecutar comandos internos en el contenedor de Docker:

`docker exec -it <container-id> /bin/sh`

## ¿Cómo usar?

### Consideraciones

## ¿Cómo contribuir?
## Licencia