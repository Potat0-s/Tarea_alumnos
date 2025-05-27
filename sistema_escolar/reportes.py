def generar_reporte(lista_alumnos):
    if not lista_alumnos:
        return "No hay alumnos registrados."
    reporte = "=== REPORTE DE ALUMNOS ===\n"
    aprobados = 0
    aplazados = 0
    reprobados = 0
    for alumno in lista_alumnos:
        # Permitir ambas claves: 'Nombre'/'nombre', 'Nota'/'nota', etc.
        nombre = alumno.get('Nombre', alumno.get('nombre', ''))
        cedula = alumno.get('Cédula', alumno.get('cedula', ''))
        curso = alumno.get('Curso', alumno.get('curso', ''))
        nota = alumno.get('Nota', alumno.get('nota', 0))
        try:
            nota_num = float(nota)
        except ValueError:
            nota_num = 0
        if nota_num > 70:
            aprobados += 1
        elif nota_num < 60:
            reprobados += 1
        else:
            aplazados += 1
        reporte += (
            f"Nombre: {nombre}, "
            f"Cédula: {cedula}, "
            f"Curso: {curso}, "
            f"Nota: {nota}\n"
        )
    reporte += (
        f"\nTotal de estudiantes aprobados: {aprobados}\n"
        f"Total de estudiantes aplazados: {aplazados}\n"
        f"Total de estudiantes reprobados: {reprobados}\n"
    )
    return reporte