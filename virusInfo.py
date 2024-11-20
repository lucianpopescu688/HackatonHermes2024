import pygame
from Controller.Controller import Controller

def createVirusInfo(screen):
    viruswindow = pygame.image.load("resources/radiobuttons.png")
    virusRect = viruswindow.get_rect(topleft = (600, 200))
    ieText = pygame.font.Font("resources/micross.ttf", 25)
    hackText = ieText.render("Advanced Hacking Tool", None, "white")
    hackRect = hackText.get_rect(topleft = virusRect.topleft)
    hackRect.top += 8
    hackRect.left += 8
    text = pygame.font.Font("resources/micross.ttf", 20)
    bruteForceText = text.render("Launch brute force attacks", None, "#2c2c24")
    phishingText = text.render("Release the phising emails", None, "#2c2c24")
    wormText = text.render("Unleash the worms", None, "#2c2c24")
    ransomwareText = text.render("Launch the ransomware hacks", None, "#2c2c24")
    bruteForceRect = bruteForceText.get_rect(midright = virusRect.center)
    bruteForceRect.left += 75
    bruteForceRect.top -= 43
    phishingRect = phishingText.get_rect(topleft = bruteForceRect.topleft)
    phishingRect.top += 36
    wormRect = wormText.get_rect(topleft = phishingRect.topleft)
    wormRect.top += 36
    ransomwareRect = ransomwareText.get_rect(topleft = wormRect.topleft)
    ransomwareRect.top += 36
    attackBtn1Text=text.render("Simple attack", None , "#2c2c24")
    attackBtn1Rect= attackBtn1Text.get_rect(midbottom =virusRect.midbottom)
    attackBtn1Rect.top-=30
    attackBtn1Rect.left+=40
    attackBtn2Text=text.render("Risky attack", None , "#2c2c24")
    attackBtn2Rect= attackBtn2Text.get_rect(midbottom =virusRect.midbottom)
    attackBtn2Rect.top-=30
    attackBtn2Rect.left+=200

    screen.blit(viruswindow, virusRect)
    screen.blit(hackText, hackRect)
    screen.blit(bruteForceText, bruteForceRect)
    screen.blit(phishingText, phishingRect)
    screen.blit(wormText, wormRect)
    screen.blit(ransomwareText, ransomwareRect)
    screen.blit(attackBtn1Text, attackBtn1Rect)
    screen.blit(attackBtn2Text, attackBtn2Rect)

    killRect1 = pygame.Rect(virusRect.right-40, virusRect.top+5, 30, 30)
    killRect2 = pygame.Rect(virusRect.left+110, virusRect.bottom-62, 150, 42)

    govRect = pygame.Rect(870, 495, 144, 42)
    compRect = pygame.Rect(1030, 495, 144, 42)

    rects = list()
    rects.append((None, killRect1))
    rects.append((None, killRect2))
    rects.append((bruteForceText, bruteForceRect))
    rects.append((phishingText, phishingRect))
    rects.append((wormText, wormRect))
    rects.append((ransomwareText, ransomwareRect))
    rects.append((None, govRect))
    rects.append((None, compRect))

    return screen, rects


def virusButtons(screen, rects, controller):
    #killsurf = pygame.draw.rect(screen, "red", pygame.Rect(1030, 495, 144, 42))

    state = "virus"

    if controller.getActiveBruteForce():
        dot = pygame.image.load("resources/dot.png")
        dotRect = dot.get_rect(topleft=(750, 331))
        dotRect.left -= 30
        screen.blit(dot, dotRect)
    else:
        notdot = pygame.image.load("resources/notDot.jpeg")
        notdotRect = notdot.get_rect(topleft=(750, 331))
        notdotRect.left -= 30
        screen.blit(notdot, notdotRect)
    if not controller.getActivePhishing():
        dot = pygame.image.load("resources/notDot.jpeg")
        dotRect = dot.get_rect(topleft=(750, 367))
        dotRect.left -= 30
        screen.blit(dot, dotRect)
    else:
        dot = pygame.image.load("resources/dot.png")
        dotRect = dot.get_rect(topleft=(750, 367))
        dotRect.left -= 30
        screen.blit(dot, dotRect)
    if not controller.getActiveWorm():
        dot = pygame.image.load("resources/notDot.jpeg")
        dotRect = dot.get_rect(topleft=(750, 403))
        dotRect.left -= 30
        screen.blit(dot, dotRect)

    else:
        dot = pygame.image.load("resources/dot.png")
        dotRect = dot.get_rect(topleft=(750, 403))
        dotRect.left -= 30
        screen.blit(dot, dotRect)
    if not controller.ransom_automation_enabled:
        dot = pygame.image.load("resources/notDot.jpeg")
        dotRect = dot.get_rect(topleft=(750, 439))
        dotRect.left -= 30
        screen.blit(dot, dotRect)
    else:
        dot = pygame.image.load("resources/dot.png")
        dotRect = dot.get_rect(topleft=(750, 439))
        dotRect.left -= 30
        screen.blit(dot, dotRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

        for i in range(len(rects)):
            if event.type == pygame.MOUSEBUTTONDOWN and rects[i][1].collidepoint(event.pos):
                if i == 0 or i == 1:
                    state = "base"
                if i == 2:

                    controller.toggle_brute_force_automation()
                if i == 3:

                    controller.toggle_phishing_automation()
                if i == 4:

                    controller.toggle_worm_automation()
                if i == 5:

                    controller.toggle_ransom_automation()

                if i == 6:
                    controller.start_government_hack()
                    pass

                if i == 7:
                    controller.start_company_hack()
                    new_company_name = controller.start_company_hack()


    return state, controller