def mostrar_menu():
    print("\n--- MENU DEL BLOG ---")
    print("1. Ver todos los posts")
    print("2. Buscar por titulo")
    print("3. Filtrar por tag")
    print("4. Validar posts")
    print("5. Salir")

def ingresar_opcion():
    try:
        entrada = input("Elija una opcion (1-5): ").strip()
        opcion = int(entrada)
        return opcion
    except ValueError:
        print("Error: Debe ingresar un numero entero entre 1 y 5.")
        return None


