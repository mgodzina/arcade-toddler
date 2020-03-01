import pygame
import random

# Game object containing parameters like position, speed etc
class GameObject():
    def __init__(self):
        self.reset()
    # reset function also used during init
    def reset(self):
        self.speed = 15
        self.dirH = 0
        self.dirV = 0
        self.posX = 0
        self.posY = 0
        self.sizeX = 100
        self.sizeY = 100

    # move object depending of direction value, including screen limit
    def move(self):
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()

        self.posX = self.posX + (self.dirH * self.speed)

        if self.posX < 0:
            self.posX = 0
        if self.posX > screen_width-self.sizeX:
            self.posX = screen_width-self.sizeX

        self.posY = self.posY + (self.dirV * self.speed)
        if self.posY < 0:
            self.posY = 0
        if self.posY > screen_height-self.sizeY:
            self.posY = screen_height-self.sizeY



pygame.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

# define joy controls
joyID = 0
axisH = 0
axisV = 1
colorBtn = 0
selectBtn = 7
startBtn = 6
speedUpBtn = 5
speedDwnBtn = 2

# define init params
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Arcade")
hero = GameObject()
color = (255, 0, 0)


done = False
while not done:
    # events management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.JOYBUTTONDOWN:
            if pygame.joystick.Joystick(joyID).get_button(speedUpBtn):
                if hero.speed < 30: hero.speed += 5
            if pygame.joystick.Joystick(joyID).get_button(speedDwnBtn):
                if hero.speed > 5: hero.speed -= 5

    # actions depending on values
    if pygame.joystick.Joystick(joyID).get_axis(axisH) > 0.3:
        hero.dirH = 1
    elif pygame.joystick.Joystick(joyID).get_axis(axisH) < -0.3:
        hero.dirH = -1
    else:
        hero.dirH = 0
    if pygame.joystick.Joystick(joyID).get_axis(axisV) > 0.3:
        hero.dirV = 1
    elif pygame.joystick.Joystick(joyID).get_axis(axisV) < -0.3:
        hero.dirV = -1
    else:
        hero.dirV = 0

    if pygame.joystick.Joystick(joyID).get_button(colorBtn):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    if pygame.joystick.Joystick(joyID).get_button(selectBtn) and pygame.joystick.Joystick(joyID).get_button(startBtn):
        done = True

    # main loop game functions
    hero.move()


    # screen drawing
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, color, (hero.posX, hero.posY, hero.sizeX, hero.sizeY))


    pygame.display.flip()
    clock.tick(20)


pygame.quit()
