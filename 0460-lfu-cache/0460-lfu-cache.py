class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.dll_by_freq = collections.defaultdict(DoublyLinkedList)
        self.min_freq = 0
        
        # freq마다 DLL을 만들면 되나?
        # 새 key가 put으로 들어오면 freq[1]의 맨 끝에 추가
        # get은? freq[key]가 1 늘어나고, 기존 freq[key]에서 제거한 뒤 새 freq[key]의 맨 끝에 추가하면 됨
        # 업데이트 put은? get이랑 같은 로직임
        # invalidate는? 가장 작은 freq의 맨 왼쪽 제거. invalidate 이후 해당 freq가 비면 가장 작은 freq를 1 더해줌
        # 그러면 기존 freq[key] LL에서 제거하는게 문제인데...
        # cache에 value 대신 Node를 가지고 있으면 되겠다.
        # 아니면 DLL 쓰지 않고 그냥 array로도 되지 않을라나? 추가는 append하고 제거는 swap 뒤 pop. index를 가지고 있어야 함. 일단 DLL로 해봅시다.


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._increase_frequency(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._increase_frequency(node)
            node.value = value
        else:
            self._invalidate()

            node = Node(key, value, 1)
            self.cache[key] = node
            self.min_freq = 1
            
            dll = self.dll_by_freq[1]
            dll.append_node(node)
    
    def _increase_frequency(self, node):
        freq = node.freq
        
        prev_dll = self.dll_by_freq[freq]
        prev_dll.remove_node(node)
        if prev_dll.size == 0 and self.min_freq == freq:
            self.min_freq = freq + 1

        new_dll = self.dll_by_freq[freq + 1]
        new_dll.append_node(node)

        node.freq += 1
    
    def _invalidate(self):
        if len(self.cache) < self.capacity:
            return
        
        min_freq_dll = self.dll_by_freq[self.min_freq]
        deleted_node = min_freq_dll.remove_head()

        del self.cache[deleted_node.key]


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def append_node(self, node):
        tail_dummy = self.tail
        prev_tail = tail_dummy.prev

        prev_tail.next = node
        node.prev = prev_tail
        node.next = tail_dummy
        tail_dummy.prev = node

        self.size += 1
    
    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.size -= 1
    
    def remove_head(self):
        head_dummy = self.head
        head = head_dummy.next
        
        self.remove_node(head)
        return head


class Node:
    def __init__(self, key=None, value=None, freq=None):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = None
        self.next = None

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)mm,,m