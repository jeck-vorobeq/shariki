import random

import pygame.display

rEGIM_fly = ""
rEGIM = "move"
screen_width, screen_height = [500, 500]
mode = "e_see"
ball_in_second = 1
b = []


def plus_ball():
    global ball_in_second
    ball_in_second = ball_in_second + 1


def minus_ball():
    global ball_in_second
    ball_in_second = ball_in_second - 1
    if ball_in_second < 0:
        ball_in_second = 0


def balls_stop():
    global rEGIM
    rEGIM = "stop"


def balls_move():
    global rEGIM
    rEGIM = "move"


def toggle_fullscreen():
    global screen_height, screen_width
    if screen_height == 500:
        screen = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode([500, 500])
    screen_height = screen.get_height()
    screen_width = screen.get_width()


def all_in_modul():
    print(rEGIM, rEGIM_fly)
    if rEGIM == "fly":
        balls_can_fly()
    if rEGIM == "special":
        balls_special_up()
    if rEGIM == "move":
        for a in b:
            move(a)


def modes():
    global mode

    if mode == "e_see":
        mode = "e_hide"
    elif mode == "e_hide":
        mode = "e_see"


def move(ball):
    ball["x"] = ball["x"] + ball["speed_x"]
    ball["y"] = ball["y"] + ball["speed_y"]
    if ball["x"] >= screen_width - ball["size"]:
        ball["x"] = screen_width - ball["size"]
        ball["speed_x"] = -ball["speed_x"]
    if ball["x"] <= ball["size"]:
        ball["x"] = ball["size"]
        ball["speed_x"] = -ball["speed_x"]
    if ball["y"] >= screen_height - ball["size"]:
        ball["y"] = screen_height - ball["size"]
        ball["speed_y"] = -ball["speed_y"]
    if ball["y"] <= ball["size"]:
        ball["y"] = ball["size"]
        ball["speed_y"] = -ball["speed_y"]


def new_ball():
    for i in range(ball_in_second):
        size = random.randint(1, 5)
        ball = {
            "size": size,
            "x": random.randint(size, screen_width - size),
            "y": random.randint(size, screen_height - size),
            "speed_x": random.choice([-2, 2]),
            "speed_y": random.choice([-2, 2]),
            "special_speed_y": 0,
            "rgb": [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]

        }

        b.append(ball)


def delete_all_balls():
    b.clear()

def balls_special():
    global rEGIM
    rEGIM="special"
def balls_special_up():
    global rEGIM
    if rEGIM == "special":
        b["special_speed_y"] = -b["y"] / 480
        for ball in b:

            ball["y"] = ball["y"] + ball["special_speed_y"]


def balls_fly():
    global rEGIM, rEGIM_fly
    rEGIM = "fly"
    rEGIM_fly = "fly_up"


def balls_fly_up():
    global rEGIM_fly
    if rEGIM == "fly":
        rEGIM_fly = "fly_up"


def balls_fly_down():
    global rEGIM_fly
    if rEGIM == "fly":
        rEGIM_fly = "fly_down"


def balls_fly_left():
    global rEGIM_fly
    if rEGIM == "fly":
        rEGIM_fly = "fly_left"


def balls_fly_right():
    global rEGIM_fly
    if rEGIM == "fly":
        rEGIM_fly = "fly_right"


def balls_can_fly():
    for ball in b:
        if rEGIM_fly == "fly_up":
            ball["y"] = ball["y"] - 1
        if rEGIM_fly == "fly_down":
            ball["y"] = ball["y"] + 1
        if rEGIM_fly == "fly_left":
            ball["x"] = ball["x"] - 1
        if rEGIM_fly == "fly_right":
            ball["x"] = ball["x"] + 1

        if ball["x"] >= screen_width - ball["size"]:
            ball["x"] = screen_width - ball["size"]
        if ball["x"] <= ball["size"]:
            ball["x"] = ball["size"]
        if ball["y"] >= screen_height - ball["size"]:
            ball["y"] = screen_height - ball["size"]
        if ball["y"] <= ball["size"]:
            ball["y"] = ball["size"]
