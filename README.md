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

