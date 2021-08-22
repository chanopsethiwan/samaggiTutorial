from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
import os

class PynamoUser(Model):
    class Meta:
        table_name = os.environ.get('USER_TABLE_NAME')
        region = 'eu-west-2'
    
    user_id = UnicodeAttribute(hash_key=True)
    username = UnicodeAttribute(null=True)
    age = NumberAttribute(null=True)

    def returnJson(self):
        return vars(self).get('attribute_values')