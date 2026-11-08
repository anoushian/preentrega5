from blog.datos import posts
from blog.operaciones import listar_posts, buscar_por_titulo, filtrar_por_tag
from blog.validaciones import validar_todos_los_posts
from blog.menu import mostrar_menu, ingresar_opcion


def main():
    while True:
        mostrar_menu()
        opcion = ingresar_opcion()
        if opcion is None:
            continue
        if opcion == 1:
            listar_posts(posts)
        elif opcion == 2:
            buscar_por_titulo(posts)
        elif opcion == 3:
            filtrar_por_tag(posts)
        elif opcion == 4:
            validar_todos_los_posts(posts)
        elif opcion == 5:
            print("Gracias por usar el sistema del blog. ¡Hasta luego!")
            break
        else:
            print("Opcion invalida. Por favor elija un numero del 1 al 5.")

if __name__ == "__main__":
    main()
