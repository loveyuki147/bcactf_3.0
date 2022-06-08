from Crypto.Util.number import inverse
import string
LETTERS = string.digits + string.ascii_lowercase + "_"

# (cipher - key_1) * key_0^-1 % len(LETTERS)
def dcode_affine_cipher(message, key):
    translated = '' 
    modInverseOfKeyA = inverse(key[0], len(LETTERS))
    for symbol in message:
        symIndex = LETTERS.find(symbol)
        translated += LETTERS[(symIndex - key[1]) * modInverseOfKeyA % len(LETTERS)]

    return translated

pair_letters_curr = 'bc'
cipher = 'bx6ez_unufi3bm0r0xeb'

flag = pair_letters_curr
for i in range(0, len(cipher), 2):
    pair_letters_cipher = cipher[i : i + 2]
   
    a = LETTERS.index(pair_letters_curr[0])
    b = LETTERS.index(pair_letters_curr[1])
    pair_letters_curr = dcode_affine_cipher(pair_letters_cipher, (a, b))
    flag += pair_letters_curr

flag = flag[:6] + '{' + flag[6:]+ "}"
print(flag)
        

        
        