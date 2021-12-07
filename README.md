# W6-api-sentiment-project

## Introducción

El objetivo de este proyecto es la creación de una API y realización de un análisis de sentimientos de una serie. En mi caso voy a utilizar una base de datos de la serie de HBO 'Juego de Tronos' Esta API permite al usuario hacer request para obtener los diáligos de un personaje/episodio/temporada.

## Documentos

Este proyecto tiene varios documentos:

- data_import.py: recorre el csv e importa los datos a la base de datos.

- sentiment_analyzer.py: consta de dos funciones que utilizan la librería nltk para analizar el texto y obtener un score del sentimiento: positivo, neutro o negativo.

- controller.py: se encarga de interactuar con la base de datos (crear, validar, queries)

- db_models: Este documento es más complejo. En lugar de hacerlo en SQL directamente, utilizo sqlalchemy(orm), un intermediario entre el código y la base de datos. Sirve para poder interactuar con distintas bases de datos relacionales sin depender de las funciones nativas de SQL. Lo utilizo para evitar problemas con SQL.

- app.py: Aqui están las rutas de la API.

- index.py: Llama al documento app.py para correr el servidor.


## Conclusión

Falta el jupyter desde el que llamar a las funciones pero no he conseguido que tirase. Cuando tenga más tiempo volveré a este proyecto a retocarlo y probar la Api.
¡Muchas gracias!

## Librerias

In this project we have used the following libraries:

 - [pandas](https://pandas.pydata.org/docs/)

 

 - [sqlalchemy](https://numpy.org/doc/stable/)

 

 - [flask](https://flask.palletsprojects.com/en/2.0.x/)

 

 - [json](https://www.json.org/json-es.html)

