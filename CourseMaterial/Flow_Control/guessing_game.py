answer = 5
print("Please guess a number between 1 and 10: ")
guess = int(input())

# if guess < answer:
# 	print("Please guess higher")
# 	guess = int(input())
# 	if guess == answer:
# 		print("Well done, you guessed it")
# 	else:
# 		print("Sorry you have not guess correctly")
# elif guess > answer:
# 	print("Please guess lower")
# 	guess = int(input())
# 	if guess == answer:
# 		print("Well done, you guessed it")
# 	else:
# 		print("Sorry you have not guess correctly")
# else:
# 	print("You got it the first time")

"""
if blocks
1. Block can be complex, including further if and else blocks
2. When testing for equality, we can't use a single = symbol. Single = indicates assigning a value 
to a variable, so we use the == to test for equality
3. Statement can include many elif statements, but only one else
4. The else, if there is one, must come after all elif blocks
5. Duplicating code is generally a bad idea, there's almost always a better way
"""
if guess != answer:
	if guess < answer:
		print("Please guess higher")
	else:
		print("Please guess lower")
	guess = int(input())
	if guess == answer:
		print("Well done, you guessed it")
	else:
		print("Sorry you have not guessed correctly")
else:
	print("You smart cookie you, first try!")