'''“Dice-roll" that generates the random value between 1 and 6 every minute . and sends 
to Redis“Sender" that reads the value from Redis and pushes to SQS“Reader" that reads 
the value from SQS and prints it to the stdout. Ideally,A reader could be deployed in 
AWS.'''

import random
min = 1
max = 6
roll_dice = "Yes" or "yes" or "Y" or "y"
while roll_dice == "Yes" or "yes" or "Y" or "y":
	print("Rolling the dices ")
	print("The values are  ")
	print(random.randint(min,max))
	print(random.randint(min,max))


	roll_again = input("Roll the dices again: ")


