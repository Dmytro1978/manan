class Student(object):
    name = ""
    age = 0
    major = ""

    # The class "constructor" - It's actually an initializer 
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def printInfo(self):
    	print "Name: %s\nAge: %s\nMajor: %s" %(self.name, self.age, self.major)

def make_student(name, age, major):
    student = Student(name, age, major)
    return student
    
student = make_student("Sam", 21, "Computer Science")
student.printInfo()
