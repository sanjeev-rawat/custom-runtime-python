#!/usr/bin/env python
import sys, json

def handler(event, context):
    event = json.loads(event)
    name = event["name"]
    age = event["age"]
    message = "Hello " + name + " age is " + str(age)
    return json.dumps({
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {
            "message ": message
        }
    })

if __name__ == "__main__":
    event_data = sys.argv[1]
    result = handler(event_data, None)
    print(result)