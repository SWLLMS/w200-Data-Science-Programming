import sys
import string

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

#Get the Scrabble rack from the command line.
if len(sys.argv) < 2 & len(sys.argv) < 7:
    print("no rack error.")
    exit(1)
else:
    raise Exception('Oops, your rack is fewer than 2 or larger than 7')

## NEED TO LIMIT INPUT TO ONE * AND ?
#while True:
   # try:
      #  if len(sys.argv) < 2:
        #    raise Exception('You have not entered enough letters in your rack.')
        #    continue
       # if len(sys.argv) > 7:
       #     raise Exception('You have too many letters in your rack.')
       #     continue
       # print("no rack error.")
       # exit(1)
   # else:
     #   break

rack = sys.argv[1]
rack_lowercase = rack.lower()


# Turn the words in the sowpods.txt file into a Python list.
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]

# Find all of the valid sowpods words that can be made
# up of the letters in the rack.
valid_words = []
wildcard_scores = {'*': 0, '?': 0}
scores = {**scores, **wildcard_scores}

def scrabble_word(word):
    rack_letters = list(rack_lowercase)
    for letter in word_lowercase:
        if letter in rack_letters:
            rack_letters.remove(letter)
        elif '*' in rack_letters:
            rack_letters.remove('*')
        elif '?' in rack_letters:
            rack_letters.remove('?')
        else:
            return False
    return True


for word in data:
    word_lowercase = word.lower()
    if scrabble_word(word_lowercase):
            # Get the Scrabble scores for each word.
        total = 0
        for letter in word_lowercase:
            total = total + scores[letter]
        valid_words.append([total, word_lowercase])

# Print the valid words, sorted by Scrabble score.

valid_words.sort(reverse = True)
for entry in valid_words:
    score = entry[0]
    word_low = entry[1]
    print((score, word_low))

print("Total number of words:", len(valid_words))
