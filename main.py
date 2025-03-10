from model import GameModel
from view import GameView
from controller import GameController

def main():
    model = GameModel(800, 600)
    view = GameView(model)
    controller = GameController(model, view)
    controller.run()

if __name__ == "__main__":
    main()
