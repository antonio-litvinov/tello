from djitellopy import Tello
import pygame
import cv2
import time

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

    if getKey("p"):
        cv2.imwrite(f'{time.time()}.jpg', img)

    return [lr, fb, ud, yv]


me = Tello()
me.connect()
me.streamon()
global img

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
