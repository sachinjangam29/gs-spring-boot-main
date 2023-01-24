import pygame

pygame.init()

window_size = (800,600)

screen = pygame.display.set_caption("Simple Game")

rect_x = 0
rect_y = 0

rect_speed = 5

rect_color = (255, 0, 0)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(0, 0, 0)

    rect_x+=rect_speed

    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, 50, 50))

    pygame.display.update()

    pygame.quit()