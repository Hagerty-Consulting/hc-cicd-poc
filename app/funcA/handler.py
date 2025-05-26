import requests

def lambda_handler(event, context):
    try:
        response = requests.get("https://api.github.com")
        data = response.json()
        return {
            "statusCode": 200,
            "body": {
                "api_status": data.get("current_user_url", "not found")
            }
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }