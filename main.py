from classes import Student
from classes import studentManager
from classes import Subject
from classes import subjectManager
from tabulate import tabulate


if __name__ == "__main__":
    insStudent = studentManager(9)
    insStudent.loadStudent()

    insSubject = subjectManager()
    insSubject.loadSubjects()

    # MENU
    while True:
        option = input("""
        MENU:
        a:  Informar promedio con y sin aplazos.
        b:  Informar promocionales de una materia.
        c:  Mostrar lista de alumnos.
        d:  Salir.
        """)

        if option == "a":
            dni = input("Ingrese el DNI del estudiante: ")
            temp = insSubject.getAverage(dni)
            print(f"El promedio del estudiante es: {temp.gbetGrade()}")
        elif option == "b":
            name = input("Ingrese el nombre de la materia: ")
            table = tabulate(insSubject.createTable(name, insStudent), headers="firstrow", tablefmt="fancy_grid")

            print(table)

        elif option == "c":
            insStudent.sort()
        elif option == "d":
            break
        else: print("La opcion es invalida")