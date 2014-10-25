# Paste this code into http://www.codeskulptor.org/ to see it work. 

# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [0,0]
score1 = 0
score2 = 0
paddle1_pos = HEIGHT/2
paddle1_vel = 0.0
paddle2_pos = HEIGHT/2
paddle2_vel = 0.0
paddle_speed = 200 / 60


def spawn_ball(direction):
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
    paddle1_pos = HALF_PAD_HEIGHT #HEIGHT/2
    paddle1_vel = 0.0
    paddle2_pos = HEIGHT/2
    paddle2_vel = 0.0
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [random.randrange(120, 240)/60.0 * direction, random.randrange(60, 180)/60.0]
    


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(-1)


def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_speed
    if(paddle_speed < ball_vel[1]/2):
        paddle_speed = ball_vel[1] * 2
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = - paddle_speed
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_speed
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = - paddle_speed
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_speed

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # paddle bounces
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
       ball_pos[0]  = BALL_RADIUS + PAD_WIDTH + 1 #prevent bounce errors
       if(ball_pos[1] > paddle1_pos - HALF_PAD_HEIGHT) and (ball_pos[1] < paddle1_pos + HALF_PAD_HEIGHT):
        ball_vel[0] = - (ball_vel[0] * 1.1)
       else:
        score2 += 1
        spawn_ball(1)
        
    if ball_pos[0] >= WIDTH - 2 - BALL_RADIUS - PAD_WIDTH:
       ball_pos[0]  = WIDTH - 3 - BALL_RADIUS - PAD_WIDTH
       if(ball_pos[1] > paddle2_pos - HALF_PAD_HEIGHT) and (ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT):
        ball_vel[0] = - (ball_vel[0] * 1.1)
       else:
        score1 += 1
        spawn_ball(-1)
        
    if ball_pos[1] <= BALL_RADIUS:
       ball_pos[1] = BALL_RADIUS
       ball_vel[1] = - ball_vel[1]
        
    if ball_pos[1] >= HEIGHT - 1 -BALL_RADIUS:
       ball_pos[1] = HEIGHT - 1 -BALL_RADIUS
       ball_vel[1] = - ball_vel[1]
        
    # update ball
    ball_pos[0] += ball_vel[0];
    ball_pos[1] += ball_vel[1];
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

    
    # update paddle's vertical position, keep paddle on the screen
    
    
    paddle1_pos = ball_pos[1]
    if(paddle1_pos - HALF_PAD_HEIGHT + paddle1_vel >= 0) and (paddle1_pos + HALF_PAD_HEIGHT + paddle1_vel <= HEIGHT):
        paddle1_pos += paddle1_vel
    
    #paddle2_pos = ball_pos[1]
    if(paddle2_pos - HALF_PAD_HEIGHT + paddle2_vel >= 0) and (paddle2_pos + HALF_PAD_HEIGHT + paddle2_vel <= HEIGHT):
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[1, paddle1_pos-HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos+HALF_PAD_HEIGHT], [0, paddle1_pos+HALF_PAD_HEIGHT]], 1, "#fff", "#cfd")
    canvas.draw_polygon([[WIDTH, paddle2_pos-HALF_PAD_HEIGHT], [WIDTH-PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT], [WIDTH-PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT], [WIDTH, paddle2_pos+HALF_PAD_HEIGHT]], 1, "#fff", "#fcd")
    
    
    # draw scores
        
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Start Game", new_game)


# start frame
frame.start()
