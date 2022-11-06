class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = round(sum(map(sum, self.grades.values())) / grades_count, 1)
        res = f'Имя: {self.name}' \
              f'\nФамилия: {self.surname}' \
              f'\nКурсы в процессе изучения: {self.courses_in_progress}' \
              f'\nЗавершенные курсы: {self.finished_courses}' \
              f'Средняя оценка за домашние задания: {self.average_rating}'
        return res

    def __lt__(self,other):
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        for c in self.grades:
            grades_count += len(self.grades[c])
        self.average_rating = round(sum(map(sum, self.grades.values())) / grades_count, 1)
        res = f'Имя: {self.name}' \
              f'\nФамилия: {self.surname}' \
              f'\nСредняя оценка: {self.average_rating}'
        return res

    def __lt__(self,other):
        return self.average_rating < other.average_rating


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}' \
              f'\nФамилия: {self.surname}'
        return res


# Студенты - информация

student_1 = Student('Peter', 'Parker', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ['Git']

student_2 = Student('Sheldon', 'Cooper', 'M')
student_2.courses_in_progress += ['Git']
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Python']

student_3 = Student('Tony', 'Stark', 'M')
student_3.courses_in_progress += ['Java']
student_3.finished_courses += ['Git']
student_3.finished_courses += ['Python']

# Лекторы -  курсы

lecturer_1 = Lecturer('Richards ', 'Reed ')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']
lecturer_1.courses_attached += ['Java']

lecturer_2 = Lecturer('Charles ', 'Xavier')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']
lecturer_2.courses_attached += ['Java']

lecturer_3 = Lecturer('Stephen', 'Strange')
lecturer_3.courses_attached += ['Python']


# Проверяющие - информация

reviewer_1 = Reviewer('Bruce ', 'Wayne')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_2 = Reviewer('Victor ', 'Doom')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']

# Студенты -оценка, курс

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Python', 9)
student_1.rate_hw(lecturer_1, 'Git', 8)
student_1.rate_hw(lecturer_1, 'Git', 8)
student_1.rate_hw(lecturer_1, 'Java', 7)
student_1.rate_hw(lecturer_1, 'Java', 9)

student_1.rate_hw(lecturer_2, 'Python', 10)
student_1.rate_hw(lecturer_2, 'Python', 10)
student_1.rate_hw(lecturer_2, 'Git', 6)
student_1.rate_hw(lecturer_2, 'Git', 7)
student_1.rate_hw(lecturer_2, 'Java', 8)
student_1.rate_hw(lecturer_2, 'Java', 10)

student_1.rate_hw(lecturer_3, 'Python', 7)
student_1.rate_hw(lecturer_3, 'Python', 9)

student_2.rate_hw(lecturer_1, 'Python', 7)
student_2.rate_hw(lecturer_1, 'Python', 9)
student_2.rate_hw(lecturer_1, 'Git', 10)
student_2.rate_hw(lecturer_1, 'Git', 8)
student_2.rate_hw(lecturer_1, 'Java', 9)
student_2.rate_hw(lecturer_1, 'Java', 9)

student_2.rate_hw(lecturer_2, 'Python', 8)
student_2.rate_hw(lecturer_2, 'Python', 10)
student_2.rate_hw(lecturer_2, 'Git', 8)
student_2.rate_hw(lecturer_2, 'Git', 7)
student_2.rate_hw(lecturer_2, 'Java', 8)
student_2.rate_hw(lecturer_2, 'Java', 9)

student_2.rate_hw(lecturer_3, 'Python', 10)
student_2.rate_hw(lecturer_3, 'Python', 9)

student_3.rate_hw(lecturer_1, 'Python', 10)
student_3.rate_hw(lecturer_1, 'Python', 10)
student_3.rate_hw(lecturer_1, 'Git', 10)
student_3.rate_hw(lecturer_1, 'Git', 10)
student_3.rate_hw(lecturer_1, 'Java', 10)
student_3.rate_hw(lecturer_1, 'Java', 10)

student_3.rate_hw(lecturer_2, 'Python', 9)
student_3.rate_hw(lecturer_2, 'Python', 9)
student_3.rate_hw(lecturer_2, 'Git', 9)
student_3.rate_hw(lecturer_2, 'Git', 9)
student_3.rate_hw(lecturer_2, 'Java', 9)
student_3.rate_hw(lecturer_2, 'Java', 10)

student_3.rate_hw(lecturer_3, 'Python', 10)
student_3.rate_hw(lecturer_3, 'Python', 10)

# Проверяющие - оценка, курс

reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 8)

reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Java', 10)
reviewer_1.rate_hw(student_2, 'Java', 9)
reviewer_1.rate_hw(student_2, 'Git', 7)
reviewer_1.rate_hw(student_2, 'Git', 6)

reviewer_1.rate_hw(student_3, 'Python', 10)
reviewer_1.rate_hw(student_3, 'Python', 8)
reviewer_1.rate_hw(student_3, 'Java', 7)
reviewer_1.rate_hw(student_3, 'Java', 7)
reviewer_1.rate_hw(student_3, 'Git', 8)
reviewer_1.rate_hw(student_3, 'Git', 8)

reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Java', 7)
reviewer_2.rate_hw(student_1, 'Java', 9)
reviewer_2.rate_hw(student_1, 'Git', 6)
reviewer_2.rate_hw(student_1, 'Git', 8)

reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Java', 5)
reviewer_2.rate_hw(student_2, 'Java', 9)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 6)

reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Python', 10)
reviewer_2.rate_hw(student_3, 'Java', 8)
reviewer_2.rate_hw(student_3, 'Java', 8)
reviewer_2.rate_hw(student_3, 'Git', 6)
reviewer_2.rate_hw(student_3, 'Git', 6)

student_list = [student_1, student_2, student_3]
lecturer_list = [lecturer_1, lecturer_2, lecturer_3]


def student_rating(student_list, course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += stud.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += lect.average_rating
            count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

print(f'Список студентов:\n{student_1}\n\n{student_2}\n\n{student_3}')
print(f'\n--------------------------------------------\n')

#--------------------------------------------

print(f'Список лекторов:\n{lecturer_1}\n\n{lecturer_2}\n\n{lecturer_3}')
print(f'\n--------------------------------------------\n')

#--------------------------------------------

print(f'Сравние студентов:'
      f'\n{student_1.name} и {student_2.name}: {student_1 > student_2}'
      f'\n{student_1.name} и {student_3.name}: {student_1 > student_3}'
      f'\n{student_2.name} и {student_3.name}: {student_2 > student_3}')
print(f'\n--------------------------------------------\n')

#--------------------------------------------

print(f'Сравние студентов:'
      f'\n{lecturer_1.name} и {lecturer_2.name}: {lecturer_1 > lecturer_2}'
      f'\n{lecturer_1.name} и {lecturer_3.name}: {lecturer_1 > student_3}'
      f'\n{lecturer_2.name} и {lecturer_3.name}: {lecturer_2 > lecturer_3}')
print(f'\n--------------------------------------------\n')

#--------------------------------------------

print(f"Средняя оценка студентов по курсу {'Java'}: {student_rating(student_list, 'Java')}")
print(f"Средняя оценка лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list, 'Python')}")