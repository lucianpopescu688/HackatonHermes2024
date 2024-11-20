import pygame

def createStatisticsWindow(screen, controller):
    notepad = pygame.image.load("resources/notepad95.png")
    notepadRect = notepad.get_rect(topleft=(400, 300))
    notepadBcgrnd = pygame.Surface(notepadRect.size)
    notepadBcgrnd.fill("white")

    ieBaseText = pygame.font.Font("resources/micross.ttf", 20)
    nameText = ieBaseText.render(f"Here is your username: {controller.getName()}", None, "#2c2c24")
    name = nameText.get_rect(topleft=(420, 370))
    victimsText = ieBaseText.render(f"Number of computers affected: {int(controller.getInfectedCount())}", None, "#2c2c24")
    victims=victimsText.get_rect(topleft=(420, 420))
    moneyText = ieBaseText.render(f"Your riches: {controller.getMoney()}$", None, "#2c2c24")
    money = moneyText.get_rect(topleft = (420, 470))

    screen.blit(notepadBcgrnd, notepadRect)
    screen.blit(notepad, notepadRect)
    screen.blit(nameText, name)
    screen.blit(victimsText, victims)
    screen.blit(moneyText, money)

    companyHackChance = controller.get_hack_chance_company()
    govHackChance = controller.get_hack_chance_government()

    companyHackChanceText = ieBaseText.render(f"Company Hack Chance: {companyHackChance}%", None, "#2c2c24")
    govHackChanceText = ieBaseText.render(f"Government Hack Chance: {govHackChance}%", None, "#2c2c24")

    rectCompanyHackChance = companyHackChanceText.get_rect(topleft=(420, 520))
    rectGovHackChance = govHackChanceText.get_rect(topleft=(420, 570))

    screen.blit(companyHackChanceText, rectCompanyHackChance)
    screen.blit(govHackChanceText, rectGovHackChance)


    killRect = pygame.Rect(932, 305, 60, 18)

    rects = list()
    rects.append((None, killRect))

    return screen, rects

def statisticsButtons(screen, rects, controller):
    #killsurf = pygame.draw.rect(screen, "red", pygame.Rect(932, 305, 60, 18))
    state = "statistics"

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
                    state = "base"

    return state, controller