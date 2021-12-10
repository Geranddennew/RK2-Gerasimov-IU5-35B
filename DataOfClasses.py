from students import Student
from Departament import ClassDep
from StudentsInClass import StudentInClass

# Классы

ClassDeps = [
    ClassDep(1, '7А'),
    ClassDep(2, '8Б'),
    ClassDep(3, '9В'),
    ClassDep(4, '10А'),
    ClassDep(5, '11Б'),
]

# Ученики
Students = [
    Student(1, 'Герасимов', 78, 1),
    Student(2, 'Ищенко', 97, 2),
    Student(3, 'Акулова', 45, 3),
    Student(4, 'Троцук', 0, 4),
    Student(5, 'Иванов', 29, 5),
    Student(6, 'Макаров', 83, 1),
    Student(7, 'Сидоров', 65, 2),
    Student(8, 'Сыса', 66, 3),
    Student(9, 'Морозов', 48, 4),
    Student(10, 'Артёменко', 77, 5),
]
# Распределение по классам
StudentInClasses = [
    StudentInClass(1, 1),
    StudentInClass(2, 2),
    StudentInClass(3, 3),
    StudentInClass(4, 4),
    StudentInClass(5, 5),
    StudentInClass(1, 6),
    StudentInClass(2, 7),
    StudentInClass(3, 8),
    StudentInClass(4, 9),
    StudentInClass(5, 10),
]