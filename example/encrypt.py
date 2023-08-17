import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
char = "*"
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key  : {key}")


plain_text = input("Enter Your password to encrypt: ")
cipher_text = ""
length_text = (len(plain_text))

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

 
print(f"orginal password: {char * length_text} ")  
print(f"encryted password: {cipher_text}")   
    
cipher_text = input("Enter Your encyted password: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text  += chars[index]
    
print(f"encryted password: {cipher_text}") 
print(f"orginal password: {plain_text} ")  
   