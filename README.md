# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.
segundas pruebas subidas por jose ramon


---
Esta es las pruebas de la segunda rama, voy a modificar varias cosas en la segunda rama.

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Prerequisitos

### Ejecucion sin makefile
Tener instalado Python (con la versión 3.X).
* En Ubuntu instalar mediante:
```
$ sudo apt-get update
$ sudo apt-get install python3.X
```
_Donde X es la version que deseamos instalar_

* En MacOS instalar mediante:
```
$ brew install python
```
_Debe descargar el interprete de [brew](https://brew.sh/index_es)_

### Ejecucion con makefile
Tener instalado Python (con la versión 3.X).
* En Ubuntu instalar mediante:
```
$ sudo apt-get update
$ sudo apt-get install docker
```
_Donde X es la version que deseamos instalar_

* En MacOS instalar mediante:
```
$ brew install docker
```
_Debe descargar el interprete de [brew](https://brew.sh/index_es)_

## Ejecución

### Ejecucion sin makefile
```
python3 main.py <filename> <dup>
```
Donde:
* filename: **ruta** al fichero que contiene la lista de palabras, una por línea
* dup: **yes | no**, yes para eliminar palabras duplicadas, no para mantener la lista

### Ejecucion con makefile
```
make
```
_NOTA: Para funcionar deberás editar el Makefile con la ubicación del fichero_

## Formato del fichero
Como se ha destacado anteriormente, al script se le debe pasar
un fichero. Como es evidente, este fichero debe ir en un formato concreto para 
poder aprovechar al máximo la funcionalidad del script, es por eso que debe seguir el 
siguiente patron:
```
<palabra_1>
<palabra_2>
<palabra_3>
<palabra_4>
<palabra_5>
```
**NOTA:** Como podemos ver, como se ha enunciado en apartados anteriores, debe ser una palabra por linea.

## Ejemplos de ejecución

### Ejemplo 1 - Sin eliminacion de duplicados (sin Makefile)
1. Deberiamos crear un fichero con el formato enunciado anteriormente:
```
jenkins
kubernetes
docker
devops
packer
docker
```
**NOTA:** En nuestro caso el fichero estara ubicado en: examples/words.txt

2. Una vez hecho esto, ejecutaremos el script mediante el comando siguiente (en este caso indicando
que no queremos que elimine las palabras duplicadas):
```
python3 main.py examples/prueba.txt no
```
3. El resultado, como le hemos indicado que no queremos que elimine los duplicados sera el siguiente:
```
['devops', 'docker', 'docker', 'jenkins', 'kubernetes', 'packer']
```
_Vemos como la palabra "docker" aparece duplicada._

### Ejemplo 2 - Con eliminacion de duplicados (sin Makefile)
1. Deberiamos crear un fichero con el formato enunciado anteriormente:
```
jenkins
kubernetes
docker
devops
packer
docker
```
**NOTA:** En nuestro caso el fichero estara ubicado en: examples/words.txt

2. Una vez hecho esto, ejecutaremos el script mediante el comando siguiente (en este caso indicando
que queremos que elimine las palabras duplicadas):
```
python3 main.py examples/prueba.txt yes
```
3. El resultado, como le hemos indicado que queremos que elimine los duplicados sera el siguiente:
```
['devops', 'docker', 'jenkins', 'kubernetes', 'packer']
```
_Vemos como la palabra "docker" aparece solo una vez._

### Ejemplo 3 - Con eliminacion de duplicados (con Makefile)
1. Deberiamos crear un fichero con el formato enunciado anteriormente:
```
jenkins
kubernetes
docker
devops
packer
docker
```
**NOTA:** En nuestro caso el fichero estara ubicado en: examples/words.txt

2. Una vez hecho esto, cambiamos en el Makefile la ubicacion del fichero. Tambien le indicamos que elimine las palabras duplicadas.
```
.PHONY: all $(MAKECMDGOALS)

run:
	docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py <ubicacion_fichero> yes
```
3. Una vez hecho esto, ejecutaremos el script mediante el comando siguiente:
```
make
```

4. El resultado, como le hemos indicado que queremos que elimine los duplicados sera el siguiente:
```
['devops', 'docker', 'jenkins', 'kubernetes', 'packer']
```
_Vemos como la palabra "docker" aparece solo una vez._


## Contacte con nosotros
Si tiene alguna duda, por favor contacte a través del canal de comunicación de la Universidad UNIR.
