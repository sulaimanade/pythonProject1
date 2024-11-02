from getpass import fallback_getpass

is_male = False

if is_male:
    print("You are a male")


#OR
#using OR in if statement, where one of two conditions is true or false
is_boy = False
is_tall = False

if is_boy or is_tall:
    print("You are a boy or tall or both")
else:
    print("You are neither a boy nor tall")


#AND
#using AND in if statement, where two conditions are both true
is_girl = True
is_fat = True

if is_girl and is_fat:
    print("You are a fat girl")
else:
    print("You are either not a girl or not short or both")


#AND #NOT
#using AND and NOT in a if statement, where the condition is mixed

is_black = False
is_american = False

if is_black and is_american:
    print("You are a black american")
elif is_black and not (is_american):
    print("you are black but not american")
elif not(is_black) and is_american:
    print("You are not a black, but you are american")
else:
    print("You are not a black and not american")
