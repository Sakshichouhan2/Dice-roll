'''“Dice-roll" that generates the random value between 1 and 6 every minute . and sends 
to Redis“Sender" that reads the value from Redis and pushes to SQS“Reader" that reads 
the value from SQS and prints it to the stdout. Ideally,A reader could be deployed in 
AWS.'''

import random
 
try:
    min_dice = 1
    max_dice = 6
except:
    print('Input invalid program will revert to defaults.')

    #Sender
    file = open("dice.txt",'r')
    
   
again = True
 
while again:
 
    print(random.randint(min_dice, max_dice))
 
    dice_again = input('Want to roll the dice again? ')
 
    if dice_again.lower() == 'yes' or dice_again.lower() == 'y' or dice_again.upper() == "Yes" or dice_again.upper() == "Y":
        continue
    else:
        break
