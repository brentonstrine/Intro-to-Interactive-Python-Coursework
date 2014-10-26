# implementation of card game - Memory

import simplegui
import random


guesses = []
cards = []

# helper function to initialize globals
def new_game():
    global guesses, cards, flipped
    cards = range(8) + range(8)
    random.shuffle(cards)
    print cards
    
    #guesses, cards, guessed zeroed
    #cards = range(8), concat to self.randomize order
    
    pass
    
    
def evaluate_match():
        global guesses
        #if not flipped && not current
        #if guesses.len() = 1, move on
        if(len(guesses)==1):
            return "false"
            # if guesses.len() = 2, compare
            #print len(guesses)
        elif(len(guesses)==2):
            if(guesses[0]==guesses[1]):#get value, not just number
                return "true"
            else:
                return "false"
            guesses = []
        #    if match, return match, else return false. 
        #if guesses.len=3, erase guesses
        #elif(len(guesses)==3):
        #    guesses = []
    # else unflip
    

     
# define event handlers
def mouseclick(pos):
    # which card was clicked. 
    guess = pos[0] / 50
    #print guesses
    # guesses . append()
    guesses.append(guess)
    #print guesses
    # evaluate-match()
    #print evaluate_match()
        
    #if match is true, add cards to list of ignore
    #if guesses.len() < total, you won game
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #draw lines
    
    #draw flipped cards
    
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
