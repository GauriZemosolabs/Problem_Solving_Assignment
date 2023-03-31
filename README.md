# Problem_Solving_Assignment
Problem Statement: Data Encryption System: Rahul wants to send encoded messages to his friend Ram. Develop an algorithm to encode all the digits, special characters, lower and upper case alphabets.

Flow of code for encoding:
1. Created a random secret key.
2. Entered message to be decoded.
3. Converted message into ASCII value and then into binary format.
4. Similarly convert secret key into ASCII value and then into binary format.
5. Perform XOR operation between each bit of bin_key and bin_message.
6. Create clusters of 8 bits and convert then into string.
7. Return the encoded message.

Flow of code for decoding:
1. Take inputs - encoded message and secret_key as strings.
2. Convert message into ASCII value and then into binary format.
3. Similarly convert secret key into ASCII value and then into binary format.
4. Perform XOR operation between each bit of bin_key and bin_message.
5. Create clusters of 8 bits and convert then into string.
6. Return the Decoded message
