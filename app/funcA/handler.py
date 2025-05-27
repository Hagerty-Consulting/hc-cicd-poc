from pyfiglet import Figlet

def lambda_handler(event, context):

    text = event.get("queryStringParameters", {}) .get("text", "Hello")
    fig = Figlet(font="standard")
    art = fig.renderText(text)
    return {
        "statusCode": 200,
        "body": art
    }