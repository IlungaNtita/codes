#rock, paper scisors
import random

games=1
score=0
#r<p<s
print('Lets play Rock, Paper, Scicor!')
while True:
	#user inputs
	p="p"
	s="s"
	r="r"
	
	r=("Rock","Paper","Scicor")
	computer=random.choice(r)
	i=input("Type in r for Rock, p for Paper and s for Scicor: ")
	
	if i == r and computer == "Scicor":
		print(computer)
		print("You won!")
		score += 1
		games = games + 1
		
	elif i == p and computer == "Rock":
		print(computer)
		print("You won!")
		score += 1
		games = games + 1
		
	elif i == s and computer == "Paper":
		print(computer)
		print("You won!")
		score += 1	
		games = games + 1	
		
	elif games == 5:
		break
		
	else:
		print(computer)
		print("You lost")
		games = games + 1
		
print("Your score: {}".format(score))
  
