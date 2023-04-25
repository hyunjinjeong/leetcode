class RandomizedSet:

    def __init__(self):
        self.positions = {}
        self.items = []

    def insert(self, val: int) -> bool:
        # 요건 O(1)
        if val in self.positions:
            return False
        
        self.items.append(val)
        self.positions[val] = len(self.items) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.positions:
            return False
        
        # O(1)을 하려면 pop()으로 맨 오른쪽만 삭제해야 함.
        # 와.. 마지막 원소랑 삭제 대상이랑 swap한 다음에 마지막 원소를 pop하는 방법이 있네;;;
        # swap
        last_item_index, target_index = len(self.items) - 1, self.positions[val]
        self.items[last_item_index], self.items[target_index] = self.items[target_index], self.items[last_item_index]
        # 포지션도 업데이트
        self.positions[self.items[target_index]] = target_index
        # pop
        self.items.pop()
        self.positions.pop(val)
        return True
        

    def getRandom(self) -> int:
        # 요것도 O(1)
        index = random.randint(0, len(self.items) - 1)
        return self.items[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()