"""Django views"""

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from snake.dva import DVA

@api_view(['POST'])
@parser_classes((JSONParser,))
def start(request):
    """Handles a start request"""
    data = request.data

    dva = DVA()
    dva.init(data)

    response = dict(
        color=dva.get_color(),
        taunt=dva.get_random_taunt('set_up'),
        head_url="%s%s" % (request.build_absolute_uri('/'), dva.get_image_url()),
        name=dva.get_name()
    )
    return Response(response)

@api_view(['POST'])
@parser_classes((JSONParser,))
def move(request):
    """Handles a move request"""
    data = request.data
    data['snakes'] = data['snakes']['data']

    data['you'] = data['you']['id']

    for snake in data['snakes']:
        snake['coords'] = snake['body']['data']

        for index, coord in enumerate(snake['coords']):
            snake['coords'][index] = [coord['x'], coord['y']]

    data['food'] = data['food']['data']

    for index, food in enumerate(data['food']):
        data['food'][index] = [food['x'], food['y']]

    dva = DVA()
    dva.init(data)
    dva.update(data)
    next_move = dva.get_move()

    response = dict(
        move=next_move
    )

    return Response(response)

def get_game(game_id):
    """Returns a game instance"""
    for game in GAMES:
        local_game_id = game[0]
        if game_id == local_game_id:
            return game

    return None
