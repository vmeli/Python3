class Person:
    name = ''
    age = 0
    country = ''

    def __init__(self, name, age, country): #Constructor (inicialización)
        self.name = name
        self.age = age
        self.country = country

    def greet(self):
        print('Bievenido a Python', self.name)

    def farewell(self):
        print('Sigue practicando')

    def score(self):
        self.greet()
        print('Falta poco para la excelencia')

user = Person('Sandor', 20, 'Londres')
print(user.age)
user.greet()

#HERENCIA SIMPLE
class Student(Person):
    school = ''

student = Student('Juliet', 18, 'Londres')
print(student.name, student.country)

#HERENCIA MÚLTIPLE
class Language:
    speak = ''

''' En caso de existir dos inicializadores
    se respeta los parámetros de la izquierda
'''
class Plataform(Student,Language):
    course = ''

user_student = Plataform('Xiomara', 17, 'Londres')
user_student.score()