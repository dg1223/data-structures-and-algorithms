class Trienode:
    def __init__(self):
        self.nodes = {}
        self.end_of_key = False
        self.freq = 0

    def add_char(self, char):
        if char not in self.nodes:
            # every character is a node in the trie
            self.nodes[char] = Trienode()
        return self.nodes[char]