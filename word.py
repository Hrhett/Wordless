# Word class
class Word:
    # Constructor
    def __init__(self, encoded_word: str) -> None:
        # Initialize letters
        self.letters = []

        # Separate letters with encodings
        encoded_letters = [encoded_word[index : index + 2] for index in range(0, len(encoded_word), 2)]

        # Fill in class
        for encoded_letter in encoded_letters:
            self.letters.append(Letter(encoded_letter[1].lower(), encoded_letter[0]))

    # To string method
    def __str__(self) -> str:
        # Convert to string
        word = ""
        for letter in self.letters:
            word = word + str(letter)

        # Return string
        return word

# Letter class
class Letter:
    # Constructor
    def __init__(self, character: str, status: str) -> None:
        # Set variables
        self.character = character
        self.status = status

    # To string method
    def __str__(self) -> str:
        # Return string version of class
        return self.character