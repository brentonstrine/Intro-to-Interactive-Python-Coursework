import simplegui
import random
secret_number = 0

def new_game():
    global secret_number
    secret_number = random.randrange(0,100)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    pass
    
def input_guess(guess):
    guess = int(guess)
    print "Guess was ", guess
    if(secret_number > guess):
        print "Higher"
    elif(secret_number < guess):
        print "Lower"
    elif(secret_number == guess):
        new_game()
        print "Correct"
    else:
        print "Error!"

    
# create frame
f = simplegui.create_frame("Guess the Number",300,300)


# register event handlers for control elements and start frame
f.add_input("Your Guess", input_guess, 100)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
