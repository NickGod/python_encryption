import random

# list of English words (hint: may want to use a different data structure for faster lookup...)
# To check if a word is an English word, call isEnglishWord()
wordList = open('EnglishWords.txt').read().split()
sampleSentences = open('SampleText.txt').read().split('\n')
sampleSentences = [x for x in sampleSentences if not x == '']
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = ''


def isEnglishWord(w):
    for word in wordList:
        if (word == w):
            return True
    return False

def cipher_encrypt(m, k):
    encrypted = ''
    charsA = LETTERS
    global key
    key = ''.join(random.sample(LETTERS,len(LETTERS)))
    charsB = key
    # return the encrypted string
    # m is the message, k is the key
    for symbol in m:
        if symbol.upper() in charsA:
            
            symbolIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                encrypted += charsB[symbolIndex].upper()
            else:
                encrypted += charsB[symbolIndex].lower()
        else:
            encrypted += symbol


    return encrypted

def cipher_decrypt(c, k):
    # return the decrypted string
    # c is the ciphered text, k is the key
    decrypted = ''
    global key
    charsA = key
    charsB = LETTERS
    # return the encrypted string
    # m is the message, k is the key
    for symbol in c:
        if symbol.upper() in charsA:
            symbolIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                decrypted += charsB[symbolIndex].upper()
            else:
                decrypted += charsB[symbolIndex].lower()
        else:
            decrypted += symbol


    return decrypted

def cipher_break(c):
    # implement this in TIER 2
    return ""
        
        

# TEST THE IMPLEMENTATION
# ------------------------------------------------------------
testText = """
A trapdoor function is a function that is easy to compute in one direction, yet believed to be difficult to compute in the opposite direction (finding its inverse) without special information, called the "trapdoor". Trapdoor functions are widely used in cryptography.
"""

failed = False

encrypted_text = ""

# for i in range(50):
#     encrypted_text = cipher_encrypt(testText, i)
# print encrypted_text

# print "trying to decrypt text"
# for i in range(50):
#     decrypted_text = cipher_decrypt(encrypted_text, i)
# print decrypted_text

for i in range(1000):
    if(not testText == cipher_decrypt(cipher_encrypt(testText, i), i)):
        print "Failed at key %d" % i
        failed = True
        
if(not failed):
    print "Succeeded for all test keys!"

sentence = random.choice(sampleSentences)

print "chose sentence: \"%s\"" % sentence

# don't worry about this next line, k?
ciphertext = cipher_encrypt(sentence, random.randint(0, 2**32))

if cipher_break(ciphertext) == sentence:
    print "break succeeded!"
else:
    print "break failed!"
# ------------------------------------------------------------
