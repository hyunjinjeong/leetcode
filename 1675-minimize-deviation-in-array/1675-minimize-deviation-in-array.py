class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # max heap을 사용하면 된다?
        # 1 -> heap에 2 넣기. min은 1
        # 2 -> heap에 2 넣기. min은 1
        # 3 -> heap에 6 넣기. min
        # 4 -> heap에 4 넣기.

        # 그러면 min max를 보자
        # 6 4 2 2 순으로 뽑혀 나옴
        # 첨에 6은 min max가 6인데... 3이 되니까 min 3 max 6
        minimum = float("inf")
        evens = []
        for num in nums:
            even = num * 2 if num % 2 == 1 else num
            minimum = min(even, minimum)
            evens.append(-even)
        
        heapq.heapify(evens)

        res = float("inf")
        while evens:
            curr = -heapq.heappop(evens)
            res = min(curr - minimum, res)
            
            if curr % 2 == 1: # 현재가 홀수면 최댓값이 더 이상 작아질 수 없음.
                break
            minimum = min(minimum, curr // 2)
            heapq.heappush(evens, -(curr // 2))

        return res