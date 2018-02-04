"""Game module, includes Game class and factory for creating Game objects"""

from game.dva.dva import DVA

class Game(object):
    """Represents a Battlesnake game"""
    data = None
    dva = None
    snakes = list()

    def __init__(self, data):
        self.data = data
        self.dva = DVA(data)

    def update(self, data):
        self.data = data
        self.dva.update(data)

GAMES = list()
MAX_GAMES = 10

def factory(data):
    """Factory function for creating games"""
    game_id = data['id']

    for game in GAMES:
        if game.data['id'] == game_id:
            return game

    if len(GAMES) >= MAX_GAMES:
        GAMES.pop(0)

    GAMES.append(Game(data))

    return GAMES[-1]
