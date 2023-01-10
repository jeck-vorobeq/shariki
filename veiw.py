import pygame, modul

pygame.init()
screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("medition")
answered = pygame.font.SysFont("Arial", 25, True)
r = 200
g = 200
b = 200


def weiv():
    global r, g, b
    screen.fill([0, 3, 0])

    for a in modul.b:
        pygame.draw.circle(screen, a["rgb"], [a["x"], a["y"]], a["size"])
    if modul.mode == "e_see":
        text = answered.render("Эту надпись можно закрыть нажав E", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 0])
        text = answered.render("G-полноэкранный режим", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 25])
        text = answered.render("На экране " + str(len(modul.b)) + " шариков", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 50])
        text = answered.render(str(modul.ball_in_second) + " Шариков в секунду", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 75])
        text = answered.render("Удалить шарики на клавишу DELETE", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 100])
        text = answered.render("Остановка шариков- клавиша 1", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 125])
        text = answered.render("полёт шариков- клавиша 2", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 150])
        text = answered.render("полёт шаров к границам - кл 3 + wasd", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 175])
        text = answered.render("фокусы-покусы- кл 4", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 200])

    pygame.display.flip()
