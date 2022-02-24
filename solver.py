# Imports
import time
from word import Word

# REBUT

# Define rank getting method
def rank(word):
    # Initialize rank
    rank = 0
    
    # Grab the letters
    letters = previous_word.letters

    # Loop through letters
    for index in range(5):
        # Get used letter
        used_letter = previous_word.letters[index]

        # Check for matching letter positions
        if used_letter.status == '@': # In this position
            if letters[index].character == word[index]: rank += 10
        elif used_letter.status == '?': # In word but not in this position
            if letters[index].character in word:
                rank += 2
                if letters[index].character == word[index]: rank -= 20
            else: rank -= 20
        elif used_letter.status == '!': # Not in word or already used in anothe position
            if letters[index].character in word: rank -= 2
            if letters[index].character == word[index]: rank -= 20

    # Return rank
    return rank

# Open words file
words_file = open("words.txt", 'r')

# Read in words file
with words_file as file:
    lines = file.readlines()

# Close words file
words_file.close()

# Populate words list
words = []
for line in lines:
    words.append(line.strip().lower())

# Greet user
print("--- Hello and welcome to Harper's Wordle solver! ---")
time.sleep(1)

# Ask user if they want to skip
print("Skip instructions?")
time.sleep(1)
skip = input("Answer: ").lower()

# Check skip input
if skip == 'n' or skip == 'no':
    # Give user instructions
    time.sleep(1)
    print("\nGo ahead and enter your first word into Wordle.")
    time.sleep(3)
    print("After that, enter the results here with these encodings appended to the front of each letter:")
    time.sleep(3)
    print("!: GREY")
    time.sleep(0.5)
    print("?: YELLOW")
    time.sleep(0.5)
    print("@: GREEN")
    time.sleep(3)
    print("Like so: !B@E!A?R!S")
    time.sleep(2)

# Loop through tried
while(True):
    # Add word to used
    time.sleep(1)
    previous_word = Word(input("\nEnter encoded word: "))

    # Ask user to wait around
    time.sleep(1)
    print(str(previous_word).upper() + "? Excellent. Let me think up a suggestion for your next word.")

    # Sort words from best choices to worst
    words = sorted(words, key=rank)

    # Give new word
    time.sleep(1)
    print("Try this: " + str(words[len(words) - 1]).upper())