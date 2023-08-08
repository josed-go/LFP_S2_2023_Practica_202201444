# *LFP_S2_2023_Practica_202201444*

* *José David Góngora Olmedo*
* *202201444*

## Introducción

Programa para manejar un inventario, donde se podra crear, vender y agregar productos. Asi como generar un reporte.

## Características

Se pueden generar y leer archivos:

- Leer archivos ".inv" para el inventario
- Leer archivos ".mov" para los movimientos
- Generar reporte ".txt"

## Contenido

Este programa contiene las siguientes funcionalidades:

### Archivo ```funciones_archivos.py```

Este archivo tiene todas las funciones para trabajar con archivos, ya sea leer o escribir.

#### Funcionalidad 1

El siguiente codigo se encuentra en el archivo ```funciones_archivos.py```. Se encarga de recibir un archivo con extension ".inv" y lo lee. Guardando todas las instrucciones en una lista y retornando dicha lista.

```python
def leer(archivo, ext):
        lineas = []
        archivo = open(archivo+ext, "r")

        lines = archivo.readline()
        while lines:
            lineas.append(lines)
            lines = archivo.readline()

        archivo.close

        return lineas
```

#### Funcionalidad 2

El siguiente codigo se encuentra en el archivo ```funciones_archivos.py```. Se encarga de generar un archivo con extension ".txt" para mostrar el reporte del inventario. Obteniendo la lista de productos, cantidad, precio y ubicación para escribir el reporte.

```python
def escribir_reporte(nombre, productos, cantidad, precio, ubicacion):
        archivo = open(nombre+".txt", "w")

        archivo.write("------------------------------------------------ INFORME DE PRODUCTOS ------------------------------------------------\n")
        archivo.write("| PRODUCTO              CANTIDAD              PRECIO UNITARIO               TOTAL              UBICACIÓN             |\n")
        archivo.write("----------------------------------------------------------------------------------------------------------------------\n")

        for index, productos in enumerate(productos):
            total = str(int(cantidad[index]) * float(precio[index]))
            archivo.write(f"| {productos}       |       {cantidad[index]}       |       Q.{precio[index]}        |       Q.{total}       |       {ubicacion[index].strip()}             |\n")

        archivo.close

        print("## REPORTE CREADO CON EXITO ##")
```