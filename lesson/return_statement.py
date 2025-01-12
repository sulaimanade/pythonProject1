#the return statement helps to return the outcome of the code we have within the function we defined

def cube(num): #we define a function here, and pass in a parameter: num
    return num*num*num #we want the function to return a result, and the result (parameter) in multiple of 3

print(cube(5))

#now let's store the returned value from our function into a variable
def new_num(num): #we define a function here, and pass in a parameter: num
    return num*num*num #we want the function to return a result, and the result (parameter) in multiple of 3

result = (new_num(3)) #here, we will store the returned value into the variable: result

print(result) #then we print variable: result

#note: that the return keyword breaks out of the function code, sort of indicating the end of the code in a function.