input_string = input("Please enter a sentence: ")

string_list = input_string.split(" ")
the_counter = 0

for i in string_list:
	if i == "the":
		the_counter += 1
	elif i == "The":
		the_counter += 1

if the_counter == 0:
	print("No instances of \"the\" were found ")
else:
	print("There are " + str(the_counter) + " the's")
