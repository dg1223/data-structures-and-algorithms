# open addressing with linear probing
class Hashmap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None] * array_size

    def _hash(self, key, collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + collisions

    def compress(self, hashed_key):
        return hashed_key % self.array_size

    def calculate_index(self, key, collisions=0):
        hashed_key = self._hash(key, collisions)
        index = self.compress(hashed_key)
        return index

    def assign(self, key, value):
        index = self.calculate_index(key)
        key_val = self.array[index]

        if not key_val:
            self.array[index] = [key, value]
            return
        elif key_val[0] == key:
            self.array[index][1] == value
            return
        # collision
        else:
            collisions = 1
            while self.array[index][0] != key:
                new_index = self.calculate_index(key, collisions)
                key_val = self.array[new_index]
                if not key_val:
                    self.array[new_index] = [key, value]
                    return
                elif self.array[new_index][0] == key:
                    self.array[new_index][1] = value
                    return
                else:
                    collisions += 1

    def retrieve(self, key):
        index = self.calculate_index(key)
        retrieval_key_val = self.array[index]

        if not retrieval_key_val:
            return "Key not found in hash map"
        elif retrieval_key_val[0] == key:
            return retrieval_key_val[1]
        else:
            collisions = 1
            while retrieval_key_val[0] != key:
                new_index = self.calculate_index(key, collisions)
                retrieval_key_val = self.array[new_index]
                if not retrieval_key_val:
                    return "Key not found in hash map"
                elif retrieval_key_val[0] == key:
                    return retrieval_key_val[1]
                else:
                    collisions += 1

# Test HashMap
hash_map = Hashmap(20)
hash_map.assign("gneiss", "metamorphic")
hash_map.assign("hneisr", "metamorphic")  # collision with "gneiss"
hash_map.assign("basalt", "igneous")
hash_map.assign("casals", "igneous")  # collision with "basalt"

# Retrieve values
''' collision clustering  '''
print(hash_map.retrieve("fneist"))
''' retrieves "metamorphic" after 1 collision '''
print(hash_map.retrieve("hneisr"))
''' no collision '''
print(hash_map.retrieve("basalt"))
            
            