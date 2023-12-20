# import math


# class shape:
#     def __init__(self,color) -> None:
#         self.color = color
#     def get_color(self):
#         return self.color
    
#     def area(self):
#         pass
# class rectangle(shape):
#     def __init__(self,color,l,w) -> None:
#         super().__init__(color=color)
#         self.length = l
#         self.width = w
#     def area(self):
#         return self.length*self.width
# class circle(shape):
#     def __init__(self,color,r) -> None:
#         super().__init__(color=color)        
#         self.radius = r
#     def area(self):
#         return math.pi * ((self.radius)**2)
# circle = circle('Blue',5)
# print(circle.get_color())
# print(circle.area())
# rect = rectangle('Red',2,3)
# print(rect.get_color())
# print(rect.area())

class Student:
    studentList = []
    def __init__(self,name,grade,age):
        Student.studentList.append([name,grade])
        self.name = name
        self.age = age
        self.grade = grade
        self.course = []
    def display(self):
        print(f"Name: {self.name}\n Age: {self.age}\nGrade: {self.grade}")
        for course in self.course:
            print(f"Course Name: {course.course_name}\n Teacher: {course.teacher.name}")
    def add_course(self,course):
        self.course.append(course)


class course:
    def __init__(self,course_name,course_code,teacher):
        assert course_name == teacher.subject, "Not the correct teacher"
        self.course_name = course_name
        self.course_code = course_code
        self.teacher = teacher
        
class teacher:
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject      

stud = Student('Abebe',100, 20)
first_teacher = teacher('abel','english')
english = course('english',123,first_teacher)

stud.add_course(english)
stud.display()    
