import pygame.event, modul


def ypravlrnie():
    events = pygame.event.get()
    for wq in events:

        if wq.type == pygame.QUIT:
            exit()
        if wq.type == pygame.MOUSEMOTION:
            modul.new_ball()
        if wq.type == pygame.KEYDOWN:
            if wq.key == pygame.K_ESCAPE:
                exit()
            if wq.key == pygame.K_e:
                modul.modes()
