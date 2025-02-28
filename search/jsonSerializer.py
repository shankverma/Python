import json
def json_serializer(dict: dict) -> str:
    """
    Serialize a dictionary to a JSON string
    """
    return json.dumps(dict, indent=2)

def json_deserializer(json_str: str) -> dict:
    """
    Deserialize a JSON string to a dictionary
    """
    return json.loads(json_str)
    