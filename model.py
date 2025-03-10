import random

class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 0.5
        self.lift = -10

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def jump(self):
        self.velocity = self.lift

class Meteorite:
    def __init__(self, x, y, speed=5):
        self.x = x
        self.y = y
        self.speed = speed

    def move(self):
        self.x -= self.speed

class GameModel:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.spaceship = Spaceship(100, height // 2)
        self.meteorites = []
        self.score = 0
        self.spawn_timer = 0
        self.started = False

    def reset_game(self):
        self.spaceship = Spaceship(100, self.height // 2)
        self.meteorites.clear()
        self.spawn_timer = 0
        self.score = 0

    def spawn_meteorite(self):
        y_pos = random.randint(0, self.height - 50)
        speed = 7 + int(self.score / 10) 
        self.meteorites.append(Meteorite(self.width, y_pos, speed))


    def update(self, moving=True):
        if moving:  
            self.spaceship.update()

            self.spawn_timer += 1
            if self.spawn_timer > 60:
                self.spawn_meteorite()
                self.spawn_timer = 0

            for meteorite in self.meteorites:
                meteorite.move()

            self.meteorites = [m for m in self.meteorites if m.x > -50]
            self.score += 0.01



    def check_collision(self):
        for meteorite in self.meteorites:
            if (self.spaceship.x < meteorite.x + 40 and
                self.spaceship.x + 40 > meteorite.x and
                self.spaceship.y < meteorite.y + 40 and
                self.spaceship.y + 40 > meteorite.y):
                return True
        if self.spaceship.y > self.height or self.spaceship.y < 0:
            return True
        return False
