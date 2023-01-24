class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.aver_grade = 0
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def _average(self):
        for i in self.grades:
            self.aver_grade += sum(self.grades[i])/len(self.grades[i])
        self.aver_grade /= len(self.grades)
        return self.aver_grade
    def compare(self, student):
        if isinstance(student, Student):
            if student.aver_grade > self.aver_grade:
                print(f'{student.name} {student.aver_grade} больше {self.name} {self.aver_grade}')
            elif student.aver_grade < self.aver_grade:
                print(f'{student.name} {student.aver_grade} меньше {self.name} {self.aver_grade}')
            else:
                print(f'{student.name} {student.aver_grade} равна {self.name} {self.aver_grade}')
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self._average()} \nКурсы в процессе изучения:: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.aver_grade = 0
    def _average(self):
        for i in self.grades:
            self.aver_grade += sum(self.grades[i])/len(self.grades[i])
        self.aver_grade /= len(self.grades)
        return self.aver_grade
    def compare(self, lecturer):
        if isinstance(lecturer, Lecturer):
            if lecturer.aver_grade > self.aver_grade:
                print(f'{lecturer.name} {lecturer.aver_grade} больше {self.name} {self.aver_grade}')
            elif lecturer.aver_grade < self.aver_grade:
                print(f'{lecturer.name} {lecturer.aver_grade} меньше {self.name} {self.aver_grade}')
            else:
                print(f'{lecturer.name} {lecturer.aver_grade} равна {self.name} {self.aver_grade}')
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self._average()}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} '

#Создаем первого студента *Имя *Фамилия *пол *текущий курс
stud_1 = Student('Алексей', 'Кравченко', 'муж')
stud_1.courses_in_progress.append('Python')
stud_1.courses_in_progress.append('GIT')
stud_1.finished_courses.append('Введение в программирование')

#Создаем второго студента *Имя *Фамилия *пол *текущий курс
stud_2 = Student('Илона', 'Саркисян', 'жен')
stud_2.courses_in_progress.append('Python')
stud_2.courses_in_progress.append('GIT')
stud_2.finished_courses.append('Введение в программирование')

#Создаем первого лектора *Имя *Фамилия *прикрепленный_курс
lec_1 = Lecturer('Иван', 'Иванов')
lec_1.courses_attached.append('Python')
lec_1.courses_attached.append('GIT')

#Создаем первого лектора *Имя *Фамилия *прикрепленный_курс
lec_2 = Lecturer('Мария', 'Ильина')
lec_2.courses_attached.append('Python')
lec_2.courses_attached.append('GIT')

#Создаем первого ревьюера *Имя *Фамилия *прикрепленный_курс
rew_1 = Reviewer('Яков', 'Бобов')
rew_1.courses_attached.append('Python')
rew_1.courses_attached.append('GIT')

#Создаем второго ревьюера *Имя *Фамилия *прикрепленный_курс
rew_2 = Reviewer('Илья', 'Ильин')
rew_2.courses_attached.append('Python')
rew_2.courses_attached.append('GIT')

#Ставим оценку первому лектору за лекцию по Питону
stud_1.rate_lec(lec_1, 'Python', 9)
stud_2.rate_lec(lec_1, 'Python', 9)

#Ставим оценку первому лектору за лекцию по Гиту
stud_1.rate_lec(lec_1, 'GIT', 7)
stud_2.rate_lec(lec_1, 'GIT', 7)

#Ставим оценку второму лектору за лекцию по Питону
stud_1.rate_lec(lec_2, 'Python', 8)
stud_2.rate_lec(lec_2, 'Python', 8)

#Ставим оценку второму лектору за лекцию по Гиту
stud_1.rate_lec(lec_2, 'GIT', 10)
stud_2.rate_lec(lec_2, 'GIT', 10)

#Ставим оценку первому студенту  за курс по Питону
rew_1.rate_hw(stud_1, 'Python', 1)
rew_2.rate_hw(stud_1, 'Python', 1)

#Ставим оценку первому студенту  за курс по Гиту
rew_1.rate_hw(stud_1, 'GIT', 2)
rew_2.rate_hw(stud_1, 'GIT', 2)

#Ставим оценку второму студенту  за курс по Питону
rew_1.rate_hw(stud_2, 'Python', 2)
rew_2.rate_hw(stud_2, 'Python', 2)

#Ставим оценку второму студенту  за курс по Гиту
rew_1.rate_hw(stud_2, 'GIT', 2)
rew_2.rate_hw(stud_2, 'GIT', 2)

all_stud = [stud_1, stud_2]
all_lec = [lec_1, lec_2]
all_course = ['Python', 'GIT']
all_stud_grades = []
all_lec_grades = []
def aver_all_stud(stud, course):
    for i in stud:
        all_stud_grades.extend(i.grades[course])
    print(f'Cредняя оценка за домашние задания по всем студентам в рамках  курса {course} равна {sum(all_stud_grades) / len(all_stud_grades)}')

def aver_all_lec(lec, course):
    for i in lec:
        all_lec_grades.extend(i.grades[course])
    print(f'Cредняя оценка за лекции по всем лекторам в рамках  курса {course} равна {sum(all_stud_grades) / len(all_stud_grades)}')

#Выводим всю инфу
print(stud_1)
print()
print(stud_2)
print()
print(lec_1)
print()
print(lec_2)
print()
print(rew_1)
print()
print(rew_2)
print()
stud_1.compare(stud_2)
print()
lec_1.compare(lec_2)
print()
aver_all_stud(all_stud, 'GIT')
print()
aver_all_lec(all_lec, 'Python')


