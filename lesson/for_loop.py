#The while loop keeps looping while its condition is
#True (which is the reason for its name),
#but what if you want to execute a block of code only a
#certain number of times? You can do this with a for loop statement and the
#range() function.

for letter in "Giraffe Academy":
    print(letter)

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")

friends = ["Sodiq", "Mark", "Saheed"]
for names in friends:
    print(names)


for index in range(10):
    print(index)


for index in range(3, 10):
    print(index)

fruits = ["Mango", "Banana", "Orange"]
for index in range(len(fruits)):
    print(fruits[index])