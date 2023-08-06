def main():
    print("-------------------------------------------------------")
    print("** PRACTICA 1 - LENGUAJES FORMALES Y DE PROGRAMACIÓN **")
    print("-------------------------------------------------------")
    menu()
    
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

    if opcion == "1":
        print("1")
        menu()
    elif opcion == "2":
        print("2")
        menu()
    elif opcion == "3":
        print("3")
        menu()
    elif opcion == "4":
        print("4")
    else:
        print("** OPCIÁN NO VÁLIDA **")
        menu()


main()