import pgzrun
WIDTH=500
HEIGHT=500
TITLE="Collecting honey"
score=0
bee=Actor("bee")
bee.pos=100,100

flower=Actor("flower")
flower.pos=200,100




def draw():
    screen.blit("background",(0,0))
    flower.draw()
    bee.draw()

def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2
        if bee.x<0:
            bee.x=100
    if keyboard.right:
        bee.x=bee.x+2
        if bee.x>500:
            bee.x=100
    if keyboard.up:
        bee.y-=2
        if bee.y<0:
            bee.y=100
    if keyboard.down:
        bee.y+=2
        if bee.y>500:
            bee.y=100






pgzrun.go()