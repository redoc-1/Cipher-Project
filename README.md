## OVERVIEW

The program is built with a goal to demonstrate the Ceaser Cipher encryption technic and an easy way of braking it by identifying the most popular letters within the encrypted text.


It basically contains 3 main parts that include text encryption, decryption and a user class for highlighting a presenter's/project owner's name.


## FIRST PART

The first part of the program replaces letters of the text you want to encrypt by other letters by simply shifting them back or forth. So, for instance if the hard coded key is 2, the program will replace any alphabet letter of your message with the one that stands two symbols away from it on the alphabet, for instance the letter A would be replaced with C or letter K with letter M. 

The first defined function does not only encrypts the data, but also counts the most popular symbols from the encrypted text. Knowing the most popular letters in English language makes it easy to guess a key in order to break a code. Information on the most popular letters may be found under the following URL:

https://en.wikipedia.org/wiki/Letter_frequency

In order to break a code take the most popular letter from the encrypted text and compare it to the most popular letter in English alphabet, a length of these letter' difference will most probably be a key to decryption.


## SECOND AND THIRD PARTs
Pretty much self-explanatory. Decryption function does only decryption and the class method is being used for a demonstration of such functionality, though it does not affect the code anyhow and is optional.


### ADDITIONAL NOTE
In order to increase chances in cracking the code use more text for easier identification of the letter pattern and guessing a key accordingly.
