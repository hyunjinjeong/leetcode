class LRUCache:
    # dict랑.. doubly linked list 쓰면 될 듯.
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._dt = {}
        self._head = Node(None, None)
        self._tail = Node(None, None)
        self._head.next = self._tail
        self._tail.prev = self._head

    def get(self, key: int) -> int:
        if key not in self._dt:
            return -1
        
        node = self._dt[key]
        self._remove(node)
        self._append(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._dt:
            self._remove(self._dt[key]) # LL에서만 갱신하기 위해...
        
        node = Node(key, value)
        self._append(node)
        self._dt[key] = node
        
        if len(self._dt) > self._capacity:
            first = self._head.next
            self._remove(first)
            self._dt.pop(first.key)
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _append(self, node):
        prev_tail = self._tail.prev
        
        prev_tail.next = node
        node.next = self._tail
        node.prev = prev_tail
        self._tail.prev = node
        

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)