import binascii
import base64

def hex_to_base64(hex_string):
    binary_data = binascii.unhexlify(hex_string)


    base64_data = base64.b64encode(binary_data)
    
    return base64_data.decode('utf-8')


hex_string = 'deadbeef'
print(hex_to_base64(hex_string))