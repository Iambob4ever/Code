#Classes
# Are a data structure and a behaviour 
class student:
    def check_pass_fail(self):
        if self.marks >=60:
            return True
        else:
            return False

student1 = student()
student1.name = "harry"
student1.marks = 85

did_pass = student1.check_pass_fail()
print(did_pass)


class robot:
    #constructor class
    def __init__(self, name, colour, weight):
         self.name = name
         self.colour = colour 
         self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)


#This won't work with a constructor
#r1 = robot()
#r1.weight = 400
#This is does almost the same thing except uses a constructor
r1 = robot("rob","red",400)

#simple class : no functions
class Length():
    pass

a = Length(2.54, "cm")
b = Length(3, "in")

a.unit
a.value