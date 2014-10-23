# template for "Stopwatch: The Game"
import simplegui

# define global variables
s = 0
m = 0
cs = 0
ticks = 0
time = ""
handCS = [12,0]
handS = [125,0]
handM = [255,0]
sTick = [0,0]
mTick = [0,0]
csTick = [0,0]


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    print "start!"
    pass
def stop():
    pass
def reset():
    pass

# define event handler for timer with 0.1 sec interval
def clock():
    global cs, s, m, csTick, sTick, mTick, time, ticks, handCS, handS, handM
    ticks = ticks + 1
    cs = cs + 1
    handCS = setPos("cs")
    handS = setPos("s")
    #handM = setPos("m")
    
        
    seconds = ticks / 10;
    milliseconds = ticks % 10;
    minute = ticks / 600
    s = seconds
    if(milliseconds==0): 
        sTick = [handS[0], handS[1]]
    time = str(minute) + ":" + str(seconds) + "." + str(milliseconds)
    
def setPos(handType):
    mltplr = 0
    if(handType=="cs"):
        mltplr = 1
        hand = [handCS[0],handCS[1]]
    elif(handType=="s"):
        mltplr = 6
        hand = [handS[0],handS[1]]
    elif(handType=="m"):
        mltplr = 60
        hand = [handM[0],handM[1]]
        
    if(ticks<=(12.5*mltplr)):
        hand[0] = (ticks * 10 / mltplr + 125)
    elif(ticks<=(37.5*mltplr)):
        hand[1] = ticks * 10 / mltplr - 125
    elif(ticks<=(62.5*mltplr)):
        hand[0] = ( (ticks * 10 / mltplr - 375) * -1 ) + 250
    elif(ticks<=(87.5*mltplr)):
        hand[1] = ( (ticks * 10 / mltplr - 625) * -1 ) + 250
    elif(ticks<(100*mltplr)):
        hand[0] = (ticks * 10 / mltplr - 875)
    
    print handType
    print ticks % 1000
    print "\n"
    return hand
        

# define draw handler
def draw(canvas):
    canvas.draw_text(str(time), [0,250], 36, "Red")
    canvas.draw_text(str(handCS), [0,36], 36, "Red")
    canvas.draw_line([125,125],handCS,1,"red")
    canvas.draw_line([125,125],sTick,2,"green")
    canvas.draw_line([125,125],handS,1,"green")
    #canvas.draw_line([125,125],handS,1,"green")
    #canvas.draw_line([125,125],handM,2,"green")

    
# create frame
frame = simplegui.create_frame("Timer Game", 250, 250)


# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(1000, clock)


# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
