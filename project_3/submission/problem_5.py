class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):

        for char in self.children:
                yield from self.children[char].suffixes(suffix+char)

        if self.is_word:
            yield suffix

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

print('<< Test Cases >>')
prefix = 'a'
print('\nWord paths under the prefix "{}":\n{}'.format(prefix,'\n'.join(MyTrie.find(prefix).suffixes(prefix))))
prefix = 'f'
print('\nWord paths under the prefix "{}":\n{}'.format(prefix,'\n'.join(MyTrie.find(prefix).suffixes(prefix))))
prefix = 'tri'
print('\nWord paths under the prefix "{}":\n{}'.format(prefix,'\n'.join(MyTrie.find(prefix).suffixes(prefix))))
prefix = ''
print('\nWord paths under the prefix "{}":\n{}'.format(prefix,'\n'.join(MyTrie.find(prefix).suffixes(prefix))))
prefix = 'x'
print('\nIs "{}" found in this Trie?:\n{}'.format(prefix, MyTrie.find(prefix)is not None))
prefix = ''
print('\nIs "{}" found in this Trie?:\n{}'.format(prefix, MyTrie.find(prefix)is not None))
