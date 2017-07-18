"""Code to autocomplete words based on a given input."""
from trie import TrieTree, Node
import sys


class AutoCompleter(TrieTree):
    """A trie tree that returns a list of suggestions based on input when called."""

    def __init__(self, vocabulary, max_completions=5):
        """Set up tree.

        Parses data (as a list or file) into tree.
        Accepts a number of completions, which is how many suggestions
        it will give when called.
        """
        self.max_completions = max_completions
        self.length = 0
        self.root = Node('.', 0, None)
        if isinstance(vocabulary, list):
            for i in range(len(vocabulary)):
                self.insert(vocabulary[i])
        elif isinstance(vocabulary, str):
            try:
                with open(vocabulary) as dictionary:
                    data = dictionary.read()
                    data = data.split('\n')
                for i in range(len(data)):
                    x = i / len(data) * 100
                    sys.stdout.write("\r%d%%" % x)
                    sys.stdout.flush()
                    self.insert(data[i])
            except FileNotFoundError:

                raise FileNotFoundError('Please enter valid list or file path.')

    def __call__(self, string):
        """Use trie traversal to return a list of suggestions based on input."""
        to_return = []
        gen = self.traversal(string)
        try:
            for i in range(self.max_completions):
                to_return.append(next(gen))
        except StopIteration:
            pass
        return to_return



if __name__ == '__main__':
    complete_me = AutoCompleter('/usr/share/dict/words', 17)
    print(complete_me('d'))