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