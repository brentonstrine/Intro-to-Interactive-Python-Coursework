import simplegui
import random
secret_number = 0
upper_bound = 100
guesses_left = 0

def new_game():
    global secret_number, upper_bound, guesses_left
    secret_number = random.randrange(0,upper_bound)
    if(upper_bound==100):    
        guesses_left = 7
    else:
        guesses_left = 10
    
    print "\n", "New Game!", "\n"

# define event handlers for control panel
def range100():
    global upper_bound
    upper_bound = 100
    new_game()

def range1000():
    global upper_bound
    upper_bound = 1000
    new_game()
    
def input_guess(guess):
    global guesses_left
    guess = int(guess)
    print "Guess was ", guess
    guesses_left = guesses_left - 1
    print "Number of guesses left: ", guesses_left
    if(secret_number > guess):
        print "Higher"
    elif(secret_number < guess):
        print "Lower"
    elif(secret_number == guess):
        print "Correct"
        new_game()
    else:
        print "Error!"
    if(guesses_left == 0):
        print "You're out of guesses! You lose!"
        new_game()
    
# create frame
f = simplegui.create_frame("Guess the Number",300,300)


# register event handlers for control elements and start frame
f.add_input("Your Guess", input_guess, 100)
f.add_button("Range: 0 - 100", range100, 100)
f.add_button("Range: 0 - 1000", range1000, 100)


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
