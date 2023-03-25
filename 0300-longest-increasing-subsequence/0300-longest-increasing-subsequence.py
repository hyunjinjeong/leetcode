class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def binary_search(target, left, right):
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            
            return left
            
        
        # binary search를 이용하면 O(nlogn) 가능
        # tails[i]는 길이가 i+1인 LIS의 tail을 의미함.
        tails = []
        for num in nums:
            idx = binary_search(num, 0, len(tails))
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)