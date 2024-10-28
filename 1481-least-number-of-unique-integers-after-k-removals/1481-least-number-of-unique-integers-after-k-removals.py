class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # # least number of unique integers니까.. 갯수가 적은 것부터 삭제해야 하나?
        # # 그럼 그냥 heap 쓰면 될 듯
        # counter = collections.Counter(arr)
        
        # heap = list(counter.values())
        # heapq.heapify(heap)

        # res = len(heap)
        # while k:
        #     count = heapq.heappop(heap)
        #     if count > k:
        #         break
            
        #     k -= count
        #     res -= 1
        
        # return res
        
        # Counting Sort도 된다
        counter = collections.Counter(arr)

        count_list = [0] * (len(arr) + 1)
        for count in counter.values():
            count_list[count] += 1
        
        res = len(counter)
        for i in range(1, len(count_list)):
            if k >= i * count_list[i]:
                remove = count_list[i]
                k -= i * remove
                res -= count_list[i]
            else:
                remove = k // i
                k -= remove
                res -= remove
                break
        
        return res