class MyHashSet:

    def __init__(self):
        self.num_buckets = 31
        self.buckets = [[] for i in range(self.num_buckets)]

    def add(self, key: int) -> None:
        index = key % self.num_buckets
        if key not in self.buckets[index]:
            self.buckets[index].append(key)

    def remove(self, key: int) -> None:
        index = key % self.num_buckets
        if key in self.buckets[index]:
            self.buckets[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.num_buckets
        return key in self.buckets[index]        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)