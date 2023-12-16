class MyHashSet:

    def __init__(self):
        self.set = [Node(None) for _ in range(10**4)]

    def add(self, key: int) -> None:
        index = key % len(self.set)
        node = self.set[index]
        while node.next:
            if node.next.val == key:
                return
            node = node.next
        node.next = Node(key)

    def remove(self, key: int) -> None:
        index = key % len(self.set)
        node = self.set[index]
        while node.next:
            if node.next.val == key:
                node.next = node.next.next
                return
            node = node.next

    def contains(self, key: int) -> bool:
        index = key % len(self.set)
        node = self.set[index]
        while node.next:
            if node.next.val == key:
                return True
            node = node.next
        return False


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)