#FUNCTION is a little block of code that we can run to perform a specific operation
#we use a keyword called def to write a function in python
#code included in a function must be indented
#you can include as many line of code as you want in a function
#you can pass in one or more parameters in a function, below we pass in the parameter: name.

def say_hi(name): #here, we define a function named: say_hi. This function will require us to give it a name whenever we call it
    print("hello " + name + " how are you?") #this is a code contained in our function, it is indented

say_hi("Adam") #we call the function here, python will jump back up and read the content then return.

print("top") #python execute this first
say_hi("Alex") #python goes up to read and execute code in the function say_hi
print("bottom") #then this is printed next.

#below we pass in multiple parameter: name, age amd phone
def staff_data(name, age, phone): #here, we define a function named: staff_data. This function will require us to give it a name, age and phone whenever we call it
    print("hello " + name + "You are " + str(age) + " years old ," + "your mobile number is " + str(phone)) #this is a code contained in our function, it is indented

staff_data("Adam ", 10, 5038822220)

#note that within the function code, in line 18 we specified the parameters: age and phone as strings, otherwise python will throw an error
#if we do not indicate as string within the code in line 18, then we must indicate as string using double quote when calling the function in line 20