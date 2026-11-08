

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

def listar_posts(lista):
    print("\n--- Todos los posts ---")
    for post in lista:
        autor_nombre = post.get("autor", {}).get("nombre", "Desconocido")
        print(f"- ID: {post.get('id')} | Titulo: {post.get('titulo')} | Autor: {autor_nombre} | Estado: {post.get('estado')}")

def buscar_por_titulo(lista):
    termino = input("Ingrese el termino o titulo a buscar: ").strip().lower()
    encontrados = False
    print("\n--- Posts encontrados ---")
    for post in lista:
        if termino in post.get("titulo", "").lower():
            print(f"- ID: {post.get('id')} | Titulo: {post.get('titulo')}")
            encontrados = True
    if not encontrados:
        print("No se encontraron posts con ese termino.")

def filtrar_por_tag(lista):
    tag_buscado = input("Ingrese la etiqueta (tag) a filtrar: ").strip().lower()
    encontrados = False
    print("\n--- Posts encontrados por etiqueta ---")
    for post in lista:
        tags = [str(t).lower() for t in post.get("tags", [])]
        if tag_buscado in tags:
            print(f"- ID: {post.get('id')} | Titulo: {post.get('titulo')} | Tags: {post.get('tags')}")
            encontrados = True
    if not encontrados:
        print("No se encontraron posts con esa etiqueta.")


    

