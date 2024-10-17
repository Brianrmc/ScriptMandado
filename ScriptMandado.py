def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar elemento")
    print("2. Eliminar elemento")
    print("3. Modificar elemento")
    print("4. Imprimir lista")
    print("5. Finalizar")

def agregar_elemento(lista):
    item = input("Ingrese el elemento que desea agregar: ")
    lista.append(item)
    print(f"'{item}' ha sido agregado a la lista.")

def eliminar_elemento(lista):
    item = input("Ingrese el elemento que desea eliminar: ")
    if item in lista:
        lista.remove(item)
        print(f"'{item}' ha sido eliminado de la lista.")
    else:
        print(f"'{item}' no está en la lista.")

def modificar_elemento(lista):
    item = input("Ingrese el elemento que desea modificar: ")
    if item in lista:
        nuevo_item = input(f"Ingrese el nuevo valor para '{item}': ")
        index = lista.index(item)
        lista[index] = nuevo_item
        print(f"'{item}' ha sido modificado a '{nuevo_item}'.")
    else:
        print(f"'{item}' no está en la lista.")

def imprimir_lista(lista):
    if lista:
        print("\nLista del mandado:")
        for i, item in enumerate(lista, 1):
            print(f"{i}. {item}")
    else:
        print("La lista está vacía.")

def main():
    lista_mandado = ['huevos', 'leche', 'pan']
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_elemento(lista_mandado)
        elif opcion == '2':
            eliminar_elemento(lista_mandado)
        elif opcion == '3':
            modificar_elemento(lista_mandado)
        elif opcion == '4':
            imprimir_lista(lista_mandado)
        elif opcion == '5':
            print("Finalizando programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
