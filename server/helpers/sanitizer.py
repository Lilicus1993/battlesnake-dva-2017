"""Saniziters for web server data"""

def sanitize_start_data(data):
    """Sanitize start request data"""
    data['id'] = data['game_id']

    return data

def sanitize_move_data(data):
    """Sanitize move request data"""
    data['snakes'] = data['snakes']['data']

    data['you'] = data['you']['id']

    for snake in data['snakes']:
        snake['coords'] = snake['body']['data']

        for index, coord in enumerate(snake['coords']):
            snake['coords'][index] = (coord['x'], coord['y'])

    data['food'] = data['food']['data']

    for index, food in enumerate(data['food']):
        data['food'][index] = (food['x'], food['y'])

    return data
