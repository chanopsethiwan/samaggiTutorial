import json
from .user import PynamoUser
from uuid import uuid4

def hello_world(event, context):
    return {'data': 'Hello World'}

def get_user(event, context):
    item = event['arguments']
    user_id = item['user_id']
    iterator = PynamoUser.query(user_id, consistent_read=True)
    user_list = list(iterator)
    lst = []
    if len(user_list) > 0:
        for user in user_list:
            lst.append(user.returnJson())
    else:
        return {'status': 400}

    return {'status': 200,
            'data': lst}

def add_user(event, context):
    item = event['arguments']
    user_uuid = str(uuid4())
    user_item = PynamoUser(
        user_id = user_uuid,
        username = item['username'],
        age = item['age']
    )
    user_item.save()
    return {'status':200}