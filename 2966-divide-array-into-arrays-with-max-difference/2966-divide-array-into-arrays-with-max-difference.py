class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # 정렬해서 순서대로 넣으면 되는거 아닌가? 반례가 있으려나
        nums.sort()

        res = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append([nums[i], nums[i + 1], nums[i + 2]])
        
        return res