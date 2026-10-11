from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

x = 2
y = 1
game_over = False
score = -1  # 0 ha az első cső előtt esik le

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
    if game_space[x * 8 + y] == r:
        game_over = True


# joy DOWN - jump
def jump(event):
    global x
    if event.action == "pressed":
        if event.direction == "down":
            if x >= 3:
                x -= 3
            else:
                x = 0


# Create a function to make pipes
def pipe_generator(space):
    # create a single column of red pixels on the right-hand side
    for row in range(7, 64, 8):
        space[row] = r
    
    # insert a gap into the pipe through which the bird can fly
    # the gap is three pixel high
    gap = randint(0, 5)

    for i in range(3):
        space[(gap + i) * 8 + 7] = o
    return space


# Move all pipes left
def move_pipes(space):
    # shift colums from right to left
    for col in range(7):
        for row in range(8):
            space[row * 8 + col] = space[row * 8 + col + 1]

    # clear last column
    for row in range(7, 64, 8):
        space[row] = o
    return space


def main():
    global game_space
    global game_over
    global score
    global x, y

    sense.stick.direction_any = jump
    
    while not game_over:
        game_space = pipe_generator(game_space)
        
        x += 1
        if x >= 8:  # leesett
            game_over = True
            break

        check_collision()
        if game_over:
            break

        sense.set_pixels(game_space)
        sense.set_pixel(y, x, w)

        for i in range(4):
            sleep(0.5)
            if game_over:
                break

            x += 1
            if x >= 8:  # leesett
                game_over = True
                break

            game_space = move_pipes(game_space)
            check_collision()
            if game_over:
                break

            sense.set_pixels(game_space)
            sense.set_pixel(y, x, w)
        
        if not game_over:
            score += 1
        
        sleep(0.5)


    sense.clear()
    sense.show_message("You lose", scroll_speed=0.05, back_colour=o)
    sense.show_message("Score: " + str(score), scroll_speed=0.05, back_colour=o)


if __name__ == "__main__":
    main()
