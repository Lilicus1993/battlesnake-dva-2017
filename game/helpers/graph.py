"""A graph used for A* pathfinding"""

import game.helpers.pathfinding as pathfinding

class Graph(object):
    """Class representing a Graph"""
    grid = [[]]
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [[1 for x in range(height)] for y in range(width)]

    def update(self, blackboard):
        """Updates graph based on blackboard data"""
        self.grid = [[1 for x in range(self.height)] for y in range(self.width)]

        snake = blackboard['snake']

        for i in range(len(snake['coords']) - 1):
            coord = snake['coords'][i]
            self.grid[coord[0]][coord[1]] = 999

        for enemy_snake in blackboard['enemy_snakes']:
            coords = enemy_snake['coords']

            for i in range(len(coords)):
                coord = coords[i]
                self.grid[coord[0]][coord[1]] = 999

                if i == 0:
                    tmp_coord = (coord[0], coord[1] + 1)
                    if self.__is_node_in_bounds(tmp_coord):
                        self.grid[tmp_coord[0]][tmp_coord[1]] = 500

                    tmp_coord = (coord[0] + 1, coord[1] + 1)
                    if self.__is_node_in_bounds(tmp_coord):
                        self.grid[tmp_coord[0]][tmp_coord[1]] = 500

                    tmp_coord = (coord[0], coord[1] - 1)
                    if self.__is_node_in_bounds(tmp_coord):
                        self.grid[tmp_coord[0]][tmp_coord[1]] = 500

                    tmp_coord = (coord[0] - 1, coord[1] - 1)
                    if self.__is_node_in_bounds(tmp_coord):
                        self.grid[tmp_coord[0]][tmp_coord[1]] = 500

                for j in range(5):
                    j_index = coord[0] - 2 + j

                    for k in range(3):
                        k_index = coord[1] - 1 - k

                        if self.__is_node_in_bounds((j_index, k_index)):
                            cost = self.grid[j_index][k_index]
                            potential_cost = 50 if k == 0 else 25

                            if cost < potential_cost:
                                self.grid[j_index][k_index] = potential_cost

                    for k in range(3):
                        k_index = coord[1] + 1 + k

                        if self.__is_node_in_bounds((j_index, k_index)):
                            cost = self.grid[j_index][k_index]
                            potential_cost = 50 if k == 0 else 25

                            if cost < potential_cost:
                                self.grid[j_index][k_index] = potential_cost

    def cost(self, node, direction):
        target_node = (node[0] + direction[0], node[1] + direction[1])

        if self.__is_node_in_bounds(target_node):
            return self.grid[target_node[0]][target_node[1]]
        else:
            return 999

    def neighbors(self, node):
        """Returns a list of neighbors of the parameter node"""
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        results = list()

        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])

            if self.is_node_accessible(neighbor):
                results.append(neighbor)

        return results

    def is_node_accessible(self, node):
        """Checks if a node is accessible"""

        return (
            self.__is_node_in_bounds(node)
            and self.grid[node[0]][node[1]] != 999
        )

    def __is_node_in_bounds(self, node):
        """Checks if a node is in the graph bounds"""

        if node[0] < 0 or node[0] >= self.width:
            return False
        elif node[1] < 0 or node[1] >= self.height:
            return False
        else:
            return True
