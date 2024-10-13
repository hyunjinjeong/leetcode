class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # count를 세서... heap 이용해서 많은거부터 하나씩 넣으면 되려나?
        # row 크기는 가장 높은 count랑 같을 거고
        counter = collections.Counter(nums)
        heap = [(-count, num) for num, count in counter.items()]
        heapq.heapify(heap)

        res = [[] for _ in range(-heap[0][0])]
        while heap:
            count, num = heapq.heappop(heap)
            for i in range(-count):
                res[i].append(num)
        
        return res