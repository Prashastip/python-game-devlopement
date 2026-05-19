import random
import pgzrun

WIDTH=500
HEIGHT=500

message=""
score=0

alien=Actor("alien")

# alien.x=60
# alien.y=70
def move():
    alien.pos=(random.randint(50,WIDTH-50),random.randint(50,HEIGHT-50))

TITLE="Shoot the alien"

def draw():
    screen.fill("maroon")
    alien.draw()
    screen.draw.text(message,center=(100,50),fontsize=31)
    screen.draw.text("score:"+str(score),center=(400,50),fontsize=31)

def update():
    pass

def on_mouse_down(pos):
    global message
    global score
    if alien.collidepoint(pos):
        move()
        score=score+1
        message="Good shot!"
    else: 
        score=score-1
        message="You missed!"

    if score>5:
        screen.fill("green")
        message="You Win!"


move()
pgzrun.go()