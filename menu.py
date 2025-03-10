import pygame

class MainMenu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.SysFont(None, 48)

        self.play_button = pygame.Rect(width // 2 - 100, height // 2 - 40, 200, 50)
        self.about_button = pygame.Rect(width // 2 - 100, height // 2 + 30, 200, 50)
        self.back_button = pygame.Rect(width // 2 - 100, height - 100, 200, 50)

    def draw_main(self):
        self.screen.fill((10, 10, 30))

        title_surface = self.font.render("AstroRush", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(self.width // 2, self.height // 4))
        self.screen.blit(title_surface, title_rect)

        pygame.draw.rect(self.screen, (0, 180, 0), self.play_button)
        play_text = self.font.render("PLAY", True, (255, 255, 255))
        play_rect = play_text.get_rect(center=self.play_button.center)
        self.screen.blit(play_text, play_rect)

        pygame.draw.rect(self.screen, (0, 100, 200), self.about_button)
        about_text = self.font.render("ABOUT", True, (255, 255, 255))
        about_rect = about_text.get_rect(center=self.about_button.center)
        self.screen.blit(about_text, about_rect)

        pygame.display.update()

    def draw_about(self):
        self.screen.fill((10, 10, 30))

        about_lines = [
            "Welcome to AstroRush!",
            "",
            "Press SPACE to control the spaceship.",
            "Avoid meteorites and earn points!",
            "",
            "The speed of meteorites",
            "increases gradually as your",
            "score gets higher!",
            "",
            "Good luck!"
        ]

        for idx, line in enumerate(about_lines):
            text = self.font.render(line, True, (255, 255, 255))
            rect = text.get_rect(center=(self.width // 2, 80 + idx * 40))
            self.screen.blit(text, rect)

        
        pygame.draw.rect(self.screen, (180, 50, 50), self.back_button)
        back_text = self.font.render("BACK", True, (255, 255, 255))
        back_rect = back_text.get_rect(center=self.back_button.center)
        self.screen.blit(back_text, back_rect)

        pygame.display.update()

    def check_click(self, pos):
        if self.play_button.collidepoint(pos):
            return "PLAY"
        elif self.about_button.collidepoint(pos):
            return "ABOUT"
        elif self.back_button.collidepoint(pos):
            return "BACK"
        return None
