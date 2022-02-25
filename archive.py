# Imports
from word import Word

# Class for storing attempts
class Archive:
    # Variables
    databank = []
    
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
    def characters_used_of_status(self, status: str) -> int:
        # Create counter
        found_characters = set()

        # Loop through archive
        for word in self.databank:
            # Loop through letters
            for letter in word.letters:
                # Check if letter is of status type
                if status == letter.status:
                    # Add to count
                    found_characters.add(letter.character)

        # Return count
        return len(found_characters)

    # Check for character in archive
    def character_in_position(self, character: str, status: str, position: int) -> bool:
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