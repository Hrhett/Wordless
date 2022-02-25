# Imports
import time
import helper
from archive import Archive
from word import Word

# Settings
green_status = '@'
yellow_status = '?'
grey_status = '!'
found_characters_before_guess = 2

# Create archive
archive = Archive()

# Define rank getting method
def rank(word):
    # Initialize rank
    rank = 0
    
    # Grab the letters
    letters = archive.get_newest().letters

    # Loop through letters
    for index in range(5):
        # Get used letter
        used_letter = letters[index]
        
        # Check for matching letter positions
        if used_letter.status == green_status: # In this position
            # Check if character at index in past
            if letters[index].character == word[index]: rank += 10
        elif used_letter.status == yellow_status: # In word but not in this position
            # Check if letter is in word
            if letters[index].character in word:
                # Increase rank
                rank += 2

                # Check if character at index
                if letters[index].character == word[index]: rank -= 20
            else: rank -= 20
        elif used_letter.status == grey_status: # Not in word or already used in another position
            # Check if letter is in word
            if letters[index].character in word: rank -= 2

            # Check if letter is at character
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
    print(green_status + ": GREEN")
    time.sleep(0.5)
    print(yellow_status + ": YELLOW")
    time.sleep(0.5)
    print(grey_status + ": GREY")
    time.sleep(3)
    print(
        "Like so: "
        + grey_status + "C"
        + green_status + "R"
        + grey_status + "A"
        + yellow_status + "N"
        + grey_status + "E"
    )
    time.sleep(3)
    print("The program will run until you enter EXIT.")
    time.sleep(2)

# Create counter for uses
uses = 1

# Loop through tried
while True:
    # Get user input
    time.sleep(1)
    user_input = input("\nAttempt " + str(uses) + ": ").replace(" ", "").lower()
    if user_input == 'exit': break
    if len(user_input) != 10:
        print("Input formatting wrong.")
        continue
    uses += 1

    # Encode user input
    new_word = Word(user_input)
    archive.add(new_word)

    # Ask user to wait around
    time.sleep(1)
    print(str(new_word).upper() + "? Excellent. Let me think up a suggestion for your next word.")

    # Sort words from best choices to worst
    possible_words = sorted(possible_words, key=rank)

    # Give new word
    time.sleep(1)
    print("Try this: " + str(possible_words[len(possible_words) - 1]).upper())

# Terminate program
print("----- Happy to be of service! -----")