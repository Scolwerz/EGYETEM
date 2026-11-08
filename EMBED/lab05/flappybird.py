from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()
x = 0
y = 0
game_over = False

r = (255, 0, 0)
o = (0, 0, 0)
w = (255, 255, 255)

game_space = [
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o]

# detect collision between the bird and pipes
def check_collision():
    global game_over
    if game_space[x*8 + y] == r:
        game_over = True

# Moving the bird upward
def draw_bird(event):
    global x
    global y
    # clear previous bird position
    sense.set_pixel(y, x, o)
    # set new bird position
    if event.action == "pressed":
        if event.direction == "up" and x > 0:
            x -= 1
        elif event.direction == "down" and x < 7:
            x += 1
        elif event.direction == "right" and y < 7:
            y += 1
        elif event.direction == "left" and y > 0:
            y -= 1
    # the set_pixel() function use reversed axes indexing
    sense.set_pixel(y, x, w)

# Create a function to make pipes
def pipe_generator(space):
    # create a single column of red pixels on the right-hand side
    for row in range(7,64,8):
        space[row] = r

    # insert a gap into the pipe through which the bird can fly
    # the gap is three pixel high
    gap = randint(0, 5)

    for i in range(3):
        space[(gap+i) * 8 + 7] = o
    return space


def move_pipes(space):
    # shift colums from right to left
    for col in range(7):
        for row in range(8):
            space[row*8 + col] = space[row*8 + col + 1]

    # clear last column
    for row in range(7,64,8):
        space[row] = o
    return space


def main():
    global game_space
    
    sense.stick.direction_any = draw_bird
    while not game_over:
        game_space = pipe_generator(game_space)
        for i in range(4):
            sense.set_pixels(game_space)
            sense.set_pixel(y, x, w)
            check_collision()
            game_space = move_pipes(game_space)
            sleep(0.5)

    sense.show_message('You lose')


if __name__ == "__main__":
    main()