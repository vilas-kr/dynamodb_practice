import boto3
import csv

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Students')

try:
    with open('students.csv', 'r') as file:

        reader = csv.DictReader(file)

        with table.batch_writer() as batch:

            for row in reader:

                batch.put_item(
                    Item={
                        'student_id': row['student_id'],
                        'name': row['name'],
                        'age': int(row['age']),
                        'address': row['address']
                    }
                )

    print("Data inserted successfully")

except Exception as e:
    print("Error:", e)