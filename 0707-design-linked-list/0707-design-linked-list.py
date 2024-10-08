class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index > self.length:
            return -1
        node = self.head
        while index:
            node = node.next
            index -= 1
        return node.val

    def addAtHead(self, val: int) -> None:
        new_node = MyNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.head
            new_node.next = tmp
            tmp.prev = new_node
            self.head = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = MyNode(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.tail
            new_node.prev = tmp
            tmp.next = new_node
            self.tail = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            node = self.head
            while index:
                node = node.next
                index -= 1
            new_node = MyNode(val)

            node.prev.next = new_node
            new_node.prev = node.prev
            new_node.next = node
            node.prev = new_node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return
        
        if index == 0 and index == self.length - 1: # head & tail
            self.head = None
            self.tail = None
        elif index == 0: # head
            self.head = self.head.next
            self.head.prev = None
        elif index == self.length - 1: # tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node = self.head
            while index:
                node = node.next
                index -= 1
            node.prev.next = node.next
            node.next.prev = node.prev

        self.length -= 1
        
        
class MyNode:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)