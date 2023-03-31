import random

#function for encoding message
def encode(message, key):

    bin_message = ''.join(format(ord(char), '08b') for char in message)
    bin_key = ''.join(format(ord(char), '08b') for char in key)
    encoded_format = ''.join(str(int(bin_message[i]) ^ int(bin_key[i % len(bin_key)])) for i in range(len(bin_message)))

    encoded_message = ''
    for i in range(0, len(encoded_format), 8):
        encoded_message += chr(int(encoded_format[i:i+8], 2))
    
    return encoded_message

#function for decoding message
def decode(encoded_message, secret_key):

    bin_encoded = ''.join(format(ord(char), '08b') for char in encoded_message)
    
    bin_key = ''.join(format(ord(char), '08b') for char in secret_key)
    decoded_bin = ''.join(str(int(bin_encoded[i]) ^ int(bin_key[i % len(bin_key)])) for i in range(len(bin_encoded)))
    
    decoded_message = ''
    for i in range(0, len(decoded_bin), 8):
        decoded_message += chr(int(decoded_bin[i:i+8], 2))
    
    return decoded_message



    
#Calling Functions
print("Hii Ram, Do you want to send some message to Rahul?")
message = input("Enter message for Rahul: ")
secret_key=''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=8))
#print("secret_key",secret_key)
encoded_message = encode(message,secret_key)
print("Message sended to rahul in this format: ")
print(encoded_message)

print("Ask Rahul to decode message using same secret Key: ")
decoded_message = decode(encoded_message, secret_key)
print(decoded_message)
