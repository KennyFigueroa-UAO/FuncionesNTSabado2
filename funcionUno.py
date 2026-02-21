#Declarar una funcion que permita crear una lisa de n estudiandtes

def createStudentsList(studentsQ):
    
    students = []
    
    for _ in range(studentsQ):
        student = {}
        student['id'] = input("id: ")
        student['documento'] = input("documento: ")
        student['nombres'] = input("nombres: ")
        student['correo'] = input("correo: ")
        student['telefono'] = input("telefono: ")
        student['promedio'] = input("promedio: ")
        student['semestre'] = input("semestre: ")
        student['esBecado'] = input("Estas becado?: ")

        students.append(student)
    
    return students

students = createStudentsList(2)
print(students)