class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # heap을 쓸 필요도 없구나
        freq = [0] * (len(nums) + 1)

        res = []
        for num in nums:
            if freq[num] >= len(res):
                res.append([])
            
            res[freq[num]].append(num)
            freq[num] += 1

        return res