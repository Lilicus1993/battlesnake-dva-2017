"""A graph used for A* pathfinding"""

import game.helpers.pathfinding as pathfinding

class Graph(object):
    """Class representing a Graph"""
    inaccessible_nodes = []
    width = -1
    height = -1

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
        results = []
        for direction in directions:
            neighbor = (node[0] + direction[0], node[1] + direction[1])
            if self.is_node_in_bounds(node) and neighbor not in self.inaccessible_nodes:
                results.append(neighbor)
        return results

    def find_path(self, node_1, node_2):
        """Updates the A* pathing logic"""
        # Obtain path mapping based on graph and start/end points
        path = pathfinding.a_star(
            self,
            node_1,
            node_2
        )

        return path

    def find_closest(self, node_1, nodes):
        """Finds the closest node amongst a list of nodes"""
        lowest_cost_node = None
        lowest_cost = -1

        if not nodes:
            return

        for node_2 in nodes:
            cost = pathfinding.cost(node_1, node_2)

            if lowest_cost == -1 or lowest_cost > cost:
                lowest_cost_node = node_2
                lowest_cost = cost

        return lowest_cost_node

    def farthest_node(self, node_1):
        """Get a farthest point given a node"""
        nodes = self.__flood_fill(node_1)
        highest_cost_node = (-1, -1)
        highest_cost = -1

        for node_2 in nodes:
            cost = pathfinding.cost(node_1, node_2)
            if cost > highest_cost:
                highest_cost_node = node_2
                highest_cost = cost

        return highest_cost_node

    def is_node_in_bounds(self, node):
        """Make sure node is in bounds"""

        if node[0] < 0 or node[0] >= self.width:
            return False
        elif node[1] < 0 or node[1] >= self.height:
            return False
        else:
            return True

    def __flood_fill(self, node):
        """Flood fills based on current node"""
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        results = [node]
        nodes = [node]
        while len(nodes) > 0:
            eval_node = nodes.pop()
            for direction in directions:
                neighbor = (eval_node[0] + direction[0], eval_node[1] + direction[1])
                if (
                        neighbor not in results
                        and self.is_node_in_bounds(neighbor)
                        and neighbor not in self.inaccessible_nodes
                ):
                    results.append(neighbor)
                    nodes.append(neighbor)
        return results
