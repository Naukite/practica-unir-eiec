# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución
```
python3 main.py <filename> <dup>
```
Donde:
* filename: **ruta** al fichero que contiene la lista de palabras, una por línea
* dup: **yes | no**, yes para eliminar palabras duplicadas, no para mantener la lista

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

### Ejemplo 1 - Sin eliminacion de duplicados
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

### Ejemplo 2 - Con eliminacion de duplicados
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