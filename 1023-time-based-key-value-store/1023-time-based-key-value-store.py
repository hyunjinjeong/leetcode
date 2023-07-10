class TimeMap:

    def __init__(self):
        # 자료구조는 일단 dict가 필요할 듯?
        # k는 key로, v가 문젠데... value와 timestamp를 모두 저장할 수 있어야 함
        # 일단 간단하게 (timestamp, value)로 해보자..
        self.dt = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dt:
            self.dt[key] = []

        # 정렬할 필요가 없음. strictly increasing이기 떄문에. 또 pop() 연산도 없고...
        self.dt[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dt.get(key)
        if not arr:
            return ""
        
        # 제일 쉬운 방법은 timestamp부터 1까지 쭉 내려가면서 있는지 찾는 것...이고
        # 정렬되어 있기 때문에 binary search 활용 가능.
        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_timestamp = arr[mid][0]
            if timestamp == mid_timestamp:
                return arr[mid][1]
            
            if timestamp > mid_timestamp:
                lo = mid + 1
            else:
                hi = mid - 1

        # 이 상태에서 lo는 timestamp_prev > timestamp인 leftmost index 상태.
        # 즉 lo - 1이 답이 될듯?
        return arr[lo-1][1] if lo > 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)