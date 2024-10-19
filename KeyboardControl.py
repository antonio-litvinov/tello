from djitellopy import Tello
import pygame

pygame.init()
win = pygame.display.set_mode((400, 400))


def getKey(key_name):
    ans = False
    for eve in pygame.event.get():
        pass
    key_input = pygame.key.get_pressed()
    key_pressed = getattr(pygame, "K_{}".format(key_name))
    if key_input[key_pressed]:
        ans = True
    pygame.display.update()
    return ans


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if getKey("LEFT"):
        lr = -speed
    elif getKey("RIGHT"):
        lr = speed

    if getKey("UP"):
        fb = speed
    elif getKey("DOWN"):
        fb = -speed

    if getKey("w"):
        ud = speed
    elif getKey("s"):
        ud = -speed

    if getKey("a"):
        yv = speed
    elif getKey("d"):
        yv = -speed

    if getKey("q"):
        me.land()
    if getKey("t"):
        me.takeoff()

    return [lr, fb, ud, yv]


me = Tello()
me.connect()

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
