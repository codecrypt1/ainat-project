import boto3

dynamodb = boto3.resource(
    "dynamodb",
    # aws_access_key_id = "AKIASLMV25ZHBN5VE6O4",
    # aws_secret_access_key = "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"
)

# Create dynamo table
table = dynamodb.create_table(
    TableName = "users",
    KeySchema = [
        {
            "AttributeName": "email",
            "KeyType": "HASH"
        }
    ],
    AttributeDefinitions = [
        {
            "AttributeName": "email",
            "AttributeType": "S"
        }
    ],
    ProvisionedThroughput = {
        "ReadCapacityUnits": 5,
        "WriteCapacityUnits": 5
    }
)

table.meta.client.get_waiter("table_exists").wait(TableName="users")

print(table.item_count)