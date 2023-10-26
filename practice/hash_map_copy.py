class Hashmap:
    def __init__(self, array_size=10):
        self.array_size = array_size
        self.array = [None] * array_size

    def _hash(self, key):
        key_byte = key.encode()
        hashed_key = sum(key_byte)
        return hashed_key

    def compress(self, hashed_key):
        return hashed_key % self.array_size

    def calculate_index(self, key, collisions=0):
        hashed_key = self._hash(key)
        index = self.compress(hashed_key)
        return index + collisions

    def assign(self, key, value):
        index = self.calculate_index(key)
        key_val = self.array[index]

        if not key_val:
            self.array[index] = [key, value]
            return
        elif key_val[0] == key:
            self.array[index][1] = value
        else:
            collisions = 1            
            while key_val[0] != key:
                new_index = self.calculate_index(key, collisions)
                key_val = self.array[new_index]
                if not key_val:
                    self.array[new_index] = [key, value]
                    return
                elif key_val[0] == key:
                    self.array[new_index][1] = value
                else:
                    collisions += 1

    def retrieve(self, key):
        index = self.calculate_index(key)
        key_val = self.array[index]

        if not key_val:
            return "Key not found in hash map"
        elif key_val[0] == key:
            return self.array[index][1]
        else:
            collisions = 1
            while key_val[0] != key:
                new_index = self.calculate_index(key, collisions)
                key_val = self.array[new_index]
                if not key_val:
                    return "Key not found in hash map"
                elif key_val[0] == key:
                    return self.array[new_index][1]
                else:
                    collisions += 1

## Uncomment these lines to test
## Test HashMap
#hash_map = Hashmap(20)
#hash_map.assign("gneiss", "metamorphic")
#hash_map.assign("hneisr", "metamorphic")  # collision with "gneiss"
#hash_map.assign("basalt", "igneous")
#hash_map.assign("casals", "igneous")  # collision with "basalt"
#
## Retrieve values
#''' collision clustering  '''
#print(hash_map.retrieve("fneist"))
#''' retrieves "metamorphic" after 1 collision '''
#print(hash_map.retrieve("hneisr"))
#''' retrieves "igneous" without collision '''
#print(hash_map.retrieve("basalt"))