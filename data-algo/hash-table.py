class HashTable:

    def __init__(self, size):
        self.size = size
        self.data = [None] * size
    
    def _hash(self, key):

        h = 0;
        for i in range(len(key)):

            h = (h + ord(key[i]) * i)% self.size
        return h

    def _set(self, key, value):
        address = self._hash(key)
        
        if self.data[address] == None:
            self.data[address] = [[key, value]]
            # print(self.data)
        else:
            self.data[address].append([key, value])
            # print(self.data[address])

    def _get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        # print(len(current_bucket) > 0)
        # print(current_bucket is not None)
        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return None
           




my_hash = HashTable(50)

# print(my_hash._set('grapes', 10000))
my_hash._set('grapes', 10000)
# print(my_hash._set('apples', 54))
print(my_hash._get('grapes'))
# print(my_hash.data)