import json


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def lambda_handler(event, context):
    try:
        number = int(event['pathParameters']['number'])

        result = factorial(number)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "result": result
            }),
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "error": str(e)
            })
        }
