import pygame.event, modul

pygame.init()
timer = pygame.event.custom_type()
pygame.time.set_timer(timer,1000)
pygame.key.set_repeat(90)

def ypravlrnie():
    global ball_in_second
    events = pygame.event.get()
    for wq in events:

        if wq.type == pygame.QUIT:
            exit()
        if wq.type == timer:
            modul.new_ball()
        if wq.type == pygame.KEYDOWN:
            if wq.key == pygame.K_ESCAPE:
                exit()
            if wq.key == pygame.K_e:
                modul.modes()
            if wq.key == pygame.K_UP:
                modul.plus_ball()
            if wq.key == pygame.K_DOWN:
                modul.minus_ball()
            if wq.key == pygame.K_g:
                modul.toggle_fullscreen()
            if wq.key == pygame.K_DELETE:
                modul.delete_all_balls()
            if wq.key == pygame.K_1:
                modul.balls_stop()
            if wq.key == pygame.K_2:
                modul.balls_move()