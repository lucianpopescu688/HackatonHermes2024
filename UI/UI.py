import pygame
from model.exceptions.GameException import GameException

class HackControlInterface:
    def __init__(self, controller, buttons):
        self.controller = controller
        self.buttons = buttons
        self.running = True
        self.company_name = self.controller.attack_on_company.get_company_name().value

    def handle_events(self):
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if button["rect"].collidepoint(event.pos):
                            action = button["action"]
                            if button.get("type") == "switch":
                                if action == "toggle_worm" and self.controller.boughtWorm:
                                    self.controller.toggle_worm_automation()
                                elif action == "toggle_ransom" and self.controller.boughtRansom:
                                    self.controller.toggle_ransom_automation()
                                elif action == "toggle_phishing" and self.controller.boughtPhis:
                                    self.controller.toggle_phishing_automation()
                            else:
                                if action == "attack_on_company":
                                    self.controller.perform_attack_on_company()
                                elif action == "upgrade_worm_speed":
                                    self.controller.upgradeWormSpeed()
                                elif action == "upgrade_worm_stealth":
                                    self.controller.upgradeWormStealth()
                                elif action == "perform_worm":
                                    self.controller.performWorm()
                                elif action == "upgrade_ransomware_encryption":
                                    self.controller.upgradeRansomwareEncryption()
                                elif action == "upgrade_ransomware_ransom":
                                    self.controller.upgradeRansomwareRansom()
                                elif action == "perform_ransom":
                                    self.controller.performRansom()
                                elif action == "upgrade_phishing_efficiency":
                                    self.controller.upgradePhishingEfficiency()
                                elif action == "upgrade_phishing_stealth":
                                    self.controller.upgradePhishingStealth()
                                elif action == "perform_phish":
                                    self.controller.performPhish()
                                elif action == "start_worm":
                                    self.controller.activateWorm()
                                elif action == "start_ransom":
                                    self.controller.activateRansomware()
                                elif action == "start_phishing":
                                    self.controller.activatePhishing()
                                elif action == "start_company_hack":
                                    new_company_name = self.controller.start_company_hack()
                                    self.company_name = new_company_name
                                elif action == "start_government_hack":
                                    self.controller.start_government_hack()
        except GameException as e:
            print(f"Game exception occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def automate_actions(self):
        if self.controller.is_worm_automation_enabled():
            self.controller.performWorm()
        if self.controller.is_ransom_automation_enabled():
            self.controller.performRansom()
        if self.controller.is_phishing_automation_enabled():
            self.controller.performPhish()


    def draw(self, screen, font):
        screen.fill((100, 100, 100))
        for button in self.buttons:
            pygame.draw.rect(screen, (255, 0, 0), button["rect"])
            label = font.render(button["label"], True, (255, 255, 255))
            screen.blit(label, (button["rect"].x + 10, button["rect"].y + 10))

        # Display the company name
        company_label = font.render(f"Target Company: {self.company_name}", True, (255, 255, 255))
        screen.blit(company_label, (50, 500))

        # Display the number of companies hacked
        companies_hacked_label = font.render(f"Companies Hacked: {self.controller.companies_hacked}", True,(255, 255, 255))
        screen.blit(companies_hacked_label, (50, 550))

        # Display player information at the very bottom
        player_info = font.render(
            f"Player: {self.controller.p.name} | Money: {self.controller.p.money} | Affected Devices: {self.controller.p.computers_infected}",
            True, (255, 255, 255))
        screen.blit(player_info, (50, screen.get_height() - 50))

        # Display company hack chance
        hack_chance = font.render(f"Company Hack Chance: {self.controller.get_hack_chance_company()}%", True,
                                  (255, 255, 255))
        screen.blit(hack_chance, (50, screen.get_height() - 100))

        # Display government hack chance
        government_hack_chance = font.render(f"Government Hack Chance: {self.controller.get_hack_chance_government()}%",
                                             True, (255, 255, 255))
        screen.blit(government_hack_chance, (50, screen.get_height() - 150))

        pygame.display.flip()