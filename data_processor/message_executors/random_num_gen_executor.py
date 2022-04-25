import json


def message_executor(message, consumer_group):
    try:
        data = json.loads(message)
        with open('../../randomnumberfile.txt', 'a') as f:
            f.write(json.dumps(data) + "\n")
    except Exception as e:
        raise e

