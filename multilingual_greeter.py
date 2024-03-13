def greet(name): #function greet takes 'name' as parameter 
	print("Hello " + name + " How are you! ")


def name_input(): # function name_input with no parameter
	name = input("Enter your name: ")
	print(name)


def language_input(): #function to offer user to select a language
	option = input(("Choose a language 1.English 2. Spanish 3. French :"))
	if option==1:
		print("Nice to meet you  " + name)
	elif option==2:
		print("Encantada de conocerte " + name)
	else:
		print("Ravi de vous rencontrer" + name)


name = input("What's your name" )
greet(name)
name_input()
language_input()