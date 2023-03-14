class LRUCache:
#     # 파이썬 걍 dict도 순서 보장이라서 이렇게 해도되는데,
#     # 내부적으로는 결국 hashmap + doubly linked list.
#     def __init__(self, capacity: int):
#         self._capacity = capacity
#         self._dt = collections.defaultdict(int)

#     def get(self, key: int) -> int:
#         if key not in self._dt:
#             return -1
        
#         val = self._dt[key]
#         del self._dt[key]
#         self._dt[key] = val
#         return val

#     def put(self, key: int, value: int) -> None:
#         if key in self._dt:
#             del self._dt[key]
#         self._dt[key] = value
        
#         if len(self._dt) > self._capacity:
#             first = next(iter(self._dt))
#             del self._dt[first]
    # 2. HashMap + Doubly Linked List 방법
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._dt = collections.defaultdict(int)
        self._head = Node(None, None)
        self._tail = Node(None, None)
        self._head.next = self._tail
        self._tail.prev= self._head

    def get(self, key: int) -> int:
        if key not in self._dt:
            return -1
        
        node = self._dt[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self._dt:
            self._remove(self._dt[key]) # LL에서만 갱신하기 위해...
        
        node = Node(key, value)
        self._add(node)
        self._dt[key] = node
        
        if len(self._dt) > self._capacity:
            first = self._head.next
            self._remove(first)
            del self._dt[first.key]
    
    def _remove(self, node):
        prev = node.prev
        _next = node.next
        
        prev.next = _next
        _next.prev = prev
    
    def _add(self, node): # 맨 뒤에 추가. LRU니까 맨 앞이 least.
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