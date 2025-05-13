class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # # ?? 직접 만드는거 말고 다른 방법이 있나
        # MOD = 10 ** 9 + 7

        # subarray_sum = []
        # for i in range(len(nums)):
        #     curr = 0
        #     for j in range(i, len(nums)):
        #         curr += nums[j]
        #         subarray_sum.append(curr)
        
        # subarray_sum.sort()
        
        # res = 0
        # for i in range(left - 1, right):
        #     res = (res + subarray_sum[i]) % MOD
        # return res

        # 놀랍게도 2개나 더 있네; heap이랑 binary search
        # heap의 직관은 숫자가 양수만 있으니까 커지기만 함. 즉 가장 작은 숫자는 이미 array에 있고,
        # 거기서부터 시작해서 heap으로 하나씩 빼고, 오른쪽으로 늘려가면서 넣으면 구할 수 있다는 것
        MOD = 10**9 + 7

        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        res = 0
        for i in range(right):
            num, index = heapq.heappop(heap)
            if i >= left - 1:
                res = (res + num) % MOD
            
            if index < len(nums) - 1:
                heapq.heappush(heap, (num + nums[index + 1], index + 1))
        
        return res
