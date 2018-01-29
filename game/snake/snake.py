"""Represents a snake"""

class Snake(object):
    """Represents a snake"""

    _BLACKBOARD = {
        'name': '',
        'id': -1,
        'health': -1,
        'body': [],
        'length': -1,
        'taunt': '',
    }

    def __init__(self, data):
        self._BLACKBOARD['name'] = data['name']
        self._BLACKBOARD['id'] = data['id']
        self._BLACKBOARD['health'] = data['health']
        self._BLACKBOARD['body'] = data['body']
        self._BLACKBOARD['length'] = data['length']
        self._BLACKBOARD['taunt'] = data['taunt']

    @property
    def name(self):
        """Returns the snake's name"""
        return self._BLACKBOARD['name']

    @property
    def id(self):
        """Returns the snake's id"""
        return self._BLACKBOARD['id']

    @property
    def health(self):
        """Returns the snake's health"""
        return self._BLACKBOARD['health']

    @property
    def head(self):
        """Returns the snake's head"""
        return self._BLACKBOARD['body'][0]

    @property
    def body(self):
        """Returns the body of the snake (incl. head and tail)"""
        return self._BLACKBOARD['body']

    @property
    def tail(self):
        """Returns the snake's tail"""
        return self._BLACKBOARD['body'][-1]

    @property
    def length(self):
        """Returns the snake's length"""
        return self._BLACKBOARD['length']

    @property
    def taunt(self):
        """Returns the snake's taunt"""
        return self._BLACKBOARD['taunt']

    def move(self):
        """Returns the snake's calculated next move"""
        return 'up'
