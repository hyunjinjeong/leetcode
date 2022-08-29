class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 일단 naive한 방법... 정렬한 다음에 이렇게 비교하면 된당.
        nums.sort()
        
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        
        return len(nums)
    
        # Follow-up으로 O(1) 공간과 O(n) 시간 복잡도로 해결해야 함.
        