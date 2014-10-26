# implementation of card game - Memory

import simplegui
import random

turn = 0
guesses = []
cards = range(16)
flipped = {}

# helper function to initialize globals
def new_game():
    global guesses, cards, flipped
    guesses = []
    flipped = {}
    cards = range(8) + range(8)
    random.shuffle(cards)
    print cards
    
    #guesses, cards, guessed zeroed
    #cards = range(8), concat to self.randomize order
    
    pass
    
    
def evaluate_match():
        global guesses, cards
        #if not flipped && not current 
    
        #if guesses.len() = 1, move on
        print "guesses: ", guesses
        if(len(guesses)==1):
            # if guesses.len() = 2, compare
            return False
        elif(len(guesses)==2):
            if(cards[guesses[0]]==cards[guesses[1]]):
                return True
            else:
                return False
        #if guesses.len=3, erase guesses
        elif(len(guesses)==3):
            guesses = [guesses[2]]
#            add first to guesses
        #elif(len(guesses)==3):
        #    guesses = []
    # else unflip


     
# define event handlers
def mouseclick(pos):
    global flipped, guesses, turn
    # which card was clicked. 
    guess = pos[0] / 50
    if(guess in guesses) or (guess in flipped):
        return True
    else:
        turn += 1
        label.set_text("Turns = " + str(turn / 2))
        guesses.append(guess)

    if(evaluate_match()):
        #add guessed cards to permanent flip
        flipped[guesses[0]] = True
        flipped[guesses[1]] = True
    else:
        pass
        

    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global guesses, cards
    #draw lines
    for line in range(16):
        x = line * 50
        canvas.draw_line((x, 0), (x, 100), 1, '#666')
        
    
    #draw guessed cards
    for idx in guesses:
        posS = idx * 50
        posE = posS + 50
        topright = [posS, 0]
        topleft = [posE, 0]
        bottomright = [posS, 100]
        bottomleft = [posE, 100]
        num = str(cards[idx])        
        canvas.draw_polygon([topleft, topright, bottomright, bottomleft], 1, "#fff", "#fcd")
        canvas.draw_text(num,[posS + 18, 60], 30, "#000")

    
    #draw flipped cards
    for idx in flipped:
        posS = idx * 50
        posE = posS + 50
        topright = [posS, 0]
        topleft = [posE, 0]
        bottomright = [posS, 100]
        bottomleft = [posE, 100]
        num = str(cards[idx])        
        canvas.draw_polygon([topleft, topright, bottomright, bottomleft], 1, "#fff", "#afd")
        canvas.draw_text(num,[posS + 15, 60], 30, "#000")


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
