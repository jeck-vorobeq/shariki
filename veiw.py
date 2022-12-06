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
        screen.blit(text, [12, 12])
        text = answered.render("G-полноэкранный режим", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 37])
        text = answered.render("На экране " + str(len(modul.b)) + " шариков", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 64])
        text = answered.render(str(modul.ball_in_second) + " шариков в секунду", True, [r, g, b], [0, 0, 0])
        screen.blit(text, [12, 91])
    pygame.display.flip()
