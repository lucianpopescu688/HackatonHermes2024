import pygame

def createBaseWindow(screen):
    ieText = pygame.font.Font("resources/micross.ttf", 25)
    ib = ieText.render("Irgum Burgum", None, "#afef31")
    xpbackground = pygame.image.load("resources/windowsXP.png")
    xpbcgndRect = xpbackground.get_rect(topleft = (0,0))
    xpFolder = pygame.image.load("resources/xpFolder.png")
    xpFolderRect = xpFolder.get_rect(topleft=((-15, 5)))
    ieLogo = pygame.image.load("resources/ieLogoforBackGround.png")
    virusLogo=pygame.image.load("resources/skull (1).png")
    virusLogoRect=xpFolder.get_rect(topleft=((5, 200)))

    ieLogoRect = ieLogo.get_rect(topleft = (-15, 100))

    screen.blit(xpbackground, xpbcgndRect)
    screen.blit(xpFolder, xpFolderRect)
    screen.blit(ieLogo, ieLogoRect)
    screen.blit(virusLogo, virusLogoRect)
    screen.blit(ib, (250, 550))
    rects = list()

    rects.append((xpFolder, xpFolderRect))
    rects.append((ieLogo, ieLogoRect))
    rects.append((virusLogo, virusLogoRect))

    killrect = pygame.rect.Rect(0, 870, 190, 30)

    rects.append((None, killrect))

    return screen, rects

def baseWindowButtons(screen, rects, controller):
    # killsurf = pygame.draw.rect(screen, "red", pygame.Rect(1510, 3, 90, 25))
    state = "base"

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
                if i == 0:
                    state = "statistics"
                if i == 1:
                    #screen, rects = createBrowserWindow(screen)
                    state = "browser"
                if i == len(rects)-1:
                    pygame.quit()
                    exit()
                if i==2:
                    state ="virus"

    return state, controller