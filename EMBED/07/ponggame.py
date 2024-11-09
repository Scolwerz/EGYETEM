from sense_hat import SenseHat
import random
from time import sleep

# Initialize Sense HAT and game variables
sense = SenseHat()
speed = 0.4
score = 0
bat = [7, 3]  # The bat's initial position (centered)
up_down = -1  # The vertical direction of the ball (-1 means moving up, +1 moving down)

# Define colors
w = (0, 0, 0)  # White (background color)
r = (255, 0, 0)  # Red (ball color)
b = (0, 0, 255)  # Blue (bat color)

# Set up initial game space
game_space = [w] * 64  # All LEDs off initially
game_space[8 * bat[0] + bat[1]] = b  # Place the bat
game_space[8 * bat[0] + bat[1] - 1] = b  # Left side of the bat
game_space[8 * bat[0] + bat[1] + 1] = b  # Right side of the bat


def update_space(x, y, colour):
    """Update the LED at (x, y) to the specified colour."""
    p = 8 * x + y
    game_space[p] = colour
    sense.set_pixels(game_space)


def left(event):
    """Move the bat left if possible."""
    if event.action == 'pressed' and bat[1] > 1:
        update_space(bat[0], bat[1] + 1, w)
        bat[1] -= 1
        update_space(bat[0], bat[1] - 1, b)


def right(event):
    """Move the bat right if possible."""
    if event.action == 'pressed' and bat[1] < 6:
        update_space(bat[0], bat[1] - 1, w)
        bat[1] += 1
        update_space(bat[0], bat[1] + 1, b)


# Joystick event bindings
sense.stick.direction_left = left
sense.stick.direction_right = right

# Initialize game
sense.clear()
sense.set_pixels(game_space)
game_alive = True

# Initialize ball position and direction
x, y = 0, random.randint(0, 7)
d = random.choice([-1, 1])  # Ball's horizontal direction
update_space(x, y, r)

# Game loop
while game_alive:
    sleep(speed)
    update_space(x, y, w)

    # Check for vertical collision
    if x == 7:
        if y in (bat[1] - 1, bat[1], bat[1] + 1):  # Ball hits the bat
            up_down = -1  # Change direction to up
            score += 1
        else:  # Ball misses the bat
            game_alive = False
            break
    elif x == 0:  # Ball hits the top wall
        up_down = 1  # Change direction to down

    # Check for horizontal collision
    if y == 7 and d == 1:  # Ball hits the right wall
        d = -1
    elif y == 0 and d == -1:  # Ball hits the left wall
        d = 1

    # Update ball position
    x += up_down
    y += d
    update_space(x, y, r)

# End game: Display score and "Game over" message
sense.clear()
sense.show_message('Game over!', scroll_speed=0.05, back_colour=w)
sense.show_message('Score: ' + str(score), scroll_speed=0.05, back_colour=w)
