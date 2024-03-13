from random import randint

user_num = int(input("Enter a number between 1 and 10 : "))


def generate_random_num():
	random_num=randint(1, 10)
	return random_num


def checknum(random_num, user_num):
	if user_num == random_num:
		return "correct"
	elif user_num < random_num:
		return "too low"
	else:
		return "too high"


checknum(generate_random_num(), user_num)
print("The random number that was generated : "  + str(generate_random_num()))
generate_random_num()
print("the user's guess : " + str(user_num))
#print(Indication : the guess was 
