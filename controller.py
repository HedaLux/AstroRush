import pygame, sys
from menu import MainMenu

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.clock = pygame.time.Clock()
        self.state = 'MENU'
        self.menu = MainMenu(view.screen, model.width, model.height)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.state == 'MENU':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    result = self.menu.check_click(event.pos)
                    if result == "PLAY":
                        self.model.reset_game()
                        self.state = 'WAITING'
                    elif result == "ABOUT":
                        self.state = 'ABOUT'

            elif self.state == 'ABOUT':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    result = self.menu.check_click(event.pos)
                    if result == "BACK":
                        self.state = 'MENU'

            elif self.state == 'WAITING':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.model.started = True
                    self.state = 'PLAYING'

            elif self.state == 'PLAYING':
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.model.spaceship.jump()

    def run(self):
        while True:
            self.handle_events()

            if self.state == 'MENU':
                self.menu.draw_main()

            elif self.state == 'ABOUT':
                self.menu.draw_about()

            elif self.state == 'WAITING':
                self.view.draw(waiting=True)

            elif self.state == 'PLAYING':
                self.model.update()
                if self.model.check_collision():
                    self.view.draw_game_over()
                    pygame.time.wait(2000)
                    self.model.reset_game()
                    self.state = 'MENU'
                else:
                    self.view.draw()

            self.clock.tick(60)
