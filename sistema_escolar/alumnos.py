alumnos_lista = []

def validar_alumno(nombre, cedula, curso, nota):
    if not nombre.strip():
        return False, "El Nombre no puede estar vacío"
    if not cedula.isdigit():
        return False, "La Cédula debe ser numérica"
    if not curso.strip():
        return False, "El Curso no puede estar vacío"
    try:
        nota = float(nota)
        if nota < 0 or nota > 100:
            return False, "La nota debe estar entre 0 y 100"
    except ValueError:
        return False, "La nota debe ser un número"
    return True, ""

def agregar_alumno(nombre, cedula, curso, nota, cursos_validos):
    if curso not in cursos_validos:
        print(" ❌ Código de curso inválido")
        return False
    valido, mensaje = validar_alumno(nombre, cedula, curso, nota)
    if not valido:
        print(" ❌", mensaje)
        return False
    alumno = {
        "Nombre": nombre,
        "Cédula": cedula,
        "Curso": curso,
        "Nota": nota
    }
    alumnos_lista.append(alumno)
    return True

def consultar_alumnos():
    return alumnos_lista