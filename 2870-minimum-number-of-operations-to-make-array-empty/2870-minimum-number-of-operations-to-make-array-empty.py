class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # count 세서 하나씩 하면 되는거 아닌가
        # 2 -> 4, 3 -> 3, 4 -> 2
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        res = 0
        for num in count:
            num_count = count[num]
            if num_count == 1:
                return -1
            if num_count % 3 == 0:
                res += num_count // 3
            elif num_count % 3 == 1:
                res += (num_count - 4) // 3 + 2
            else:
                res += num_count // 3 + 1
        
        return res