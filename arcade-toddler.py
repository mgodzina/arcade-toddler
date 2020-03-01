# Ver 1.0.1
import pygame
import random


# Game object containing parameters like position, speed etc
class GameObject:
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
        self.color = (255, 0, 0)

    # move object depending of direction value, including screen limit
    def move(self):
        screen_width = pygame.display.get_surface().get_width()
        screen_height = pygame.display.get_surface().get_height()

        self.posX = self.posX + (self.dirH * self.speed)

        if self.posX < 0:
            self.posX = 0
        if self.posX > screen_width - self.sizeX:
            self.posX = screen_width - self.sizeX

        self.posY = self.posY + (self.dirV * self.speed)
        if self.posY < 0:
            self.posY = 0
        if self.posY > screen_height - self.sizeY:
            self.posY = screen_height - self.sizeY


class Controls():
    def __init__(self, joyid, axish, axisv, colorbtn, speedupbtn, speeddwnbtn, selectbtn, startbtn):
        self.joyID = joyid
        self.axisH = axish
        self.axisV = axisv
        self.colorBtn = colorbtn
        self.speedUpBtn = speedupbtn
        self.speedDwnBtn = speeddwnbtn
        self.selectBtn = selectbtn
        self.startBtn = startbtn

    def dirH(self):
        if pygame.joystick.Joystick(self.joyID).get_axis(self.axisH) > 0.3:
            return 1
        elif pygame.joystick.Joystick(self.joyID).get_axis(self.axisH) < -0.3:
            return -1
        else:
            return 0

    def dirV(self):
        if pygame.joystick.Joystick(self.joyID).get_axis(self.axisV) > 0.3:
            return 1
        elif pygame.joystick.Joystick(self.joyID).get_axis(self.axisV) < -0.3:
            return -1
        else:
            return 0

    def color(self, object):
        if pygame.joystick.Joystick(self.joyID).get_button(self.colorBtn):
            object.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            return True
        return False

    def changeSpeed(self, object):
        if pygame.joystick.Joystick(self.joyID).get_button(self.speedUpBtn):
            if object.speed < 30: object.speed += 5
        if pygame.joystick.Joystick(self.joyID).get_button(self.speedDwnBtn):
            if object.speed > 5: object.speed -= 5

    def joyquit(self):
        if pygame.joystick.Joystick(self.joyID).get_button(self.selectBtn) and pygame.joystick.Joystick(self.joyID).get_button(self.startBtn):
            return True
        return False


pygame.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
pygame.joystick.init()
pygame.joystick.Joystick(0).init()

# define joy controls
joy = Controls(0, 0, 1, 0, 5, 2, 7, 6)

# define init params
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Arcade")
hero = GameObject()

done = False
while not done:
    # events management
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.JOYBUTTONDOWN:
            joy.changeSpeed(hero)

    # actions depending on values
    hero.dirH = joy.dirH()
    hero.dirV = joy.dirV()

    joy.color(hero)

    if joy.joyquit(): done = True

    # main loop game functions
    hero.move()

    # screen drawing
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, hero.color, (hero.posX, hero.posY, hero.sizeX, hero.sizeY))

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
