from time import sleep

import pygame
from sys import exit
from baseWindow import *
from browserWindow import *
from statisticsWindow import *
from virusInfo import *
from Controller.Controller import Controller

pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Hackaton")

screen, rects = createBaseWindow(screen)

clock = pygame.time.Clock()

state = "base"
changed = False

controller = Controller("Pityuka")

i=0
controller.activateWorm()
controller.activateRansomware()
controller.activatePhishing()
controller.activateBruteForce()
controller.performWorm()
controller.performRansom()
controller.performPhish()
controller.performBruteForce()
while True:
    #killsurf = pygame.draw.rect(screen, "red", pygame.Rect(0, 870, 190, 30))

    if state == "base":
        if changed == True:
            screen, rects = createBaseWindow(screen)
            changed = False
        state, controller = baseWindowButtons(screen, rects, controller)
        if (state != "base"):
            changed = True
    if state == "browser":
        if changed == True:
            screen, rects= createBrowserWindow(screen)
            changed = False
        state, controller = browserWindowButtons(screen, rects, controller)
        if state != "browser":
            changed = True
    if state == "statistics":
        if changed == True:
            screen, rects = createStatisticsWindow(screen, controller)
            changed = False
        state, controller = statisticsButtons(screen, rects, controller)
        if state != "statistics":
            changed = True
    if state == "virus":
        if changed == True:
            screen, rects = createVirusInfo(screen)
            changed = False
        state, controller = virusButtons(screen, rects, controller)
        if state != "virus":
            changed=True

    if i%300 == 0:
        if controller.ransom_automation_enabled:
            controller.performRansom()
        if controller.phishing_automation_enabled:
            controller.performPhish()
        if controller.worm_automation_enabled:
            controller.performWorm()
        if controller.brute_force_automation_enabled:
            controller.performBruteForce()

    i += 1

    pygame.display.update()
    clock.tick(60)