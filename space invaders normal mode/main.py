import pgzrun
WIDTH = 600
HEIGHT = 800
TITLE = 'Space Invaders -normal mode-'
buggys = []
dont_know = []
ship = Actor('galaga')
ship.x = 300
ship.y = 750
score = 0
game_on = True

for i in range(5):
    for j in range(5):
        bug = Actor('bug')
        bug.x = 80*j +135
        bug.y = 70*i +100
        buggys.append(bug)


    

def draw():
    global buggys, bug, pew_pew, score
    screen.clear()
    for i in dont_know:
        i.draw()
    ship.draw()
    for bug in buggys:
        bug.draw()
    screen.draw.text(f'score = {score}',(50,10),fontsize = 30)
    if game_on == 'lost':
        screen.fill('black')

def update():
    global buggys,bug,score,game_on
    if keyboard.left:
        ship.x = ship.x - 10
    if keyboard.right:
        ship.x = ship.x + 10
    for i in dont_know:
        i.y =i.y-10
    for bug in buggys:
        bug.y = bug.y+0.3
        for i in dont_know:
            if bug.colliderect(i):
                dont_know.remove(i)
                buggys.remove(bug)
                score = score + 1  
        if bug.colliderect(ship):
            game_on = 'lost'

def on_key_down(key):
    global pew_pew
    if key == keys.SPACE:
        pew_pew = Actor('bullet')
        pew_pew.x = ship.x
        pew_pew.y = ship.y
        dont_know.append(pew_pew)

def game_lost():
    pass

pgzrun.go()