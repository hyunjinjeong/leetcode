class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num2_index = {}
        for i, num2 in enumerate(nums2):
            num2_index[num2] = i
        
        ans = []
        for i, num1 in enumerate(nums1):
            next_gt = -1
            for j in range(num2_index[num1] + 1, len(nums2)):
                num2 = nums2[j]
                if num2 > num1:
                    next_gt = num2
                    break
            ans.append(next_gt)
        
        return ans