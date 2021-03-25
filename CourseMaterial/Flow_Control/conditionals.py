name = input("Please eneter your name: ")
age = int(input("how old are you, {0}? ".format(name)))
print(age)
# Python uses indentation to process logic in code blocks
# if age >= 18:
# 	print("You are old enough to vote!")
# else:
# 	print("Please come back in {0} years".format(18 - age))

if age < 18:
	print("Please come back in {0} years".format(18 - age))
elif age == 900:
	print("Sorry that can't happen.")
else:
	print("You are old enough to vote!")


