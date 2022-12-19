# SCRIPTS desarrollados para ejercicio "Sobre yaml"

## Para ejecutar el script es necesario Python3. En caso de no tenerlo puede utilizarse el contenedor docker que se encunetra en un nivel superior a este archivo.

## Forma de ejecución:

1- docker-compose build
2- docker-compose up
3- docker exec -it python /bin/bash
4- cd usr/src/app/sobre_yaml
5- python main.py


El archivo main ejecuta dos "clases". La primera crea un csv (archivo.csv) para tenerlo como ejemplo.
Luego ejecuta el script que convierte ese csv a json y yaml (archivo.json y archivo.yaml respectivamente)


El script tiene varios puntos de mejoras, algunos de ellos son:
 - Recibir lor paths de los archivos de entrada y salida por parametros.
 - No se utilizaron librerias que no esten provistas por python para facilitar la ejecucion en cualquier dispositivo (debe tener python3). Sin embargo la escritura de json y -fundamentalmente- yaml se podria modularizar y mejorar.

