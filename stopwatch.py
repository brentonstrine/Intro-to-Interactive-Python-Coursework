# template for "Stopwatch: The Game"
import simplegui

# define global variables
ticks = 0
time = ""
handCS = [125,0]
handS = [125,0]
handM = [125,0]


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    cs = t % 10
    s = (t / 10) % 60
    m = (t / 600) % 60
    return str(m) + ":" + str(s) + "." + str(cs)
    
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
    global time, ticks, handCS, handS, handM
    ticks = ticks + 1
    handCS = setPos("cs")
    handS = setPos("s")
    handM = setPos("m")
    time = format(ticks)
    
def setPos(handType):
    mltplr = 0
    pxlCnvt = 16.66666666
    if(handType=="cs"):
        mltplr = 1
        tick = (ticks % 10) / (pxlCnvt / 100)
        hand = [handCS[0],handCS[1]]
    elif(handType=="s"):
        tick = (ticks % 600) / 10
        hand = [handS[0],handS[1]]
    elif(handType=="m"):
        tick = (ticks % 36000) / 600
        hand = [handM[0],handM[1]]
        
    if(tick<=(7.5)):
        hand[0] = (tick * pxlCnvt) + 125
        debug = hand
    elif(tick<=(22.5)):
        hand[0] = 250
        hand[1] = (tick -7.5) * pxlCnvt
        debug = hand
    elif(tick<=(37.5)):
        hand[0] = ((tick - 22.5) * -1 * pxlCnvt) + 250
        hand[1] = 250
        debug = hand
    elif(tick<=(52.5)):
        hand[0] = 0
        hand[1] =  ((tick - 37.5) * -1 * pxlCnvt) + 250
    elif(tick<=(60)):
        hand[0] = ((tick - 52.5) * pxlCnvt)
        hand[1] = 0
    return hand

# define draw handler
def draw(canvas):
    canvas.draw_text(str(time), [100,210], 26, "Red")
    canvas.draw_line([125,125],handCS,1,"red")
    
    canvas.draw_line([123,123],handS,1,"#aae")
    canvas.draw_line([127,123],handS,1,"#bbd")
    canvas.draw_line([125,125],handS,2,"#00f")
    canvas.draw_line([127,127],handS,1,"#ccc")
    canvas.draw_line([123,127],handS,1,"#ddb")
    
    canvas.draw_line([123,123],handM,2,"#aaa")
    canvas.draw_line([127,123],handM,2,"#bbb")
    canvas.draw_line([127,127],handM,2,"#ccc")
    canvas.draw_line([123,127],handM,2,"#ddd")
    canvas.draw_line([125,125],handM,2,"#fff")
    
    canvas.draw_circle([125,125], 155, 50, "black")
    canvas.draw_circle([125,125], 1, 5, "white")

    
# create frame
frame = simplegui.create_frame("Timer Game", 250, 250)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, clock)

# start frame
frame.start()
timer.start()
