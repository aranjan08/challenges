# Confidentiality
# 
#  In this lesson you will learn about confidentiality. Good luck!
# ### Challenge Name: caesar_easy (/embsec/confidentiality/caesar_easy)
# 
# 
#         The serial device is sending you a message which includes a ciphertext 
#         encrypted with a caesar cipher! 
#         
#         The message is in the following format:
#     
#         [      0x2       ] [ variable... ] <-- Field Size(s) in Bytes
#         ----------------------------------
#         | Ciphertext Size |  Ciphertext  | <-- Field Name
#         ----------------------------------
#     
#         1. Read the ciphertext size (formatted as a little-endian short) from the serial device
#         2. Read the ciphertext from the serial device
#         3. Decrypt the ciphertext using the key 20 (rotate each letter by 20)
#         4. Send the plaintext back to the device
#         5. Read the flag from the serial device!
#     
#     Hint: Print the decrypted message, it should be in english and make sense!
#     
#     Resources:
#     
#     <https://docs.python.org/3/library/struct.html>
#     
#     <https://en.wikipedia.org/wiki/Caesar_cipher>
#     
#     <http://www.asciitable.com/>
#     
# 
from embsec import Serial

def caesar_easy():
    ser = Serial("/embsec/confidentiality/caesar_easy")
    # Your code goes here!

caesar_easy()
### Challenge Name: caesar_hard (/embsec/confidentiality/caesar_hard)
# 
# 
#         The serial device is sending you a message which includes a ciphertext 
#         encrypted with a caesar cipher! But now...you don't know the key!
#         
#         The message is in the following format:
# 
#         [      0x2       ] [ variable... ] <-- Field Size(s) in Bytes
#         ----------------------------------
#         | Ciphertext Size |  Ciphertext  | <-- Field Name
#         ----------------------------------
# 
#         1. Read the ciphertext size (formatted as a little-endian short) from the serial device
#         2. Read the ciphertext from the serial device
#         3. Do a frequency analysis to recover the secret key
#         3. Decrypt the ciphertext using the recovered key
#         4. Send the plaintext back to the device
#         5. Read the flag from the serial device!
# 
#     Hint: The Counter class in the collections module may come in handy!
# 
#     Resources:
# 
#     <https://docs.python.org/3/library/struct.html>
# 
#     <https://en.wikipedia.org/wiki/Caesar_cipher>
# 
#     <http://www.asciitable.com/>
#     
# 
from embsec import Serial

def caesar_hard():
    ser = Serial("/embsec/confidentiality/caesar_hard")
    # Your code goes here!

caesar_hard()
