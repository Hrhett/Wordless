# Imports
from word import Word

# Class for storing attempts
class Archive:
    # Variables
    databank = []

    # Constructor
    def __init__(self) -> None:
        pass
    
    # Add to archive
    def add(self, word: Word):
        # Add to databank
        self.databank.append(word)

    # Get top of archive
    def get_newest(self) -> Word:
        # Return last word
        databank_length = len(self.databank)
        return self.databank[databank_length - 1]

    # Get number of letters in a row
    def characters_at_position(self, character: str, status: str, position: int):
        # Create counter
        count = 0

        # Loop through archive
        for word in self.databank:
            # Get letter
            letter = word.letters[position]

            # Check if letter in position
            if character == letter.character and status == letter.status:
                # Add to count
                count += 1

        # Return count
        return count

    # Check for character in archive
    def character_at_position(self, character: str, status: str, position: int):
        # Loop through archive
        for word in self.databank:
            # Get letter
            letter = word.letters[position]

            # Check if character matches
            if character == letter.character and status == letter.status:
                return True

        # Character not found
        return False

    # To string method
    def __str__(self) -> str:
        # Return databank
        return self.databank