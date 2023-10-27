# stores strings that are made up of chars (nodes)
class Trie:
    def __init__(self):
        self.root = Trie()

    def add_string(self, string):
        current_node = self.root
        for char in string:
            current_node = current_node.add_char(char)
            current_node.freq += 1
        current_node.end_of_key = True

    def search_string(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node.nodes:
                return False
            current_node = current_node.nodes[char]
        return current_node.end_of_key

    def count_prefix(self, string):
        current_node = self.root
        for char in string:
            if char not in current_node.nodes:
                return 0
            current_node = current_node.nodes[char]
        return current_node.freq
                