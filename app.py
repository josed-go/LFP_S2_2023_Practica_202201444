from funciones_archivos import funciones_archivos

funciones = funciones_archivos

product = []
stock = []
precio = []
ubicacion = []

def main():
    print("-------------------------------------------------------")
    print("** PRACTICA 1 - LENGUAJES FORMALES Y DE PROGRAMACIÓN **")
    print("-------------------------------------------------------")
    menu()
    
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

def agregar_producto(nombre, ubicacion_p, cantidad):
    for index, productos in enumerate(product):
        #for ubicaciones in ubicacion:
        if nombre == productos and ubicacion_p.strip() == ubicacion[index].strip():
            stock[index] = str(int(stock[index]) + int(cantidad))
                #print(nombre, ubicacion_p, stock[index])

def vender_producto(nombre, ubicacion_p, cantidad):
    for index, productos in enumerate(product):
        #for ubicaciones in ubicacion:
        if nombre == productos and ubicacion_p.strip() == ubicacion[index].strip():
            if int(cantidad) <= int(stock[index]):
                stock[index] = str(int(stock[index]) - int(cantidad))
                print("## PRODUCTO", nombre, " VENDIDO CORRECTAMENTE ##")
            else:
                print("** NO HAY SUFICIENTES PRODUCTO", nombre, " EN STOCK **")

    
def buscar_producto(nombre, ubicacion_p):
    for index, productos in enumerate(product):
        #for ubicaciones in ubicacion:
        if nombre == productos and ubicacion_p.strip() == ubicacion[index].strip():
            return True
            
    return False

def reporte():
    print("## INGRESE EL NOMBRE PARA GUARDAR EL REPORTE ##")
    nombre = input()
    funciones.escribir_reporte(nombre,product,stock,precio,ubicacion)


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


main()