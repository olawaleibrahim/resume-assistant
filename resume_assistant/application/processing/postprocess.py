import json

def get_json_from_result(result):
    return json.loads(result.content[8:-4])