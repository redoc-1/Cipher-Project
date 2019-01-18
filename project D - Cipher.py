#!/usr/bin/env python
# coding: utf-8

# In[18]:


# hardcoding string and a list that is going to be used onward

array = "abcdefghijklmnopqrstuvwxyz"
array_list = [
    'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L',
    'M', 'N', 'O', 'P', 'Q', 'R',
    'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z'
]

# function for encrypting data and adding up letters to dictionary from an encrypted text

# encryption part


def encode():

    text = input("Please enter text you want to encrypt:\n ")
    encrypted = ""
    key = 4

    for c in text:
        if c.isalpha():
            if c.islower():
                encrypted += array[(array.index(c) + key) % 26]
                #letters[c] = letters.get(c, 0) + 1
            elif c.isupper():
                encrypted += array_list[(array_list.index(c) + key) % 26]
                #letters[c] = letters.get(c, 0) + 1
        else:
            encrypted += c

# letters' dictionary
    letters = dict()
    encrypted_list = list(encrypted)

    for h in encrypted_list:
        letters[h] = letters.get(h, 0) + 1

    return print("\nYour text has been successfully encrypted:\n", encrypted,
                 "\n\nThe most poular letters are:\n", letters)


# function for decrypting data
def decode():

    _encrypted = input("Enter text you want to decrypt:\n ")
    decrypting = ""
    key = 4

    for d in _encrypted:
        if d.isalpha():
            if d.islower():
                decrypting += array[(array.index(d) - key) % 26]
            elif d.isupper():
                decrypting += array_list[(array_list.index(d) - key) % 26]
        else:
            decrypting += d

    return print("\nYour text has been successfully decrypted:\n", decrypting)


# creating class for a project owner
class User:

    def __init__(self, firstname, surname):
        self.firstname = firstname
        self.surname = surname


owner = User("Viktoras", "Vovčenko")

print(" A PROJECT BY\n", owner.firstname, owner.surname, "\n\n")
encode()
decode()


# In[ ]:
