from trienode import Trienode
from trie import Trie

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
    prefix_count = trie.count_prefix(prefix)
    print(f"Prefix count for {prefix} = {prefix_count}")