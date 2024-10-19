#variable, how to use variables

character_name= "Mike"
character_age= "30"
print("There was once a Man called "+ character_name +",")
print("he was " + character_age + " years old,")
print("he really liked the name " + character_name + ",")
print("but did not like being " + character_age + ".")

print("I wil be travelling home,\"not until next week though") #insert quote
print("I wil be travelling home,\nnot until next week though") #break into a new line

home_address = "15, Agege moto rd, lagos Nigeria"  #still on variables
print(home_address + " is the location") #printing the variable

phrase = "Life is good" #variable
print(phrase + ", make it count") #variable with concatenation

print(phrase.lower()) #This is a function, this function renders the variable as lower case
print(phrase.upper()) #This is a function, this function renders the variable as UPPER case
print(phrase.isupper()) #This is a function, this function checks if the variable is in UPPER case
print(phrase.islower()) #This is a function, this function checks if the variable is in lower case
print(phrase.upper().isupper()) #This is a multi-function, first function converts to UPPER, second checks if the variable is in UPPER case
print(len(phrase)) #This is a function that count & prints the number of characters in the variable phrase
print(phrase[6]) #This is a function that identify & returns character in the position stated
print(phrase.index("e")) #This is a function that identify & returns the position of a specified character
print(phrase.replace("good", "beautiful"))
