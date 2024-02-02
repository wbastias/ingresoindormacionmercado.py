compra = []

print ("------------------")
print ("- LISTA DE COMPRA -")
print("--------------------")


while True:
    print ("1.- Añadir Producto")
    print ("2.- Eliminar producto")
    print ("3.- Mostar lista de compra")
    print ("4.- Salir del programa")
    print ()
    opcion = input("--> ")
    print()
    if opcion == "1":
        producto = input("Introduce el producto: ").capitalize()#la primera en mayuscula
        flag = True
        while flag:
            if producto in compra:
                print("ese producto ya esta en la lista.")
                producto = input("Ingrese nuevamente el producto:  ").capitalize()              
            else:
                compra.append(producto)
                flag = False
                print("Producto ingresado con existo")
                # agregar a la lista
    elif opcion == "2":
        producto = input("introduce el producto: ").capitalize()
        if producto not in compra:
            print("ese producto no esta en la lista.")
        else:
            compra.remove(producto)
            print("Producto Eliminado")#remove para eliminar un elemento
    elif opcion == "3":
        print("listo compra:")
        for i in compra:
            print("-", i)
    elif opcion == "4":
        break
    else:
        print("introduce una opcion correcta.")

    print()



    