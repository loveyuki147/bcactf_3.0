from Crypto.Util.number import *
import string
LETTERS = string.ascii_lowercase + string.digits + "_"
LETTERS = '0123456789bcdefghijklmnopqrstuvwxyz_'


# Return Affine Cipher with MODE encrypt or decrypt
def dcode_affine_cipher(message, key):
    message = message.lower()
    translated = ''
    
    l = len(LETTERS)
    modInverseOfKeyA = inverse(key[0], l)
    
    for symbol in message:
        symIndex = LETTERS.find(symbol)
        if symIndex == -1:
            translated += symbol
        else:
            translated += LETTERS[(symIndex - key[1]) * modInverseOfKeyA % l]

    return translated

cipher = 'bx6ez_unufi3bm0r0xeb'

def split_strings(s, n):
    split_strings = []
    for index in range(0, len(s), n):
        split_strings.append(s[index : index + n])
    return split_strings

for i in range(len(LETTERS)):
    for j in range(len(LETTERS)):
        key = (i, j)
        
        message = dcode_affine_cipher(cipher, key)
   
        #print(message)
        if 'ctf' in message:
            print(key, message)
        m_a = split_strings(message, 2)
           
        

        
        