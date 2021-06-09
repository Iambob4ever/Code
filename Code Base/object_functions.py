#Example to show that data can be created within the function and does not need to be passed in
from datetime import datetime

class person:
    #constructor class
    def __init__(self, name, hight, weight):
         self.name = name
         self.hight = hight 
         self.weight = weight
         _now = datetime.now()
         self._create_time = _now.strftime("%H:%M:%S")
         

    def introduce_self(self):
        print("My name is " + self.name)
    def create_date(self):
        print("I was created " + self.create_time)

p1 = person("bob",179,165)

p1.introduce_self()
p1.create_date()
#comment
