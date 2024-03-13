import json

def encode_to_json(data):
    return json.dumps(data, default=lambda x: None if x is None else x)

input_data = [None, 123, ["a", "b"], {"c": "d"}]
result = encode_to_json(input_data)
print(result)