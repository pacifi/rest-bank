# API REST

Validación de pagos por evento

## Proceso de desarrollo.

Validación de pagos a eventos por cuenta y persona

## Proceso Terminado.

Conexión a API REST, Registro de Eventos  

## Metodo de identificación

- Django JWT Json Web Token

## Dependencias del sistema.

1. Python 3

## Ejecución

    $ git clone https://github.com/pacifi/rest-bank.git
    $ cd rest-bank
    $ virtualenv -p python3 venv
    $ source venv/bin/activate  # Linux
    $ source venv/bin/Scripts/activate # Windows
    $ pip install -r requirements.txt
    $ python manage.py makemigrations 
    $ python manage.py migrate
    $ python manage.py loaddata data.json
    $ python manage.py runserver 9000


### Datos de Prueba

![GitHub Logo](/docs/img.png)    

Visitar la página de Inicio http://localhost:9000


    