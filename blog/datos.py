perfil_autor = {
    "nombre": "Vivian Kohen",
    "bio": "Psicologa, Analista de Sistemas de Informacion y Programadora",
    "especialidad": "Identidad Digital, Python, JavaScript, Django y Desarrollo Web",
    "redes_sociales": ["@vivian_kohen", "@digitalizados", "@love_python"]
}
estados_post = ("borrador", "publicado", "archivado")
etiquetas_blog = {"Python", "Identidad Digital", "Django", "JavaScript", "Redes Sociales", "Desarrollo Web"}
posts = [
    {
        "id": 1,
        "titulo": "Python, la guia definitiva",
        "contenido": "Se provee teoria y ejercicios practicos para lograr un manejo avanzado de Python.",
        "autor": perfil_autor,
        "tags": ["Python", "Django"],
        "estado": "publicado"
    },
    {
        "id": 2,
        "titulo": "Desarrollo Web",
        "contenido": "Se brindan las herramientas para desarrollar un sitio web estatico.",
        "autor": perfil_autor,
        "tags": ["Desarrollo Web", "Identidad Digital"],
        "estado": "archivado"
    },
    {
        "id": 3,
        "titulo": "Aprender a programar: Python y JavaScript",
        "contenido": "Se brindan herramientas teoricas para el aprendizaje de Python y JavaScript.",
        "autor": perfil_autor,
        "tags": ["Python", "JavaScript"],
        "estado": "publicado"
    },
    {
        # Post con dato inválido a propósito para probar la validación:
        "id": 4,
        "titulo": "Redes sociales e identidad digital",
        "contenido": "Se explora como las redes sociales moldean la identidad digital.",
        "autor": perfil_autor,
        "tags": ["Identidad Digital", "Redes Sociales"],
        "estado": "en desarrollo"  # 'en desarrollo' no pertenece a estados_post
    }
]
