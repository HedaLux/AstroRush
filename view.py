import pygame

import pygame

class GameView:
    def __init__(self, model):
        pygame.init()
        self.model = model
        self.screen = pygame.display.set_mode((model.width, model.height))
        pygame.display.set_caption('AstroRush')
        self.font = pygame.font.SysFont(None, 36)

        self.spaceship_img = pygame.image.load('assets/spaceship.png').convert_alpha()
        self.spaceship_img = pygame.transform.scale(self.spaceship_img, (50, 40))

        self.meteor_img = pygame.image.load('assets/meteorite.png').convert_alpha()
        self.meteorite_img = pygame.transform.scale(self.meteor_img, (40, 40))

    def draw(self, waiting=False):
        self.screen.fill((20, 20, 30))

        spaceship_rect = self.spaceship_img.get_rect(center=(self.model.spaceship.x, self.model.spaceship.y))
        self.screen.blit(self.spaceship_img, spaceship_rect)

        for meteorite in self.model.meteorites:
            meteor_rect = self.meteorite_img.get_rect(center=(meteorite.x, meteorite.y))
            self.screen.blit(self.meteorite_img, meteor_rect)

        score_text = self.font.render(f"Score : {int(self.model.score)}", True, (255,255,255))
        self.screen.blit(score_text, (10,10))

        if not self.model.started:
            overlay_text = self.font.render("Appuie sur ESPACE pour commencer", True, (255, 255, 255))
            overlay_rect = overlay_text.get_rect(center=(self.model.width // 2, self.model.height // 2))
            self.screen.blit(overlay_text, overlay_rect)

        pygame.display.update()

    
    def draw_game_over(self):
        self.screen.fill((0,0,0))
        game_over_text = self.font.render(f"Game Over! Score : {int(self.model.score)}", True, (255,0,0))
        rect1 = game_over_text.get_rect(center=(self.model.width//2, self.model.height//2 - 30))
        self.screen.blit(game_over_text, rect1)
        pygame.display.update()
