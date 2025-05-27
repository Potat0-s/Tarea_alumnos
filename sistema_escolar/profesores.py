profesores_lista = []

def agregar_profesor(nombre, cedula, curso):
    if not nombre.strip() or not cedula.strip() or not curso.strip():
        print(" ❌ Todos los campos son obligatorios")
        return False
    profesor = {
        "Nombre": nombre,
        "Cédula": cedula,
        "Curso": curso
    }
    profesores_lista.append(profesor)
    return True

def consultar_profesores():
    return profesores_lista