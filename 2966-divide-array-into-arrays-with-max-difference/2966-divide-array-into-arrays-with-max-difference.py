class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        # 정렬해서 순서대로 넣으면 되는거 아닌가? 반례가 있으려나
        nums.sort()

        start = 0
        res = []
        for i in range(len(nums) // 3):
            res.append([])
            for j in range(start, start + 3):
                res[i].append(nums[j])
            
            if res[i][2] - res[i][0] > k:
                return []
            
            start += 3
        
        return res