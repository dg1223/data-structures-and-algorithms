class TrieNode:
	def __init__(self):
		self.nodes = {}
		self.freq = 0
		self.end_of_key = False

	def add_char(self, char):
		if char not in self.nodes:
			self.nodes[char] = TrieNode()
		return self.nodes[char]

class Trie:
	def __init__(self):
		self.root = TrieNode()

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


trie = Trie()

words = ["AMBER", "ALICE", "AMPLE", "BALLOON", "BALL", \
"BLAST", "BAND", "DENSE", "DUTCH", "DECK", "DANCE", \
"DRAMA", "MESS", "MAVERICK", "MAVEN", "PHYSICS", "PHONE", \
"PHANTOM", "PASS", "PEAK", "PACK", "ZEST", "ZEAL", "ZAP", "ZIP", "ZIPPER"]

for word in words:
	trie.add_string(word)

more_words = ["APPLE", "AMPLIFIER", "AMPLE", "BALLOON", \
"BALL", "DART", "DUTCH", "DECK", "DRAM", "FLAG", "MOP", \
"MAVERICK", "MANSION", "PHYSICS", "PHONE", "PHANTOM", \
"PASS", "PECK", "PAIN", "ZAM", "ZEST", "ZAP", "ZIP", "ZEBRA"]

for word in more_words:
	if trie.search_string(word):
		print(word)

print()

prefixes = ["A", "AM", "B", "BALL", "BA", "C", "CA", \
"DUTCH", "DECK", "GA", "J", "MA", "P", "PH", "PE", "Z", "ZIP"]

for prefix in prefixes:
	print(f"Prefix count of {prefix} = {trie.count_prefix(prefix)}")