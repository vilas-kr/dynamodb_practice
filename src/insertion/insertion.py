import boto3

dynamo_db = boto3.resource("dynamodb")
table = dynamo_db.Table("student")

result = table.put_item(
    Item = {
        'student_id':"10090",
        'name': 'vilas',
        'age':56,
        'address': 'Davangere'
    },
    ConditionExpression='attribute_not_exists(#n)',
    ExpressionAttributeNames={
        '#n': 'name'
    }
)

print(result)