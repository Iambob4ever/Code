#opening files

f = open("myfile.txt", "w", -1, "utf-8")
f = open("myfile.txt", encoding="utf-8", mode="w")

#We can look up names of keyword parameters in the documentation (e.g. via help(open))
#optional parameters, defualt permeteters are found in documentation. open() only the first permeter is required.


#Defineing functions

def average(a, b):
    m = (a + b) / 2
    return m


#optional parameters

#end, has a default value of !
def shout(phrase, end="!"):
    print(phrase.upper() + end)

    #outside of function
    #shout("hello") # HELLO!
    #shout("hi", ".") # HI.



#Method
#Is based on the object

first_name.upper()
first_name.count("a")
first_name.replace("a", "@")
