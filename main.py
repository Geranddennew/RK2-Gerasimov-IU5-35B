import TDD
from operator import itemgetter
from DataOfClasses import ClassDeps, StudentInClasses,Students


def taskD1():
    many_to_many_temp = [(c.name, pc.ClassDep_id, pc.student_id)
                         for c in ClassDeps
                         for pc in StudentInClasses
                         if c.id == pc.ClassDep_id]

    many_to_many = [(p.fio, p.mark, ClassDep)
                    for ClassDep, ClassDep_id, student_id in many_to_many_temp
                    for p in Students if p.id == student_id]
    # «Класс» и «Ученик» связаны соотношением один-ко-многим. Выведите список всех учеников, у которых фамилия заканчивается на «ов», и названия их классов.

    answer_1 = []
    b = [j for j in many_to_many if j[0][-1:] == 'в' and j[0][-2] == 'о']
    answer_1 = {j[2]: [i[0] for i in b if i[2] == j[2]] for j in b}
    return answer_1


def taskD2():
    one_to_many = [(p.fio, p.mark, c.name)
                   for c in ClassDeps
                   for p in Students
                   if p.ClassDep_id == c.id]
    # «Класс» и «Ученик» связаны соотношением один-ко-многим. Выведите список классов со средней оценкой учеников в каждом отделе, отсортированный по средней оценке

    answer_2NS = []
    # Перебираем все классы

    for c in ClassDeps:
        # Список учеников класса
        list_students = list(filter(lambda i: i[2] == c.name, one_to_many))
        # Если класс не пустой
        if len(list_students) > 0:
            # Оценки учеников класса
            mark = [mark for _, mark, _ in list_students]
            # Среднее значение оценок учеников класса
            mark_sum = (round((sum(mark)) / (len(list_students)), 3))
            answer_2NS.append((c.name, mark_sum))

    # Сортировка по среднему значению оценки
    answer_2 = sorted(answer_2NS, key=itemgetter(1), reverse=True)

    return answer_2

    # «Класс» и «Ученик» связаны соотношением многие-ко-многим.
    # Выведите список всех классов, у которых название начинается с буквы «А»(или присутсвует),
    # и список классов в них учеников.


def taskD3(ClassDeps):
    many_to_many_temp = [(c.name, pc.ClassDep_id, pc.student_id)
                         for c in ClassDeps
                         for pc in StudentInClasses
                         if c.id == pc.ClassDep_id]

    many_to_many = [(p.fio, p.mark, ClassDep)
                    for ClassDep, ClassDep_id, student_id in many_to_many_temp
                    for p in Students if p.id == student_id]

    answer_3 = {}
    # Перебираем все классы
    for c in ClassDeps:
        if 'А' in c.name:
            # Список учеников класса
            list_students = list(filter(lambda i: i[2] == c.name, many_to_many))
            list_students_names = [x for x, _, _ in list_students]
            answer_3[c.name] = list_students_names

    return answer_3



if __name__ == '__main__':
    # Соединение данных один-ко-многим
    one_to_many = [(p.fio, p.mark, c.name)
                   for c in ClassDeps
                   for p in Students
                   if p.ClassDep_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, pc.ClassDep_id, pc.student_id)
                         for c in ClassDeps
                         for pc in StudentInClasses
                         if c.id == pc.ClassDep_id]

    many_to_many = [(p.fio, p.mark, ClassDep)
                    for ClassDep, ClassDep_id, student_id in many_to_many_temp
                    for p in Students if p.id == student_id]

    print('Задание D1:')
    print(taskD1())
    print('Задание D2:')
    print(taskD2())
    print('Задание D3:')
    print(taskD3(ClassDeps))

