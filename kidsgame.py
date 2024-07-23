# lets create an example word list
word_list = {
    'Easy': ['ant', 'bat', 'cat', 'lion', 'beetroot', 'london', 'use', 'very', 'ingenious', 'hot', 'nellore', 'realize'],
    'medium': ['aggressive', 'transcribe', 'knowledge', 'diligent', 'wallpaper', 'entrepreneur', 'futuristic', 'possessive', 'yellow', 'japanese'],
    'difficult': ['xylophone', 'opaque', 'ingenious', 'gullible', 'zebra', 'quasar', 'juxtapose', 'superstitious', 'metrix']
}
#Random letter selection

import random
import string

random_letter = random.choice(string.ascii_lowercase)
print(f"The random letter is:",random_letter)

# now lets ask the kids to think of a word with this letter and check if thw word is correct and in the wordlist


#function to check if the word is in the wordlist
def check_word(wrd, letter):
    if not wrd.startswith(letter):
        return False, None
    
    for level, words in word_list.items():
        if wrd in words:
            return True, level

    return False, None

while True:
    res = input(f"Think and Write a word with the letter '{random_letter}':").strip().lower()
    print(f"you enetred:", res)
    
    is_valid,difficulty_level = check_word(res, random_letter)

#function to provide feedback
    if is_valid:
        print("Good work!")
        print(f"the difficulty level of your word is :",difficulty_level.capitalize())
        break

    else:
        if res.startswith(random_letter):
            print(f"'{res}' starts with the correct letter', but it's not in our list. Try again!")
        else:
            print(f"oops! '{res}' doesnt start with '{random_letter}'. Try again!")      

