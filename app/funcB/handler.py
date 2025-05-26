import datetime

def lambda_handler(event, context):
    now = datetime.datetime.utcnow()
    return {
        "statusCode": 200,
        "body": {
            "timestamp": now.isoformat() + "Z"
        }
    }