count = 0
run = True

while run:
	
	try:
		word = input("Please input a string: ")
	except EOFError:
		print("Bye")
		break

	word_list = word.split(" ")

	for i in word_list:
		if i == "the" or i == "The":
			count += 1
		elif i == "exit" or i == "Exit":
			run = False	

	print("Count: " + str(count))
