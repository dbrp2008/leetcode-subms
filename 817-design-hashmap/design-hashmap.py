class MyHashMap:

    def __init__(self):
        self.num_buckets = 41
        self.buckets = [[] for i in range(self.num_buckets)]

    def put(self, key: int, value: int) -> None:
        index = key % self.num_buckets
        for item in self.buckets[index]:
            if item[0] == key:
                item[1] = value 
                return
        self.buckets[index].append([key, value])

    def get(self, key: int) -> int:
        index = key % self.num_buckets
        for ke, value in self.buckets[index]:
            if ke == key:
                return value
        return -1 

    def remove(self, key: int) -> None:
        index = key % self.num_buckets
        for i, (ke, value) in enumerate(self.buckets[index]):
            if ke == key:
                self.buckets[index].pop(i)
                return        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)