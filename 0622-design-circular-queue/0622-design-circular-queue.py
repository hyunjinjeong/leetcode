class MyCircularQueue:

    def __init__(self, k: int):
        self.front = None
        self.rear = None
        self.size = 0
        self.limit = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        node = Node(value)
        if self.isEmpty():
            self.front = node
        else:
            self.rear.next = node
            node.prev = self.rear
        
        self.rear = node
        self.size += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.front = self.front.next
        self.size -= 1
        
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.limit
        

class Node:
    def __init__(self, value, prev=None, nxt=None):
        self.value = value
        self.prev = prev
        self.next = nxt

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()