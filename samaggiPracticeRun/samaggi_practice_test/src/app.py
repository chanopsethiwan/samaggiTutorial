import json
from .user import PynamoUser


def test(event, context):
    return {'data': 'Hello World'}

def get_user(event, context):
    item = event['arguments']
    user_id = item['user_id']
    iterator = PynamoUser.query(user_id)
    user_list = list(iterator)
    lst = []
    if len(user_list) > 0:
        for user in user_list:
            lst.append(user.returnJson())
    else:
        return {'status': 400}

    return {'status': 200,
            'data': lst}