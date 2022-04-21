class MyHashSet(object):

    def __init__(self):
        self.size = 10000
        self.arr = [None] * self.size

    #     Creates hash value based on the given key
    def calc_hash_val(self, key):
        return key % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_val = self.calc_hash_val(key)

        if self.arr[hash_val] == None:
            self.arr[hash_val] = [key]
        else:
            self.arr[hash_val].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_val = self.calc_hash_val(key)
        if self.arr[hash_val] != None:
            while key in self.arr[hash_val]:
                self.arr[hash_val].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        hash_val = self.calc_hash_val(key)

        if self.arr[hash_val] != None:
            return key in self.arr[hash_val]

# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))

