cursos_lista = []

def agregar_curso(codigo, nombre):
    if not codigo.strip() or not nombre.strip():
        print(" ❌ Todos los campos son obligatorios.")
        return False
    # Verificar si el código ya existe
    for curso in cursos_lista:
        if curso["codigo"] == codigo:
            print(" ❌ Ya existe un curso con ese código.")
            return False
    curso = {
        "codigo": codigo,
        "nombre": nombre
    }
    cursos_lista.append(curso)
    return True

def consultar_cursos():
    return cursos_lista

def obtener_codigos_cursos():
    return [c["codigo"] for c in cursos_lista]