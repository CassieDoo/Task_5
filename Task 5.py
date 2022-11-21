class Student:
    instancelist = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.instancelist.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturers(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mean_grades(self):
        grades_list = []
        for course_grades in self.grades.values():
            for grade in course_grades:
                grades_list.append(grade)
        return sum(grades_list) / len(grades_list)

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}" \
               f"\nСредняя оценка: {self.mean_grades()}" \
               f"\nКурсы в процессе изучения: {self.courses_in_progress}" \
               f"\nЗавершенные курсы: {self.finished_courses}"

    def __lt__(self, other):
        return self.mean_grades() < other.mean_grades()

    def __gt__(self, other):
        return self.mean_grades() > other.mean_grades()

    def __eq__(self, other):
        return self.mean_grades() == other.mean_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.grades = {}

    def mean_grades(self):
        if not self.grades:
            return 0
        grades_list = []
        for course_grades in self.grades.values():
            for grade in course_grades:
                grades_list.append(grade)
        return sum(grades_list) / len(grades_list)

    def __str__(self) -> str:
        return f"{super().__str__()}\nСредняя оценка за лекции: {self.mean_grades()}"

    def __lt__(self, other):
        return self.mean_grades() < other.mean_grades()

    def __gt__(self, other):
        return self.mean_grades() > other.mean_grades()

    def __eq__(self, other):
        return self.mean_grades() == other.mean_grades()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)

    def rate_students(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
                return student.grades
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Tom', 'Cruise', 'male')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Angelina', 'Jolie')
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Anna', 'Bolein')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Matt', 'Smith')
reviewer_2.courses_attached += ['Git']

student_1.rate_lecturers(lecturer_1, 'Python', 8)
student_2.rate_lecturers(lecturer_1, 'Python', 9)

student_1.rate_lecturers(lecturer_2, 'Git', 10)

reviewer_1.rate_students(student_1, 'Python', 10)
reviewer_1.rate_students(student_2, 'Python', 8)

reviewer_2.rate_students(student_1, 'Git', 9)


def mean_course_grades_lecturers(*lecturers, course):
    lecturers_list = [*lecturers]
    lecturers_grades_list = []
    for lecturer in lecturers_list:
        lecturer_grades = lecturer.grades
        for lecturer_course, lecturer_grades in lecturer_grades.items():
            if lecturer_course == course:
                for mark in lecturer_grades:
                    lecturers_grades_list.append(mark)
    return sum(lecturers_grades_list) / len(lecturers_grades_list)


def mean_course_grades_students(*students, course):
    students_list = [*students]
    students_grades_list = []
    for student in students_list:
        students_grades = student.grades
        for student_course, student_grades in students_grades.items():
            if student_course == course:
                for mark in student_grades:
                    students_grades_list.append(mark)
    return sum(students_grades_list) / len(students_grades_list)


print(lecturer_1.grades)
print(lecturer_2.grades)

print(student_1.grades)
print(student_2.grades)

print(lecturer_1 > lecturer_2)

print(mean_course_grades_students(student_1, student_2, course='Python'))
print(mean_course_grades_students(lecturer_1, lecturer_2, course='Python'))

