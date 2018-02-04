"""A graph used for A* pathfinding"""

import game.helpers.pathfinding as pathfinding

class Graph(object):
    """Class representing a Graph"""
    inaccessible_nodes = list()
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def update(self, blackboard):
        """Updates graph based on blackboard data"""
        self.inaccessible_nodes = list()

        for snake in blackboard['snakes']:
            coords = snake['coords']

            for i in range(len(coords) - 1):
                self.inaccessible_nodes.append(coords[i])

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
            node not in self.inaccessible_nodes
            and self.__is_node_in_bounds(node)
        )

    def __is_node_in_bounds(self, node):
        """Checks if a node is in the graph bounds"""

        if node[0] < 0 or node[0] >= self.width:
            return False
        elif node[1] < 0 or node[1] >= self.height:
            return False
        else:
            return True
