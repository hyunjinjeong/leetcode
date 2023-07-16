class LRUCache:
    # dict랑.. doubly linked list 쓰면 될 듯.
    def __init__(self, capacity: int):
        self.ll = LinkedList()
        # key -> Node 형태로...
        self.dt = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dt:
            return -1
        
        node = self.dt[key]
        self.ll.remove_node(node)
        self.ll.append_node(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.dt:
            node = Node(key, value)
            self.dt[key] = node
            self.ll.append_node(node)
        else:
            # dt 업데이트 하고..
            node = self.dt[key]
            node.val = value
            self.ll.remove_node(node)
            self.ll.append_node(node)
        
        if len(self.dt) > self.capacity:
            head_key = self.ll.head.key
            self.dt.pop(head_key)
            self.ll.remove_head()
    
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def remove_head(self):
        self.remove_node(self.head)
    
    def remove_node(self, node):
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            node_next = node.next
            node_next.prev = None
            self.head = node_next
        elif node is self.tail:
            node_prev = node.prev
            node_prev.next = None
            self.tail = node_prev
        else:
            node_next, node_prev = node.next, node.prev
            node_next.prev = node_prev
            node_prev.next = node_next
    
    def append_node(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

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