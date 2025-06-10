import requests

def lambda_handler(event, context):
    
    print("Hello World!")

    return {
        "statusCode": 200,
        "body": "this is a test"
    } 