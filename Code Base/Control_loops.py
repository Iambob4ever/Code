#Comparisons
a = 2
b = 5

#prints TRUE/FALSE
print(a == b) # a is equal to b
print(a != b) # a not equal to b
print(a < b)  # a is smaller than b
print(a > b)
print(a <= b) # a is smaller than or equal to b
print(a >= b) # 

##############################################
#IF / ELSE
age = 30
age_seconds = age * 365 * 24 * 60 * 60

if age_seconds < 1000000000:
    print("You are less than 1 billion seconds old")
elif age_seconds == 1000000000:
    print("You are 1 billion seconds")
else:
    print("You are older than 1 billion seconds")

##############################################
#For Loops

names = ["Alice", "Bob", "Charlie"]

#Goes for each object
for name in names:
    print("Hello, " + name + "!")

#Counting loop 

for i in range(10):
    print(i)

###############################################
#While loops

a = 1
#while the condition is true
while a < 2000:
    print(a)
    a = a * 2


    