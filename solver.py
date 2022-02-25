# Imports
import time
import helper
from word import Word

# Settings
green_code = '@'
yellow_code = '?'
grey_code = '!'

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
        if used_letter.status == green_code: # In this position
            if letters[index].character == word[index]: rank += 10
        elif used_letter.status == yellow_code: # In word but not in this position
            if letters[index].character in word:
                rank += 2
                if letters[index].character == word[index]: rank -= 20
            else: rank -= 20
        elif used_letter.status == grey_code: # Not in word or already used in anothe position
            if letters[index].character in word: rank -= 2
            if letters[index].character == word[index]: rank -= 20

    # Return rank
    return rank

# Populate possible words list
possible_words = helper.load_words("words.txt")

# Greet user
print("----- Hello and welcome to Harper's Wordle solver! -----")
time.sleep(1)

# Ask user if they want to skip instructions
print("Skip instructions?")
time.sleep(1)
skip = input("Answer: ").lower()

# Check if user wants to skip instructions
if skip == 'n' or skip == 'no':
    # Give user instructions
    time.sleep(1)
    print("\nGo ahead and enter your first word of choice into Wordle.")
    time.sleep(3)
    print("After that, enter the results here with these encodings before each letter:")
    time.sleep(3)
    print(green_code + ": GREEN")
    time.sleep(0.5)
    print(yellow_code + ": YELLOW")
    time.sleep(0.5)
    print(grey_code + ": GREY")
    time.sleep(3)
    print(
        "Like so: "
        + grey_code + "C"
        + green_code + "R"
        + grey_code + "A"
        + yellow_code + "N"
        + grey_code + "E"
    )
    time.sleep(3)
    print("The program will keep running until you enter EXIT.")
    time.sleep(2)

# Loop through tried
while(True):
    # Get user input
    time.sleep(1)
    user_input = input("\nEnter: ").replace(" ", "").lower()
    if user_input == 'exit': break
    if len(user_input) != 10:
        print("Input formatting wrong.")
        continue

    # Encode user input
    previous_word = Word(user_input)

    # Ask user to wait around
    time.sleep(1)
    print(str(previous_word).upper() + "? Excellent. Let me think up a suggestion for your next word.")

    # Sort words from best choices to worst
    possible_words = sorted(possible_words, key=rank)

    # Give new word
    time.sleep(1)
    print("Try this: " + str(possible_words[len(possible_words) - 1]).upper())

# Terminate program
print("----- Goodbye! -----")