import alumnos
import profesores
import cursos
import reportes

def menu():
    while True:
        print("\n===== SISTEMA ESCOLAR =====")
        print("1. Alumnos")
        print("2. Profesores")
        print("3. Cursos")
        print("4. Reporte")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == '1':
            while True:
                sub = input("a) Agregar Alumno\nb) Consultar Alumnos\ns) Salir\nSeleccione: ").lower().strip()
                if sub == 'a':
                    nombre = input("Nombre: ")
                    cedula = input("Cédula: ")
                    curso = input("Código del Curso: ")
                    nota = input("Nota: ")
                    cursos_validos = cursos.obtener_codigos_cursos()
                    if alumnos.agregar_alumno(nombre, cedula, curso, nota, cursos_validos):
                        print(" \n✅ Alumno agregado con éxito")
                elif sub == 'b':
                    lista = alumnos.consultar_alumnos()
                    if not lista:
                        print(" \n⚠️  No hay alumnos registrados")
                        continue
                    for a in lista:
                        print(a)
                elif sub == 's':
                    break
                else:
                    print(" \n❌ Opción inválida. Intente de nuevo")

        elif opcion == '2':
            while True:
                sub = input("a) Agregar Profesor\nb) Consultar Profesores\ns) Salir\nSeleccione: ").lower().strip()
                if sub == 'a':
                    nombre = input("Nombre: ")
                    cedula = input("Cédula: ")
                    curso = input("Curso que imparte: ")
                    if profesores.agregar_profesor(nombre, cedula, curso):
                        print(" \n✅ Profesor agregado con éxito")
                elif sub == 'b':
                    lista = profesores.consultar_profesores()
                    if not lista:
                        print(" \n⚠️  No hay profesores registrados")
                        continue
                    for p in lista:
                        print(p)
                elif sub == 's':
                    break
                else:
                    print(" \n❌ Opción inválida. Intente de nuevo")

        elif opcion == '3':
            while True:
                sub = input("a) Agregar Curso\nb) Consultar Cursos\ns) Salir\nSeleccione: ").lower().strip()
                if sub == 'a':
                    codigo = input("Código del curso: ")
                    nombre = input("Nombre del curso: ")
                    if cursos.agregar_curso(codigo, nombre):
                        print(" \n✅ Curso agregado con éxito")
                elif sub == 'b':
                    lista = cursos.consultar_cursos()
                    if not lista:
                        print(" \n⚠️ No hay cursos registrados")
                        continue
                    for c in lista:
                        print(c)
                elif sub == 's':
                    break
                else:
                    print(" \n❌  Opción inválida. Intente de nuevo")

        elif opcion == '4':
            datos = alumnos.consultar_alumnos()
            print(reportes.generar_reporte(datos))

        elif opcion == '5':
            print("\n👋 ...Saliendo del sistema...")
            break

        else:
            print("\n❌ Opción inválida. Intente de nuevo")

if __name__ == "__main__":
    menu()