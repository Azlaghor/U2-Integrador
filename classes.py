import numpy as np
import csv

class Student:
    # ========= Init ========= #
    def __init__ (self,dni,lasName, name, career, year):
        self.__dni = dni
        self.__lastName = lasName
        self.__name = name
        self.__career = career
        self.__year = year

    # ========= Overload ========= #
    def __str__(self):
        return f"{self.__dni} {self.__lastName} {self.__name} {self.__career} {self.__year}"

    def __lt__(self, other):
        if self.__year != other.getYear(): return self.__year < other.getYear()
        else: return (self.__lastName.lower(), self.__name.lower()) < (other.getLastName(), other.getName())
    
    # ========= Getters ========= #
    def getDni(self):
        return self.__dni

    def getLastName(self):
        return self.__lastName

    def getName(self):
        return self.__name

    def getCareer(self):
        return self.__career

    def getYear(self):
        return self.__year

    

class studentManager:
    __length = 0
    __amount = 0
    __increase = 5
    # ========= Init ========= #
    def __init__(self, length):
        self.__students = np.empty(length, dtype=Student)
        self.__amount = 0
        self.__length = length
    # ========= Methods ========= #
    def addStudent(self, new):
        if self.__amount == self.__length:
            self.__amount += self.__increase
            self.__students.resize(self.__length)
        self.__students[self.__amount] = new
        self.__amount += 1

    def getStudent(self):
        return self.__students
    
    def loadStudent(self):
        with open("alumnos.csv") as archive:
            for line in archive:
                data = line.strip().split(";")
                student = Student(data[0],data[1],data[2],data[3],data[4])
                self.addStudent(student)
    
    def searchDni(self, dni):
        for student in self.__students:
            if student == dni:
                print(student)

    def sort(self):
        sortStud = sorted(self.__students)
        sortStud.pop()

        for name in sortStud:
            print(name)

class Subject:
    # ========= Init ========= #
    def __init__(self, dni, name, date, grade, passing):
        self.__dni = dni
        self.__name = name
        self.__date = date
        self.__grade = grade
        self.__passing = passing
    
    # ========= Overload ========= #
    def __str__(self):
        return f"{self.dni} {self.__name} {self.__date} {self.__grade} {self.__passing}"

    # ========= Getters ========= #
    def getDni(self):
        return self.__dni

    def getName(self):
        return self.__name

    def getDate(self):
        return self.__date

    def getGrade(self):
        return self.__grade

    def getPassing(self):
        return self.__passing
    

class subjectManager():
    def __init__(self):
        self.__subjects = []
        # self.__table = []

    def addSubject(self,  new):
        self.__subjects.append(new)

    def loadSubjects(self):
        with open("materiasAprobadas.csv") as archive:
            for line in archive:
                data = line.strip().split(";")
                subject = Subject(data[0], data[1], data[2], data[3], data[4])
                self.addSubject(subject)


    def getAverage(self, dni):
        for ins in self.__subjects:
            if dni == ins.getDni():
                return ins
    def createTable(self, name, student):
        table = []
        title = ["DNI", "Apellido y nombre", "Fecha", "Nota", "Año que cursa"]
        table.append(title)
        data  = []
        for i in range(5):
            data.append(None)
        for i in self.__subjects:
            if i.getName() == name:
                if i.getPassing() == "P":
                    data[0] = i.getDni()
                    data[2] = i.getDate()
                    data[3] = i.getGrade()
                    for j in student.getStudent():
                        if j.getDni() == i.getDni():
                            data[1] = f"{j.getName()} {j.getLastName()}"
                            data[4] = f"{j.getYear()}º Año"
                            table.append(data)
                
        return table
