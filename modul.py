import random

mode = "e_see"

b = []


def all_in_modul():
    for a in b:
        otbivka(a)


def modes():
    global mode

    if mode == "e_see":
        mode = "e_hide"
    elif mode == "e_hide":
        mode = "e_see"


def otbivka(ball):
    ball["x"] = ball["x"] + ball["speed_x"]
    ball["y"] = ball["y"] + ball["speed_y"]
    if ball["x"] >= 500 - ball["size"]:
        ball["speed_x"] = -ball["speed_x"]
    if ball["x"] <= ball["size"]:
        ball["speed_x"] = -ball["speed_x"]
    if ball["y"] >= 500 - ball["size"]:
        ball["speed_y"] = -ball["speed_y"]
    if ball["y"] <= ball["size"]:
        ball["speed_y"] = -ball["speed_y"]


def new_ball():
    ball = {
        "x": random.randint(14, 486),
        "y": random.randint(14, 486),
        "size": random.randint(5, 14),
        "speed_x": random.randint(-9, 9),
        "speed_y": random.randint(-9, 9),
        "rgb": [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]

    }
    b.append(ball)
