films = {
	"Finding Dory":{"age_rating":3,"seats":5},
	"Bourne":{"age_rating":18,"seats":5},
	"Tarzan":{"age_rating":15,"seats":5},
	"Ghost Busters":{"age_rating":12,"seats":5}
	}

while True:
	choice = input("What film do you want to see?: ").strip().title()
	if choice in films:
		#pass

		# Age checking

		age = int(input("How old are you?: ").strip())

		if age >= films[choice]["age_rating"]:
			pass
		else:
			print("You are too young to watch that film")

	else:
		print("We don't have that film ...")


	
