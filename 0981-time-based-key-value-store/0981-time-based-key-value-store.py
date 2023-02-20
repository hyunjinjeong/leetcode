class TimeMap:
    # hash table에 저장하고 없는 값이 들어오면 어떻게 처리하면 될 것 같은디
    # 일단 가장 단순한건 1까지 내려가면서 찾으면 됨. => TLE 뜸.
    # 그 담에 최적 솔루션은..?!
    # binary search를 사용하면 된다고 한다.
    # strictly increasing이니까 array append만 해도 정렬되어 있음.
    
    def __init__(self):
        self._time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self._time_map:
            self._time_map[key] = []
        self._time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self._time_map.get(key)
        if not arr:
            return ""
        
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            curr_timestamp = arr[mid][0]
            
            if curr_timestamp <= timestamp:
                left = mid + 1
            else:
                right = mid
            
        # 이 시점에서 right는 timestamp보다 큰 가장 작은 index. 따라서 같거나 작은건 -1 해줘야 함.
        # right가 0이면 모든 원소가 timestamp보다 큰 거.
        return arr[right-1][1] if right > 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)