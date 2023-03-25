class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. 일단 set 활용한 거
        s, ans = set(nums), 0
        
        for num in s:
            # 여기서 -1 체크하는 이유는 +1 ...로 검사하기 때문에.
            if num - 1 in s:
                continue
            
            j = 1
            while num + j in s:
                j += 1
            
            ans = max(ans, j)
        
        return ans