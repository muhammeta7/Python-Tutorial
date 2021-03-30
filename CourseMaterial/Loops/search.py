shopping_list = ["milk", "pasta", "eggs", "bacon", "bread", "rice"]

item_to_find = "bacon"
found_at = None

for index in range(len(shopping_list)):
	if shopping_list[index] == item_to_find:
		found_at = index
		break   # jump out of loop making it more efficient
print("Item found at position {}".format(found_at))