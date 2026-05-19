import boto3
import csv

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('student')

with open('delete.csv', 'r') as file:

    reader = csv.DictReader(file)

    with table.batch_writer() as batch:

        for row in reader:

            batch.delete_item(
                Key={
                    'student_id': row['student_id']
                }
            )

print("Bulk delete completed")