from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
import os

class PynamoUser(Model):
    class Meta:
        table_name = "SamaggiPracticeRunUser"
        region = 'eu-west-2'
    user_id = UnicodeAttribute(hash_key = True)
    username = UnicodeAttribute()
    age = NumberAttribute()