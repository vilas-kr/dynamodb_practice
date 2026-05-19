import boto3

dynamo_db = boto3.resource("dynamodb")
table = dynamo_db.Table("student")

response = table.update_item(
    Key={
        'student_id': '1001'
    },
    UpdateExpression='SET age = :a',
    ConditionExpression='attribute_exists(student_id)',
    ExpressionAttributeValues={
        ':a': 30
    },
    ReturnValues='ALL_NEW'
)

print(response["Attributes"])