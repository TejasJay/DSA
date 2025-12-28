# key - value pairs
# keys are uniques but values can be same
# key1 -> value1
# key2 -> value1
# key3 -> value2
# key4 -> value3

# This uses a hash function to work
# We pass the key into a hash function and get the index position of the key, this index leads to position where we can find the value
# for the same key we always get the same index
# when we hash a key using a hash function it assigns a position in the hashmap and everytime we need to search the key or value, we pass it to the hash function to get the position of its value.

# collision handling - when a hash function assigns the same position in the hashmap for different keys
# how to handle it?
# If there are empty spaces in the hashmap, we jump to the nearest empty space and assign the key that is causing the collision to that position.
# Now everytime we need to find that key we first land on the spot where collision happened and then we need to jump to the new spot that was assigned to that key to find its value.
# If we have a good hash function we can avoid collisions from happening
# if we have a bad hash function then wrost case would be linear time - O(n)

# we ca also use buckets, [[], [], [], [], []] which is basically a list of lists.
# if we want to hash a key 'name' and value 'Mike', the hash function returns postion 3, we append it to that list.
# it would now look like [[], [], [], ['Mike'], []]
# Now if we want to hash a key 'job' and value 'Programmer' and the hash function returns postion 3 again, then we append it to the list.
# it would now look like [[], [], [], ['Mike', 'Programmer'], []]
# worst case all the values would end up in the same list and we need to treat it like a list

class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity # capacity is the number of buckets we look to create
        self.size = 0 # The number of elements in the bucket
        self.buckets = [[] for _ in range(capacity)]
    
    # O(1)
    def __len__(self):
        return self.size

    # Worst: O(n)
    # Average: O(1)
    # depends on the quality of the hash function
    def __contains__(self, key):
        index = self._hash_function(key) # convert key to its hash index
        bucket = self.buckets[index] # retreive the bucket with that index
        for k, v in bucket: # every bucket stores both its key & value like [(k, v)]
            if k == key: 
                return True
        return False

    # Worst: O(n)
    # Average: O(1)
    # depends on the quality of the hash function
    def put(self, key, value):
        index = self._hash_function(key) # convert key to its hash index
        bucket = self.buckets[index] # retreive the bucket with that index
        for i, (k, v) in enumerate(bucket): # we go through all the elements in the bucket
            if k == key: # if we find a key
                bucket[i] = (key, value) # we update the value
                break # if key key is found, then we break out, so the next lines wont execute
        else: # if key isnt found, we dont break out of the above loop, then the below lines executes (for else python syntax)
            bucket.append((key, value)) # we append the new key and value in the buckets index
            self.size += 1

    # Worst: O(n)
    # Average: O(1)
    # depends on the quality of the hash function
    def get(self, key):
        index = self._hash_function(key) # convert key to its hash index
        bucket = self.buckets[index] # retreive the bucket with that index
        for k, v in bucket: # every bucket stores both its key & value like [(k, v)]
            if k == key: 
                return v
        raise KeyError("Key not present")

    # Worst: O(n)
    # Average: O(1)
    # depends on the quality of the hash function
    def remove(self, key):
        index = self._hash_function(key) # convert key to its hash index
        bucket = self.buckets[index] # retreive the bucket with that index
        for i, (k, v) in enumerate(bucket): # every bucket stores both its key & value like [(k, v)]
            if k == key: 
                del bucket[i]
                self.size -= 1
                break
        else: # for else syntax
            raise KeyError("Key not present")

    # O(m + n) = O(n)
    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    # O(m + n) = O(n)
    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    # O(m + n) = O(n)
    def items(self):
        return [(k,v) for bucket in self.buckets for k, v in bucket]

    # O(k) - linear in key lenght
    # O(1) - ideally if the key lenght is small, because keys are not very large
    def _hash_function(self, key):
        # we convert the key to str first
        # we loop through every char in the str 
        # we find the integer result for every character using ord
        # Multiply by 31 is a common trick to “mix” values (a small prime helps spread).\
        # Multiply by ord(c) injects the character.
        # % self.capacity keeps it within valid bucket range.
        ### Tiny example (capacity = 10, key = "ab") ###
        # Using the fixed formula:
        # start h = 0
        # 'a' (97): h = (0*31 + 97) % 10 = 7
        # 'b' (98): h = (7*31 + 98) % 10 = (217 + 98) % 10 = 315 % 10 = 5
        # So "ab" hashes to index 5.
        key_string = str(key)
        hash_result = 0
        for c in key_string:
            hash_result = (hash_result * 31 + ord(c)) % self.capacity
        return hash_result


if __name__ == "__main__":
    hash_map = HashMap(capacity = 32)

    hash_map.put('name', 'Tj')
    hash_map.put('age', 30)
    hash_map.put('job', 'Programmer')
    hash_map.put('name', 'Jake')
    hash_map.put('name', 'Alex')

    print(hash_map.items())

    hash_map.put('name', 'Tj')
    hash_map.put('age', 30)
    hash_map.put('job', 'Programmer')
    hash_map.put('name1', 'Jake')
    hash_map.put('name2', 'Alex')

    print(hash_map.items())

    print(hash_map.buckets)

