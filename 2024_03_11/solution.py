import binascii
import base64

def base64_to_hex(base64_string):
    binary_data = base64.b64decode(base64_string)
    
    hex_data = binascii.hexlify(binary_data)

    return hex_data.decode('utf-8')

base64_string = '3q2+7w=='
print(base64_to_hex(base64_string)) 