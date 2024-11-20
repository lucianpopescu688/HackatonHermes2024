import pygame
from Controller.Controller import Controller

def createBrowserWindow(screen):
    # bcgrnd = pygame.Surface((1561, 775))
    # bcgrnd.fill("#c4f0c0")

    bcgrnd = pygame.image.load("resources/hackerbackground.png")
    bcgrndRect = bcgrnd.get_rect(topleft = (3, 86))

    windowsButtons = pygame.image.load("resources/windowsheaderstuff.png")
    buttonsRect = windowsButtons.get_rect(topleft = (1510, 3))
    ieLogo = pygame.image.load("resources/ieLogo.png")
    ieBase = pygame.image.load("resources/ieBase.png")
    header = pygame.Surface((1600, 30))
    header.fill("#010180")
    ieText = pygame.font.Font("resources/micross.ttf", 25)
    ieTextSurface = ieText.render("Windows Internet Explorer", None, "White")
    # UserName = pygame.font.Font("resources/micross.ttf", 20)
    # UserNameText = UserName.render("Hacker name", None, "#36454F")

    screen.blit(header, (0,0))
    screen.blit(windowsButtons, buttonsRect)
    screen.blit(ieTextSurface, (30, 0))

    screen.blit(ieLogo, (-2, 0))
    screen.blit(ieBase, (0, 30))
    screen.blit(bcgrnd, bcgrndRect)
    # screen.blit(UserNameText, (10, 95))


    ieBaseText = pygame.font.Font("resources/micross.ttf", 50)

    balanceText = ieBaseText.render("Your wallet: 0.00$", None, "#CFCFC4")
    bruteForceText=ieBaseText.render("Brute Force attack", None, "#CFCFC4")
    wormText=ieBaseText.render("Worm Virus", None, "#CFCFC4")
    ransomText=ieBaseText.render("Ransom Virus", None, "#CFCFC4")
    phishinText=ieBaseText.render("Phishing Scams", None, "#CFCFC4")
    companyText=ieBaseText.render("Corporate love - hack", None, "#CFCFC4")
    govText=ieBaseText.render("Government kisses - hack", None, "#CFCFC4")

    rectBalance=balanceText.get_rect(topleft=(600, 150))
    rectBrute = bruteForceText.get_rect(topleft=(100, 250))
    rectWorm = wormText.get_rect(topleft=(100, 350))
    rectRansom = ransomText.get_rect(topleft=(100, 450))
    rectPhis = phishinText.get_rect(topleft=(100, 550))
    rectComp = companyText.get_rect(topleft=(100, 650))
    rectGov = govText.get_rect(topleft=(100, 750))


    screen.blit(balanceText, rectBalance)
    screen.blit(bruteForceText, rectBrute)
    screen.blit(wormText, rectWorm)
    screen.blit(ransomText, rectRansom)
    screen.blit(phishinText, rectPhis)
    screen.blit(companyText, rectComp)
    screen.blit(govText, rectGov)

    brutePriceText = ieBaseText.render("Price", None, "#CFCFC4")
    wormPriceText = ieBaseText.render("Price", None, "#CFCFC4")
    ransomPriceText = ieBaseText.render("Price", None, "#CFCFC4")
    phishinPriceText = ieBaseText.render("Price", None, "#CFCFC4")
    companyPriceText = ieBaseText.render("Price", None, "#CFCFC4")
    govPriceText = ieBaseText.render("Price", None, "#CFCFC4")

    brutePrice = brutePriceText.get_rect(topleft=(800, 250))
    wormPrice = wormPriceText.get_rect(topleft=(800, 350))
    ransomPrice = ransomPriceText.get_rect(topleft=(800, 450))
    phisPrice = phishinPriceText.get_rect(topleft=(800, 550))
    compPrice = companyPriceText.get_rect(topleft=(800, 650))
    govPrice = govPriceText.get_rect(topleft=(800, 750))

    screen.blit(brutePriceText, brutePrice)
    screen.blit(wormPriceText, wormPrice)
    screen.blit(ransomPriceText, ransomPrice)
    screen.blit(phishinPriceText, phisPrice)
    screen.blit(companyPriceText, compPrice)
    screen.blit(govPriceText, govPrice)

    # buyBtn1 = pygame.image.load("resources/buyButton.png")
    # buyBtn2 = pygame.image.load("resources/buyButton.png")
    # buyBtn3 = pygame.image.load("resources/buyButton.png")
    # buyBtn4 = pygame.image.load("resources/buyButton.png")
    # buyBtn5 = pygame.image.load("resources/buyButton.png")
    # buyBtn6 = pygame.image.load("resources/buyButton.png")
    #
    # rectBtn1=(buyBtn1.get_rect(topleft=(1100, 250)))
    # rectBtn2=(buyBtn2.get_rect(topleft=(1100, 350)))
    # rectBtn3=(buyBtn3.get_rect(topleft=(1100, 450)))
    # rectBtn4=(buyBtn4.get_rect(topleft=(1100, 550)))
    # rectBtn5=(buyBtn5.get_rect(topleft=(1100, 650)))
    # rectBtn6=(buyBtn6.get_rect(topleft=(1100, 750)))
    #
    # screen.blit(buyBtn1, rectBtn1)
    # screen.blit(buyBtn2, rectBtn2)
    # screen.blit(buyBtn3, rectBtn3)
    # screen.blit(buyBtn4, rectBtn4)
    # screen.blit(buyBtn5, rectBtn5)
    # screen.blit(buyBtn6, rectBtn6)

    upBypassing = pygame.image.load("resources/bypassingUpgradeButton.png")
    upComponents = pygame.image.load("resources/componentsUpgradeButton.png")
    upCredibility = pygame.image.load("resources/credibilityUpgradeButton.png")
    upDataFlow = pygame.image.load("resources/dataflowUpgradeButton.png")
    upEncryption = pygame.image.load("resources/encryptionUpgradeButton.png")
    upMaxMails = pygame.image.load("resources/maxemailUpgradeButton.png")
    upSpeed = pygame.image.load("resources/speedUpgradeButton.png")
    upSpread = pygame.image.load("resources/spreadrateUpgradeButton.png")
    upStealth = pygame.image.load("resources/stealthUpgradeButton.png")
    skillUp = pygame.image.load("resources/skillUpgradeButton.png")
    rectUpBypassing=(upBypassing.get_rect(topleft=(1000, 750)))
    rectComponents=(upComponents.get_rect(topleft=(1000, 250)))
    rectCredibiliy=(upCredibility.get_rect(topleft=(1000, 550)))
    rectDataFlowG=(upDataFlow.get_rect(topleft=(1200, 750)))
    rectDataFlowC=(upDataFlow.get_rect(topleft=(1200, 650)))
    rectEncrypionC=(upEncryption.get_rect(topleft=(1000, 650)))
    rectEncrypionR=(upEncryption.get_rect(topleft=(1000, 450)))
    rectMaxMails=(upMaxMails.get_rect(topleft=(1200, 550)))
    rectSpeed=(upSpeed.get_rect(topleft=(1200, 250)))
    rectSpread=(upSpread.get_rect(topleft=(1000, 350)))

    skillRectR = skillUp.get_rect(topleft=(1200, 450))
    skillRectP = skillUp.get_rect(topleft=(1400, 650))
    rectStealthW = (upStealth.get_rect(topleft=(1200, 350)))
    rectStealthP = (upStealth.get_rect(topleft=(1400, 750)))

    screen.blit(upBypassing, rectUpBypassing)
    screen.blit(upComponents, rectComponents)
    screen.blit(upCredibility, rectCredibiliy)
    screen.blit(upDataFlow, rectDataFlowG)
    screen.blit(upDataFlow, rectDataFlowC)
    screen.blit(upEncryption, rectEncrypionC)
    screen.blit(upEncryption, rectEncrypionR)
    screen.blit(upMaxMails, rectMaxMails)
    screen.blit(upSpeed, rectSpeed)
    screen.blit(upSpread, rectSpread)
    screen.blit(upStealth, rectStealthW)
    screen.blit(upStealth, rectStealthP)
    screen.blit(skillUp, skillRectP)
    screen.blit(skillUp, skillRectR)

    rects = list()

    rects.append((windowsButtons, buttonsRect))#0

    rects.append((upBypassing, rectUpBypassing))#1
    rects.append((upComponents, rectComponents))#2
    rects.append((upCredibility, rectCredibiliy))#3
    rects.append((upDataFlow, rectDataFlowG))#4
    rects.append((upDataFlow, rectDataFlowC))#5
    rects.append((upEncryption, rectEncrypionC))#6
    rects.append((upEncryption, rectEncrypionR))#7
    rects.append((upMaxMails, rectMaxMails))#8
    rects.append((upSpeed, rectSpeed))#9
    rects.append((upSpread, rectSpread))#10
    rects.append((upStealth, rectStealthW))#11
    rects.append((upStealth, rectStealthP))#12
    rects.append((skillUp, skillRectP))#13
    rects.append((skillUp, skillRectR))#14

    ieBaseText = pygame.font.Font("resources/micross.ttf", 50)

    balanceText = ieBaseText.render("Your wallet: 0.00$", None, "#CFCFC4")
    bruteForceText = ieBaseText.render("Brute Force attack", None, "#CFCFC4")
    wormText = ieBaseText.render("Worm Virus", None, "#CFCFC4")
    ransomText = ieBaseText.render("Ransom Virus", None, "#CFCFC4")
    phishinText = ieBaseText.render("Phishing Scams", None, "#CFCFC4")
    companyText = ieBaseText.render("Corporate love - hack", None, "#CFCFC4")
    govText = ieBaseText.render("Government kisses - hack", None, "#CFCFC4")

    companyHackChanceText = ieBaseText.render("Company Hack Chance: 0%", None, "#CFCFC4")
    govHackChanceText = ieBaseText.render("Government Hack Chance: 0%", None, "#CFCFC4")

    rectBalance = balanceText.get_rect(topleft=(600, 150))
    rectBrute = bruteForceText.get_rect(topleft=(100, 250))
    rectWorm = wormText.get_rect(topleft=(100, 350))
    rectRansom = ransomText.get_rect(topleft=(100, 450))
    rectPhis = phishinText.get_rect(topleft=(100, 550))
    rectComp = companyText.get_rect(topleft=(100, 650))
    rectGov = govText.get_rect(topleft=(100, 750))

    screen_height = screen.get_height()
    rectCompanyHackChance = companyHackChanceText.get_rect(topleft=(100, screen_height - 150))
    rectGovHackChance = govHackChanceText.get_rect(topleft=(100, screen_height - 100))

    screen.blit(balanceText, rectBalance)
    screen.blit(bruteForceText, rectBrute)
    screen.blit(wormText, rectWorm)
    screen.blit(ransomText, rectRansom)
    screen.blit(phishinText, rectPhis)
    screen.blit(companyText, rectComp)
    screen.blit(govText, rectGov)

    return screen, rects

def browserWindowButtons(screen, brects, controller):
    state = "browser"

    ieBaseText = pygame.font.Font("resources/micross.ttf", 50)
    balanceText = ieBaseText.render(f"Your wallet: {controller.getMoney()}$", None, "#CFCFC4")
    rectBalance = balanceText.get_rect(topleft=(400, 150))
    header = pygame.Surface((800, 60))
    header.fill("black")
    screen.blit(header, (400, 150))
    screen.blit(balanceText, rectBalance)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        for i in range(len(brects)):
            if event.type == pygame.MOUSEBUTTONDOWN and brects[i][1].collidepoint(event.pos):
                if i == 0:
                    state = "base"
                if i == 1:
                    controller.get_hack_chance_government()
                if i == 2:
                    controller.upgradeBruteForceAttempts()
                if i == 3:
                    controller.upgradePhishingEfficiency()
                if i == 4:
                    controller.get_hack_chance_government()
                    controller.get_hack_chance_company()
                if i == 5:
                    controller.get_hack_chance_government()
                    controller.get_hack_chance_company()
                if i == 6:
                    controller.upgradeRansomwareEncryption()
                    controller.get_hack_chance_government()
                    controller.get_hack_chance_company()
                if i == 7:
                    controller.upgradeRansomwareEncryption()
                if i == 8:
                    controller.upgradePhishingStealth()
                if i == 9:
                    controller.upgradeBruteForceAttempts()
                if i == 10:
                    controller.upgradeWormSpeed()
                if i == 11:
                    controller.upgradeWormStealth()
                    controller.get_hack_chance_government()
                    controller.get_hack_chance_company()
                if i == 12:
                    controller.upgradePhishingStealth()
                    controller.get_hack_chance_government()
                    controller.get_hack_chance_company()
                if i == 13:
                    controller.get_hack_chance_government()
                    controller.get_hack_chance_company()
                if i == 14:
                    controller.get_hack_chance_government()
                    controller.get_hack_chance_company()


    return state, controller