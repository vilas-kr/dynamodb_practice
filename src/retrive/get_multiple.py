import boto3
dynamo_db = boto3.resource("dynamodb")

response = dynamo_db.batch_get_item(
    RequestItems={
        'student': {
            'Keys': [
                {'student_id': '1001'},
                {'student_id': '1010'}
            ]
        }
    }
)
response = response['Responses']['student']

def convert_to_int(v):
    if isinstance(v, Decimal):
        if v%1 == 0:
            return int(v)
        else : 
            return float(v)

    return v

for i in response:
    result = [convert_to_int(v) for k, v in i.items()]
    print(result)
    
# production grade code using recursion
from decimal import Decimal

def convert_data(obj):

    if isinstance(obj, list):

        return [convert_data(i) for i in obj]

    elif isinstance(obj, dict):

        return {k: convert_data(v) for k, v in obj.items()}

    elif isinstance(obj, Decimal):

        if obj % 1 == 0:
            return int(obj)

        return float(obj)

    return obj