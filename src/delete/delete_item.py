import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('student')

response = table.delete_item(
    Key={
        'student_id': '10090'
    },
    ReturnValues='ALL_OLD'
)

print(f"Item deleted: {response}")