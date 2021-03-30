shopping_list = ["milk", "pasta", "eggs", "bacon", "bread", "rice"]

for item in shopping_list:
	if item != "bacon":
		print("Buy " + item)
print("-" * 10)
for item in shopping_list:
	if item == "bacon":
		continue    # Not used very often and you don't really ever need to use it.

	print("Buy " + item)

