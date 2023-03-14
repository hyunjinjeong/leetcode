class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._dt = collections.defaultdict(int)

    def get(self, key: int) -> int:
        if key not in self._dt:
            return -1
        
        val = self._dt[key]
        del self._dt[key]
        self._dt[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self._dt:
            del self._dt[key]
        self._dt[key] = value
        
        if len(self._dt) > self._capacity:
            first = next(iter(self._dt))
            del self._dt[first]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)