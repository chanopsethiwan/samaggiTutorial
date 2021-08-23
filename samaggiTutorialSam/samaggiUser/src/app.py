import json
from .user import PynamoUser
from uuid import uuid4
import boto3
from boto3.dynamodb.conditions import Key
import os

def hello_world(event, context):
    return {'data': 'Hello Gai'}

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

    ##### init boto3
    # dynamodb = boto3.resource('dynamodb')
    # table = dynamodb.Table(os.environ.get('USER_TABLE_NAME'))
    
    #### SELECT * FROM table WHERE user_id='6'
    # response =  table.get_item(Key={'user_id': str(user_id)})


    ##### SELECT * FROM table
    # response = table.scan()

    # lst_temp = response['Item'] # For get_item
    # lst = [lst_temp]
    # lst = response['Items'] # For query
    
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