import string
import random

chars=" "+string.ascii_letters+string.digits+string.punctuation
chars=list(chars)
key=chars.copy()
random.shuffle(key)

# print(f"chars:{chars}")
# print(f"key:{key}")

#encryption

text=input("Enter the TEXT:")
encrypted=""

for letters in text:
    index=chars.index(letters)
    encrypted+= key[index]
print(f"Text: {text}")
print(f"Encrypted text: {encrypted}")

