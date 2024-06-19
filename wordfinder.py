"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    """Word Finder: finds random words from a dictionary.
    
    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random()  # Will be one of the words from the file
    'example_word'
    """
    
    def __init__(self, path):
        """Initialize WordFinder with a path to a file and read the words from the file."""
        self.path = path
        self.words = self.read_words()
        print(f"{len(self.words)} words read")

    def read_words(self):
        """Read the words from the file, stripping newline characters, and return them as a list."""
        with open(self.path, 'r') as file:
            return [line.strip() for line in file]

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)

# Example usage:
# wf = WordFinder("words.txt")
# print(wf.random())
