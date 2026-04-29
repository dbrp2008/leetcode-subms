class RandomizedSet:

    def __init__(self):
        self.data_list = []
        self.val_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx_to_remove = self.val_to_idx[val]
        last_element = self.data_list[-1]
        self.data_list[idx_to_remove] = last_element
        self.val_to_idx[last_element] = idx_to_remove
        self.data_list.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data_list)        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()