"""A* algorithm based on http://www.redblobgames.com/pathfinding/a-star/implementation.html"""

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

def __build_path(start_node, goal_node, nodes):
    """Builds a path from start to goal node based on graph of nodes"""
    # Build path array based on path mapping
    current_node = goal_node
    path = []

    while current_node != start_node:
        # If node is not in mapping, no path exists
        if current_node in nodes:
            path.append(current_node)
            current_node = nodes[current_node]
        else:
            # Set path to empty if no path exists and exit
            path = []
            break

    path.reverse()

    return path
