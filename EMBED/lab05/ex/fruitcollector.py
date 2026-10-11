from sense_hat import SenseHat
from random import randint
from time import sleep, time

sense = SenseHat()

w = (255, 255, 255)
r = (255, 0, 0)
b = (0, 0, 0)

basket = [4, 4]
fruit = [0, 0]

def generate_fruit():
    global fruit, basket
    fruit = [randint(0, 7), randint(0, 7)]
    while fruit == basket:
        fruit = [randint(0, 7), randint(0, 7)]
generate_fruit()

score = 0
game_over = False


def draw_game():
    global basket, fruit

    sense.clear()
    sense.set_pixel(basket[1], basket[0], w)
    sense.set_pixel(fruit[1], fruit[0], r)


def move_basket(event):
    global basket

    if event.action == "pressed":
        if event.direction == "up" and basket[0] > 0:
            basket[0] -= 1
        elif event.direction == "down" and basket[0] < 7:
            basket[0] += 1
        elif event.direction == "left" and basket[1] > 0:
            basket[1] -= 1
        elif event.direction == "right" and basket[1] < 7:
            basket[1] += 1


def check_collision():
    global basket, fruit
    global score

    if basket == fruit:
        score += 1
        return True
    return False
        

def main():
    start_time = time()
    duration = 30
    
    sense.stick.direction_any = move_basket
    sense.clear(b)

    while time() - start_time < duration:
        if check_collision():
            generate_fruit()
        draw_game()
        sleep(0.05)


    sense.clear()
    sense.show_message("Time!", scroll_speed=0.05, back_colour=b)
    sense.show_message("Score: " + str(score), back_colour=b, scroll_speed=0.05)


if __name__ == "__main__":
    main()
