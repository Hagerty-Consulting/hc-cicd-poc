import requests

def lambda_handler(event, context):
    # fetch a random cat fact
    resp = requests.get("https://catfact.ninja/fact")
    fact = resp.json().get("fact", "No fact found.")
    return {
        "statusCode": 200,
        "body": fact
    }