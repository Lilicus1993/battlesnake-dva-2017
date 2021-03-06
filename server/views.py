"""Django views"""

from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from server.helpers.sanitizer import sanitize_start_data, sanitize_move_data
import game.game as bs_game

@api_view(['POST'])
@parser_classes((JSONParser,))
def start(request):
    """Handles a start request"""
    data = sanitize_start_data(request.data)
    game = bs_game.factory(data)
    dva = game.dva

    response = dict(
        color=dva.COLOR,
        taunt=dva.get_random_taunt('set_up'),
        head_url="%s%s" % (request.build_absolute_uri('/'), dva.IMAGE_URL),
        name=dva.NAME
    )

    return Response(response)

@api_view(['POST'])
@parser_classes((JSONParser,))
def move(request):
    """Handles a move request"""
    data = sanitize_move_data(request.data)
    game = bs_game.factory(data)
    game.update(data)
    dva = game.dva

    next_move = dva.get_move()

    response = dict(
        move=next_move
    )

    return Response(response)
