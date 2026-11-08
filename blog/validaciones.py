from blog.datos import estados_post

def validar_post(post):
    if not isinstance(post, dict):
        print("  -> Falló: el post no es un diccionario.")
        return False
    claves_obligatorias = ["id", "titulo", "contenido", "autor", "tags", "estado"]
    for clave in claves_obligatorias:
        if clave not in post:
            print(f"  -> Falló: falta la clave obligatoria '{clave}'.")
            return False
        valor = post[clave]
        if valor is None:
            print(f"  -> Falló: '{clave}' es None.")
            return False
        if isinstance(valor, str) and valor.strip() == "":
            print(f"  -> Falló: '{clave}' está vacío.")
            return False
        if isinstance(valor, (list, set)) and len(valor) == 0:
            print(f"  -> Falló: '{clave}' no tiene elementos.")
            return False
    # Verificación de autor
    if not isinstance(post["autor"], dict) or not post["autor"].get("nombre"):
        print(f"  -> Falló: 'autor' no es diccionario válido o no tiene 'nombre' (valor actual: {post.get('autor')}).")
        return False
     # Verificación de estado
    if post["estado"] not in estados_post:
        print(f"  -> Falló: estado '{post['estado']}' no está en {estados_post}.")
        return False
    return True

def validar_todos_los_posts(lista):
    print("\n--- Validacion de posts ---")
    for post in lista:
        post_id = post.get("id", "?")
        if validar_post(post):
            print(f"[OK] Post ID {post_id} es valido.")
        else:
            print(f"[ERROR] Post ID {post_id} contiene datos incompletos o estado invalido.")

