class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # least number of unique integers니까.. 갯수가 적은 것부터 삭제해야 하나?
        # 그럼 그냥 heap 쓰면 될 듯
        counter = collections.Counter(arr)
        
        heap = [(count, num) for num, count in counter.items()]
        heapq.heapify(heap)

        res = len(heap)
        while k:
            count, num = heapq.heappop(heap)
            if count > k:
                break
            
            k -= count
            res -= 1
        
        return res