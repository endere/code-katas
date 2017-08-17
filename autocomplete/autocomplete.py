from trie import TrieTree, Node
import sys


class AutoCompleter(TrieTree):

    def __init__(self, vocabulary, max_completions=5):
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
        to_return = []
        gen = self.traversal(string)
        try:
            for i in range(self.max_completions):
                to_return.append(next(gen))
        except StopIteration:
            pass
        return to_return



if __name__ == '__main__':
    # complete_me = AutoCompleter('/usr/share/dict/words')
    complete_me = AutoCompleter(['test', 'hello', 4])

    print(complete_me('dino'))


    #/django-imager/imagersite$ /home/ubuntu/django-imager/ENV/bin/gunicorn imagersite.wsgi:application