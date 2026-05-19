# bulk scan 
import boto3
import csv
from decimal import Decimal

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb')

# Select table
table = dynamodb.Table('student')

# Scan entire table
response = table.scan()

items = response['Items']

# Handle pagination
while 'LastEvaluatedKey' in response:

    response = table.scan(
        ExclusiveStartKey=response['LastEvaluatedKey']
    )

    items.extend(response['Items'])

# Convert Decimal to int/float
def convert_decimal(obj):

    if isinstance(obj, Decimal):

        if obj % 1 == 0:
            return int(obj)

        return float(obj)

    return obj

# Write to CSV
with open('students_output.csv', mode='w', newline='') as file:

    if items:

        # CSV column names
        fieldnames = items[0].keys()

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for item in items:

            cleaned_item = {
                k: convert_decimal(v)
                for k, v in item.items()
            }

            writer.writerow(cleaned_item)

print("Data exported successfully")