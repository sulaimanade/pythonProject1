#NUMBERS: working with numbers
print(5+2)
print(5-2)
print(5*2)
print(5/2) #normal division
print(5//2) #division with exact value, no decimal
print(5%2) #division with only remainder after decimal

#use parenthesis to arrange the order of calculation
print(2 * 3 + 5) #this will execute in order, from 2 to 3 to 5
print(2 * (3 + 5)) #but this will first calculate 3+5, then add it to 2

#storing numbers with variables
my_phone = 7012345678 #here I have saved my mobile numbere inside the variable my_phone
print(my_phone)
print(str(my_phone) + ", is my phone number") #here I am calling the variable, convert it to a string and concatenate with other

#numbers and functions
print(pow(2, 3))
print(min(7, 4, 3, 8, 7))
print(max(10, 400, 20, 450, 270))
print(round(230.572))
