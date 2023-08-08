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

### Archivo ```app.py```

Este archivo es el principal, se encuentra el menu y la logica de toda la funcionalidad del programa.

#### Función 1

Es el encabezado para el menu.

```python
def main():
    print("-------------------------------------------------------")
    print("** PRACTICA 1 - LENGUAJES FORMALES Y DE PROGRAMACIÓN **")
    print("-------------------------------------------------------")
    menu()
```

#### Función 2

Es toda la logica del menu, donde se muestran las opciones y donde se selecciona que accion se desea hacer.

```python
def menu():
    print("")
    print("-------------------------------------------------------")
    print("################ SISTEMA DE INVENTARIO ################")
    print("-------------------------------------------------------")

    print("-------------------------------------------------------")
    print("| 1. CARGAR INVENTARIO INICIAL                        |")
    print("| 2. CARGAR INSTRUCCIONES DE MOVIMIENTOS              |")
    print("| 3. CARGAR INFORME DE INVENTARIO                     |")
    print("| 4. SALIR                                            |")
    print("-------------------------------------------------------")

    print("")
    print("## INGRESE UNA OPCION: ##")
    opcion = input()
    print("")

    if opcion == "1":
        inventario_inicial()
        menu()
    elif opcion == "2":
        instrucciones_movimiento()
        menu()
    elif opcion == "3":
        reporte()
        menu()
    elif opcion == "4":
        print("4")
    else:
        print("** OPCIÁN NO VÁLIDA **")
        menu()
```

#### Función 3

En este codigo es donde se trabaja con las instrucciones que se obtienen al leer el archivo ".inv" y se agregan los productos a las listas.

```python
def inventario_inicial():
    print("## INGRESE EL NOMBRE DEL ARCHIVO O LA RUTA ##")
    archivo = input()
    print("")

    try: 
        for p in funciones.leer(archivo, ".inv"):
            producto = p.split(" ",1)
            producto.remove("crear_producto")
            product.append(producto[0].split(";")[0])
            stock.append(producto[0].split(";")[1])
            precio.append(producto[0].split(";")[2])
            ubicacion.append(producto[0].split(";")[3])
        
        print("## PRODUCTOS AGREGADOS! ##")
        print(product)
        print(stock)
        print(precio)
        print(ubicacion)
    except:
        print("** ARCHIVO NO ENCONTRADO **")
```

#### Función 4

Es esta parte del codigo se realizan las ventas o agregar productos al obtener las instrucciones del archivo ".mov".

```python
def instrucciones_movimiento():
    instruccion = []
    producto_temp = []
    cantidad_temp = []
    ubicacion_temp = []
    print("## INGRESE EL NOMBRE DEL ARCHIVO O LA RUTA ##")
    archivo = input()
    print("")

    try:
        for movimiento in funciones.leer(archivo, ".mov"):
            movi = movimiento.split(" ",1)
            instruccion.append(movi[0])
            movi.pop(0)
            producto_temp.append(movi[0].split(";")[0])
            cantidad_temp.append(movi[0].split(";")[1])
            ubicacion_temp.append(movi[0].split(";")[2])

        for index, instrucciones in enumerate(instruccion):
            validaciones_movimiento(instrucciones, producto_temp[index], cantidad_temp[index], ubicacion_temp[index])
            print("")

        print("## SE HICIERON MOVIMIENTOS EN LOS PRODUCTOS ##")
        print(product)
        print(stock)
        print(precio)
        print(ubicacion)

    except:
        print("** ARCHIVO NO ENCONTRADO **")
```

#### Función 5

Esta función realiza una busqueda del producto y su ubicación para saber si existen. Retorna un booleano.

```python
def buscar_producto(nombre, ubicacion_p):
    for index, productos in enumerate(product):
        if nombre == productos and ubicacion_p.strip() == ubicacion[index].strip():
            return True
            
    return False
```

#### Función 6

En esta función se hacen las validaciones y se agregar o venden productos al obtener las instrucciones del archivo.

```python
def validaciones_movimiento(instru, nombre, cantidad, ubicacion):
    if instru == "agregar_stock":
        if buscar_producto(nombre, ubicacion) == True:
            agregar_producto(nombre, ubicacion, cantidad)
            print("## PRODUCTO", nombre, " AGREGADO CORRECTAMENTE ##")
        elif buscar_producto(nombre, ubicacion) == False:
            print("** PRODUCTO", nombre, "NO EXISTE EN UBICACIÓN:", ubicacion.strip(),"**")

    elif instru == "vender_producto":
        if buscar_producto(nombre, ubicacion) == True:
            vender_producto(nombre, ubicacion, cantidad)

        elif buscar_producto(nombre, ubicacion) == False:
            print("** PRODUCTO", nombre, "NO EXISTE EN ESA UBICACIÓN:", ubicacion.strip(),"**")
```

#### Función 7

Esta función agrega los productos a la lista si cumple las validaciones.

```python
def agregar_producto(nombre, ubicacion_p, cantidad):
    for index, productos in enumerate(product):
        if nombre == productos and ubicacion_p.strip() == ubicacion[index].strip():
            stock[index] = str(int(stock[index]) + int(cantidad))
```

#### Función 8

Esta función vende los productos si cumple las validaciones.

```python
def vender_producto(nombre, ubicacion_p, cantidad):
    for index, productos in enumerate(product):
        if nombre == productos and ubicacion_p.strip() == ubicacion[index].strip():
            if int(cantidad) <= int(stock[index]):
                stock[index] = str(int(stock[index]) - int(cantidad))
                print("## PRODUCTO", nombre, " VENDIDO CORRECTAMENTE ##")
            else:
                print("** NO HAY SUFICIENTES PRODUCTO", nombre, " EN STOCK **")
```

#### Función 9

Esta función genera el reporte del inventario.

```python
def reporte():
    print("## INGRESE EL NOMBRE PARA GUARDAR EL REPORTE ##")
    nombre = input()
    funciones.escribir_reporte(nombre,product,stock,precio,ubicacion)
```

### Archivo ```funciones_archivos.py```

Este archivo tiene todas las funciones para trabajar con archivos, ya sea leer o escribir.

#### Función 1

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

#### Función 2

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