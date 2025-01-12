#With a class, you can essentially define your own data type
#Classes are extremely useful
#A class is like an object constructor, or a blueprint for creating objects
#It's like creating a model for an object by giving it some attributes

#Let's create a class below
#The keyword "class" is used

#Then give the class a name i.e "student"

#"def" is a function definition that defines a user-defined function object

#The __init__ method is crucial in object-oriented programming in python
#It is a special method automatically called when an object is created from a class.
#This method allows us to initialize an object's attributes and perform any necessary
#setup or initialization task.
#the __init__ is an instance method that initiates a newly created object.
#It takes the object as its first argument (self) followed by additional arguments.

#"self" is referring to the actual object

# name, major gpa... are parameters / arguments

class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

#Now we have successfully created a student data type