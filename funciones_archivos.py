class funciones_archivos:
    
    def leer(archivo, ext):
        lineas = []
        archivo = open(archivo+ext, "r")

        lines = archivo.readline()
        while lines:
            lineas.append(lines)
            lines = archivo.readline()

        archivo.close

        return lineas
    
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