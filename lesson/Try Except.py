# using "except" without specifying the error to catch is not a best practice
# Best practice is to specify which specific error the "except" is meant to catch

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err: #here, we specify the error we would like to catch, and stored it as a variable "err"
    print(err)
except ValueError: #here, we specify the error we would like to catch
    print("Invalid Input")
