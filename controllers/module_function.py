import json


def module_handler(event, context):
    try:
        a = int(event['queryStringParameters']['a'])
        b = int(event['queryStringParameters']['b'])

        result = a % b

        return {
            "statusCode": 200,
            "body": json.dumps({
                "result": result
            })
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": str(e)
            })
        }
