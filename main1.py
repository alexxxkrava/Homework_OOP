class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def info(self):
        print(f'Студент \nИмя: {self.name} \nФамилия: {self.surname} \nПол: {self.gender} \nКурс: {self.courses_in_progress} \nОценка за курс: {self.grades}')

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def info(self):
        print(f'Лектор \nИмя: {self.name} \nФамилия: {self.surname}  \nКурс: {self.courses_attached} \nОценка за лекцию: {self.grades}')

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
    def info(self):
        print(f'Ревьюер \nИмя: {self.name} \nФамилия: {self.surname}  \nКурс: {self.courses_attached}')

#Создаем первого студента *Имя *Фамилия *пол *текущий курс
stud_1 = Student('Леха', 'Крава', 'мужик')
stud_1.courses_in_progress.append('Python')
print()

#Создаем лектора *Имя *Фамилия *прикрепленный_курс
lec_1 = Lecturer('Яша', 'Лава')
lec_1.courses_attached.append('Python')
print()

#Создаем ревьюера *Имя *Фамилия *прикрепленный_курс
rew_1 = Reviewer('Ясос', 'Биба')
rew_1.courses_attached.append('Python')
print()

#Ставим оценку лектору за лекцию
stud_1.rate_lec(lec_1, 'Python', 10)
stud_1.rate_lec(lec_1, 'Python', 9)
stud_1.rate_lec(lec_1, 'Python', 8)

#Ставим оценку студенту за курс
rew_1.rate_hw(stud_1, 'Python', 10)

#Выводим всю инфу
stud_1.info()
print()
lec_1.info()
print()
rew_1.info()




