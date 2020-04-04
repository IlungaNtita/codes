#coin flip game
import random

luck = ("Head","Tails")
score=1

while True:
	if input("Would you like to flip a coin? \nType yes or no: ") == "yes":
	    print(random.choice(luck))
	else:
		#return "Heads {}\n Tails {}".format(Heads,Tails)
		break
