"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Reads words in from a list and generates a random word from the list.

    >>> wf = WordFinder("words.txt")
    235886 words read

    >>> wf.random() in strips
    True

    >>> wf.random() in strips
    True

    >>> wf.random() in strips
    True
    """

    def __init__(self, path):
        """Reads list of words and reports back the number of words in the list"""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        strips = [word.strip() for word in dict_file]
        return strips

    def random(self):
        """Returns random word from the list."""

        return random.choice(self.words)
