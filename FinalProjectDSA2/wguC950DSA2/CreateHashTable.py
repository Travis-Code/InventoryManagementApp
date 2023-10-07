# Defines a class named CreateHashMap, which implements a hash map.
# the hash map is initialized with a list of empty lists of a certain init capacity.
# the hash map also supports four operations:
# 1. insert: inserts a new item into the hash map
# 2. lookup: looks up an item in the hash map
# 3. hash_remove: removes an item from the hash map
# 4. the hash map uses chaining to handle collisions.
class CreateHashMap:
    # The constructor initializes an empty hash map with a list of empty lists of a certain initial capacity.
    def __init__(self, initial_capacity: object = 20) -> object:
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # The insert function inserts a new item into the hash map
    # uses chaining to handle collisions.
    # updates the value of the key if it is already in the bucket.
    # (Time complexity: O(N))
    def insert(self, key, item):
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # updates key if already in bucket
        # (Time complexity: O(N))
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # lookup looks up an item in the hash map
    # uses the hash of the key to determine the bucket where the item might be found.
    # then searches the items in that bucket to find the item with the given key.
    # (Time complexity: O(N))
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None

    # hash_remove removes an item from the hash map
    # uses the hash of the key to determine the bucket where the item might be found.
    # then removes the item with the given key from that bucket if it exists.
    # (Time complexity: O(N)
    def hash_remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        # If the key is found in the hash table then remove
        if key in destination:
            destination.remove(key)
