class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
        # 어케 생각한겨...
        count = 0
        max_length = 0
        
        dt = {0:-1}
        for index, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in dt:
                max_length = max(max_length, index - dt[count])
            else:
                dt[count] = index
        
        return max_length