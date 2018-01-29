"""Represents the snake AI with personality D.Va"""

from game.dva.dva import DVA

class Game(object):
    """Represents the Battlesnake D.Va"""
    data = None
    dva = None
    snakes = list()

    def __init__(self, data):
        self.data = data
        self.dva = DVA(data)

    def update(self, data):
        self.data = data
        self.dva.update(data)

class GameManager(object):

    MAX_GAMES = 10

    games = list()

    def create_or_get_game(self, data):
        game_id = data['id']

        for game in self.games:
            if game.data['id'] == game_id:
                return game

        if len(self.games) >= self.MAX_GAMES:
            self.games.pop(0)

        self.games.append(Game(data))

        return self.games[-1]
