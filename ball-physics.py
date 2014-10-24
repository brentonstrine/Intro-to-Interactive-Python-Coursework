import simplegui
import random
import math

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-990.0 / 60.0,  990.0 / 60.0]

max = 0

# define event handlers
def keydown(key):
    global vel
    if key == simplegui.KEY_MAP["left"]:
        vel[0] -= 1
    elif key == simplegui.KEY_MAP["right"]:
        vel[0] += 1
    elif key == simplegui.KEY_MAP["down"]:
        vel[1] += 1
    elif key == simplegui.KEY_MAP["up"]:
        vel[1] -= 1   
        
def draw(canvas):
    # Gravity and air resistance
    vel[0] = vel[0] / 1.005
    vel[1] = (vel[1] + .8) / 1.005

    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS:
       ball_pos[0] = BALL_RADIUS
       vel[0] = - (vel[0] / 1.0001)
        
    if ball_pos[0] >= WIDTH - 1 -BALL_RADIUS:
       ball_pos[0] = WIDTH - 1 -BALL_RADIUS
       vel[0] = - (vel[0] / 1.0001)
        
    if ball_pos[1] <= BALL_RADIUS:
       ball_pos[1] = BALL_RADIUS
       vel[1] = - (vel[1] / 1.1)
        
    if ball_pos[1] >= HEIGHT - 1 -BALL_RADIUS:
       ball_pos[1] = HEIGHT - 1 -BALL_RADIUS
       vel[1] = - (vel[1] / 1.1)
         
       if(vel[1] <= 1 and vel[1] >= -1):
        vel[1] = vel[1] / 2
       if(vel[1] <= .4 and vel[1] >= -.4):
        vel[1] = 0
        
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    
    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    canvas.draw_text(str(vel[1]), [20,20], 20, "white")

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)


# start frame
frame.start()
