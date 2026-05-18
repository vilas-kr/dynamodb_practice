import boto3
from decimal import Decimal

dynamo_db = boto3.resource("dynamodb")
table = dynamo_db.Table("students")

# get one item with only required fields
response = table.get_item(
    Key={
        'student_id': '1001'
    },
    ProjectionExpression='student_id, #n',
    ExpressionAttributeNames={
        '#n': 'name'
    },
)
print(response['Item'])