"""A* algorithm based on http://www.redblobgames.com/pathfinding/a-star/implementation.html"""

import sys
from queue import PriorityQueue

def cost(node_1, node_2):
    """Determines the approximate cost going from one coord to another"""

    return abs(node_1[0] - node_2[0]) + abs(node_1[1] - node_2[1])

def a_star(graph, start_node, goal_node):
    """Determines a good path from start to goal based on heuristic"""
    to_visit = PriorityQueue()
    to_visit.put((0, start_node))
    came_from = {}
    cost_so_far = {}
    came_from[start_node] = None
    cost_so_far[start_node] = 0

    while not to_visit.empty():
        current_node = to_visit.get()[1]

        if current_node == goal_node:
            break

        for next_node in graph.neighbors(current_node):
            new_cost = cost_so_far[current_node] + cost(current_node, next_node)

            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost
                to_visit.put((priority, next_node))
                came_from[next_node] = current_node

    return __build_path(start_node, goal_node, came_from)

def find_path(graph, start_node, goal_node, algorithm = a_star):
    """Find path between two nodes in a given algorithm"""
    return algorithm(graph, start_node, goal_node)

def find_closest_node(node_1, nodes):
    """Finds the closest node amongst a list of nodes"""
    lowest_cost_node = None
    lowest_cost = sys.maxsize

    if not nodes:
        return lowest_cost_node

    for node_2 in nodes:
        current_cost = cost(node_1, node_2)

        if lowest_cost > current_cost:
            lowest_cost_node = node_2
            lowest_cost = current_cost

    return lowest_cost_node

def find_farthest_node(graph, node_1):
    """Get a farthest point given a node"""
    nodes = __flood_fill(graph, node_1)
    highest_cost_node = None
    highest_cost = 0

    for node_2 in nodes:
        current_cost = cost(node_1, node_2)

        if current_cost > highest_cost:
            highest_cost_node = node_2
            highest_cost = current_cost

    return highest_cost_node

def __build_path(start_node, goal_node, nodes):
    """Builds a path from start to goal node based on graph of nodes"""
    # Build path array based on path mapping
    current_node = goal_node
    path = list()

    while current_node != start_node:
        # If node is not in mapping, no path exists
        if current_node in nodes:
            path.append(current_node)
            current_node = nodes[current_node]
        else:
            # Set path to empty if no path exists and exit
            path = list()
            break

    path.reverse()

    return path

def __flood_fill(graph, node):
    """Flood fills based on current node"""
    results = [node]
    nodes = [node]

    while len(nodes) > 0:
        current_node = nodes.pop()
        neighbors = graph.neighbors(current_node)

        for neighbor in neighbors:
            if neighbor not in results:
                results.append(neighbor)
                nodes.append(neighbor)

    return results
