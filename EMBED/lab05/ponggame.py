from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()

speed = 0.3
bat = [7,4]
score = 0
up_down = -1

w = (0,0,0)
r = (255,0,0)
b = (0,0,255)

game_space = [
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,b,b,w,w,w]

def update_space(x, y, colour):
    p = 8 * x + y
    game_space[p] = colour
    sense.set_pixels(game_space)

def left(event):
    if event.action == "pressed":
        if bat[1] - 1 == 0:
            pass
        else:
            update_space(bat[0], bat[1], w)
            bat[1] -= 1
            update_space(bat[0], bat[1] - 1, b)
    
def right(event):
    if event.action == "pressed":
        if bat[1] + 1 == 8:
            pass
        else:
            update_space(bat[0], bat[1] - 1, w)
            bat[1] += 1
            update_space(bat[0], bat[1], b)


# triggering function calls with joystick
sense.stick.direction_left = left
sense.stick.direction_right = right

# initialize game
sense.clear()
sense.set_pixels(game_space)
game_alive = True

# initial position and direction of the ball
x = 0
y = random.randint(0,7)
d = random.choice([-1, 0, 1])
#put the ball into the game_space
update_space(x, y, r)

def main():
    # game loop
    while game_alive:
        sleep(speed)
        update_space(x, y, w)
        # ball is out of the space at bottom
        if x == 7:
            if y == bat[1]-1 or y == bat[1]:
                # ball is on the bat
                update_space(x, y, b)
                score += 1
                d = random.choice([-1, 0, 1])
                up_down = -1
            else:
                #ball is out of the space
                game_alive = False
                break
        elif x == 0:
            # ball is on the top
            up_down = 1
            d = random.choice([-1, 0, 1])

        # ball reached the right side of space
        if y == 7 and d == 1:
            d = random.choice([-1, 0])
        # ball reached the left side of space
        elif y == 0 and d == -1:
            d = random.choice([0, 1])

        x += up_down
        y += d
        update_space(x, y, r)

    
    sense.clear()
    sense.show_message("Game over!", scroll_speed=0.05, back_colour=w)
    sense.show_message("Score: " + str(score), scroll_speed=0.1, back_colour=w)

if __name__ == "__main__":
    main()
    