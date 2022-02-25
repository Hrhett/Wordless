# Get list of words from file
def load_words(file_path: str) -> list:
    # Open words file
    words_file = open("words.txt", 'r')

    # Read in words file
    lines = []
    with words_file as file:
        lines = file.readlines()

    # Close words file
    words_file.close()

    # Populate words list
    words = []
    for line in lines:
        words.append(line.strip().lower())

    # Return list
    return words