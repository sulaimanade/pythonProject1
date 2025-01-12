#Class function Python
# A class function is a function we can use inside a class.
# It is a function that can be used by the object of the class

# This is the class

class Staff:
    def __init__(self, name, department, duration):
        self.name = name
        self.department = department
        self.duration = duration

# Now this is the function below

    def on_probation(self):
        if self.duration >= "6months":
            return False
        else:
            return True
