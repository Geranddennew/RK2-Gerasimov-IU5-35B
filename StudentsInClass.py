class StudentInClass:
    """ 'Ученики класса' для реализации связи многие-ко-многим"""

    def __init__(self, ClassDep_id, student_id):
        self.ClassDep_id = ClassDep_id
        self.student_id = student_id
