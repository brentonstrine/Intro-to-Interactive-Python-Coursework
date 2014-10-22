# Rock-paper-scissors-lizard-Spock template

import random

# helper functions

def name_to_number(name):
    number = 0

    if(name=="rock"):
        number = 0
    elif(name=="Spock"):
        number = 1
    elif(name=="paper"):
        number = 2
    elif(name=="lizard"):
        number = 3
    elif(name=="scissors"):
        number = 4
        
    return number

def number_to_name(number):
    name = ""

    if(number==0):
        name = "rock"
    elif(number==1):
        name = "Spock"
    elif(number==2):
        name = "paper"
    elif(number==3):
        name = "lizard"
    elif(number==4):
        name = "scissors"
        
    return name
    

def rpsls(player_choice):
    print "\n"
    print "Player chooses " + player_choice

    # convert the player's choice number
    player_number = name_to_number(player_choice)
    
    # compute random guess
    comp_number = random.randrange(0,5)
    
    # convert comp_number to name
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5

    # use if/elif/else to determine winner, print winner message
    if(diff >= 3):
        print "Player wins!"
    elif(diff >= 1):
        print "Computer wins!"
    else:
        print "Player and computer tie!"
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
