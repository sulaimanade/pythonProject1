#secrete_word = "Dolphin"
#guess = ""

#while guess != secrete_word:
#    guess = input("Enter guess: ")

#print("You win!")

#=====================

secrete_word = "Dolphin"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secrete_word and  not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You Lose!")
else:
    print("You win!")