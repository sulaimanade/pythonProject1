#While Loop statements
#You can make a block of code execute over and over again using a while
#statement. The code in a while clause will be executed as long as the while
#statement’s condition is True.

#In code, a while statement always consists of
#the following:
#•	 The while keyword
#•	 A condition (that is, an expression that evaluates to True or False)
#•	 A colon
#•	 Starting on the next line, an indented block of code (called the while clause)

#You can see that a while statement looks similar to an if statement. The
#difference is in how they behave. At the end of an if clause, the program
#execution continues after the if statement. But at the end of a while clause,
#the program execution jumps back to the start of the while statement.

i = 1
while i <= 10:
    print(i)
    i = i + 1

print("done with loop")
