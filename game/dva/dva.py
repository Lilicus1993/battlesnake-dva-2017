"""Represents the snake AI with personality D.Va"""

import sys
import random
import game.helpers.pathfinding as pathfinding
from game.helpers.graph import Graph

class DVA(object):
    """Represents the Battlesnake D.Va"""

    NAME = 'D.Va'
    IMAGE_URL = '../static/d_va.png'
    COLOR = '#EE4BB5'
    TAUNTS = {
        'set_up': {
            'dva_online': 'D.Va online.',
            'into_the_fight': 'I can\'t wait to get into the fight!',
            'new_high_score': 'Let\'s shoot for a new high score!',
            'gameface_on': 'Alright. Gameface: On.',
            'keep_up_with_me': 'Think you can keep up with me?',
            'lead_the_way': 'MEKA leads the way!',
            'ready_player_one': 'Ready, player 1.',
        }
    }

    # AI Blackboard
    BLACKBOARD = {
        'id': '',
        'snake': dict(),
        'nearest_snake': dict(),
        'nearest_food': (0, 0),
        'snakes': list(),
        'enemy_snakes': list(),
        'food': list(),
    }

    graph = None

    def __init__(self, data):
        """Initializes object based on Battlesnake game data"""
        self.graph = Graph(data['width'], data['height'])

    def get_taunt(self, category, key):
        """Return taunt based on category and key parameters"""
        return self.TAUNTS[category].get(key)

    def get_random_taunt(self, category):
        """Return random taunt based on category parameter"""
        random_key = random.choice(list(self.TAUNTS[category]))

        return self.TAUNTS[category].get(random_key)

    def get_move(self):
        """Returns the next moves relative direction"""
        snake_head = self.BLACKBOARD['snake']['coords'][0]
        snake_tail = self.BLACKBOARD['snake']['coords'][-1]
        nearest_food = self.BLACKBOARD['nearest_food']
        nearest_snake = self.BLACKBOARD['nearest_snake']

        current_farthest_node = pathfinding.find_farthest_node(
            self.graph,
            snake_head
        )
        current_farthest_path = pathfinding.find_path(
            self.graph,
            snake_head,
            current_farthest_node,
        )
        current_path_to_tail = pathfinding.find_path(
            self.graph,
            snake_head,
            snake_tail,
        )

        path = None

        if self.BLACKBOARD['snake']['health'] <= 50:
            nearest_food_cost = pathfinding.cost(snake_head, nearest_food)
            nearest_snake_food_cost = sys.maxsize
            potential_path = None

            if nearest_snake is not None:
                nearest_snake_food_cost = pathfinding.cost(
                    nearest_food,
                    nearest_snake
                )

            if nearest_food_cost < nearest_snake_food_cost:
                potential_path = pathfinding.find_path(
                    self.graph,
                    snake_head,
                    nearest_food,
                )

            if potential_path:
                future_coord = potential_path[0]
                future_farthest_node = pathfinding.find_farthest_node(
                    self.graph,
                    future_coord
                )
                future_farthest_path = pathfinding.find_path(
                    self.graph,
                    snake_head,
                    future_farthest_node,
                )

                if len(future_farthest_path) >= len(current_farthest_path) - 1:
                    path = potential_path

        if not path:
            if current_path_to_tail:
                path = current_path_to_tail
            else:
                path = current_farthest_path

        next_coord = path[0]

        diff = (
            next_coord[0] - snake_head[0],
            next_coord[1] - snake_head[1]
        )

        if diff == (0, 1):
            return 'down'
        elif diff == (0, -1):
            return 'up'
        elif diff == (1, 0):
            return 'right'
        else:
            return 'left'

    def update(self, data):
        """Updates object based on Battlesnake turn data"""
        snake = dict()
        snakes = list()
        enemy_snakes = list()

        for snake in data['snakes']:
            if snake['id'] == data['you']:
                snake = snake
            else:
                enemy_snakes.append(snake)

            snakes.append(snake)

        self.BLACKBOARD['id'] = data['you']
        self.BLACKBOARD['snake'] = snake
        self.BLACKBOARD['snakes'] = snakes
        self.BLACKBOARD['enemy_snakes'] = enemy_snakes
        self.BLACKBOARD['food'] = data['food']

        # Update graph
        self.graph.update(self.BLACKBOARD)

        self.BLACKBOARD['nearest_snake'] = self.__find_nearest_snake_node()
        self.BLACKBOARD['nearest_food'] = self.__find_nearest_food_node()

    def __find_nearest_snake_node(self):
        coord_1 = self.BLACKBOARD['snake']['coords'][0]
        enemy_snakes = self.BLACKBOARD['enemy_snakes']
        enemy_snake_nodes = list()

        for enemy_snake in enemy_snakes:
            enemy_snake_nodes.append(enemy_snake['coords'][0])

        return pathfinding.find_closest_node(coord_1, enemy_snake_nodes)

    def __find_nearest_food_node(self):
        coord_1 = self.BLACKBOARD['snake']['coords'][0]
        food = self.BLACKBOARD['food']

        return pathfinding.find_closest_node(coord_1, food)
