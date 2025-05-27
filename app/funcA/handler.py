import requests

def lambda_handler(event, context):
    
    resp = requests.get("https://catfact.ninja/fact") 
    fact = resp.json().get("fact", "No fact found.")

    return {
        "statusCode": 200,
        "body": fact
    }