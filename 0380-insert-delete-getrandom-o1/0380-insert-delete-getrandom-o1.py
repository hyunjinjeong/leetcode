class RandomizedSet:

    def __init__(self):
        self.index = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False

        self.array.append(val)        
        self.index[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        
        val_index = self.index[val]

        self.array[-1], self.array[val_index] = self.array[val_index], self.array[-1]
        self.index[self.array[val_index]] = val_index

        self.array.pop()
        self.index.pop(val)

        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.array) - 1)
        return self.array[random_index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()