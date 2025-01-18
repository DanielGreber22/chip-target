import random
import pgzrun 
import itertools

WIDTH = 400
HEIGHT = 400

BLOCK_POS = [
    (350,50),(350,350),(50,350),(50,50)
]
block_pos = itertools.cycle(BLOCK_POS)

block = Actor('the_thing', center=(50, 50))
ship = Actor('chip', center=(200, 200))


def draw():
    screen.clear()
    block.draw()
    ship.draw()

def move_block():
    animate(block,"bounce_end",duration = 1,pos = next(block_pos))

move_block()
clock.schedule_interval(move_block,2)

def ship_target():
    x = random.randint(100,300)
    y = random.randint(100,300)
    
    ship.target = x,y
    target_angle = ship.angle_to(ship.target)

    target_angle += 360 * ((ship.angle - target_angle + 180)//360)

    animate(ship,angle = target_angle ,duration = 0.3,on_finished = move_ship)


def move_ship():
    """Move the ship to the target."""
    anim = animate(
        ship,
        tween='accel_decel',
        pos=ship.target,
        duration=ship.distance_to(ship.target) / 200,
        on_finished=ship_target,)
ship_target()
    
pgzrun.go()
