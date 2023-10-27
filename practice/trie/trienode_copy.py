# each node stores a character
class Trienode:
    def __init__(self):
        self.nodes = {}
        self.end_of_key = False
        self.freq = 0

    def add_char(self, char):
        if char not in self.nodes:
            # every character is a node in the trie
            self.nodes[char] = Trienode()
        # we need to return the node so that when we
        # add a string to the trie, we can keep moving
        # forward from node to node. See Trie class
        return self.nodes[char]