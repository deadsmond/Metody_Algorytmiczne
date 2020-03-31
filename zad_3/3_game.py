# game object


class GameEngine:
    def __init__(self):
        pass

    def analyse_state(self):
        """ analyse state passed from GameController """
        pass

    def random(self, ) -> str:
        """ make random decision based on analysed game state """
        pass

    def decision_tree(self):
        """ make decision based on analysed game state and decision tree """
        pass


class GameInterface:
    def __init__(self):
        pass

    def analyse_state(self):
        """ analyse state passed from GameController"""
        pass

    def text(self):
        """ return text based interface """

    def graphic_window(self):
        """ return graphic window based interface """


class GameController:
    def __init__(self):
        # variables
        self.engine = GameEngine()
        self.interface = GameInterface()


if __name__ == "__main__":
    # init games
    game = GameController()
